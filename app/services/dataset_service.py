from uuid import UUID

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.ai.insight_generator import InsightGenerator
from app.ai.recommendation_engine import RecommendationEngine
from app.analytics.correlation import CorrelationAnalyzer
from app.analytics.outliers import OutlierAnalyzer
from app.analytics.quality import DataQualityAnalyzer
from app.analytics.statistics import StatisticsAnalyzer
from app.analytics.visualization import VisualizationAnalyzer
from app.data.loader import DataLoader
from app.data.profiler import DataProfiler
from app.data.validator import FileValidator
from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from app.schemas.query_schema import QueryRequest
from app.services.query_service import QueryService
from app.services.storage_service import StorageService


class DatasetService:

    @staticmethod
    async def upload_dataset(
        file: UploadFile,
        db: Session,
    ):
        await FileValidator.validate(file)

        saved_file = await StorageService.save_file(file)
        df = DataLoader.load(saved_file["file_path"])

        metadata = DataProfiler.profile(df)
        statistics = StatisticsAnalyzer.analyze(df)
        quality = DataQualityAnalyzer.analyze(df)
        outliers = OutlierAnalyzer.analyze(df)
        correlation = CorrelationAnalyzer.analyze(df)

        insights = InsightGenerator.generate(
            metadata,
            statistics,
            quality,
            outliers,
        )

        recommendations = RecommendationEngine.generate(
            metadata,
            quality,
            outliers,
        )

        visualizations = VisualizationAnalyzer.generate(df)

        file_ext = (file.filename or "").split(".")[-1].lower()

        dataset = Dataset(
            filename=saved_file["original_filename"],
            stored_filename=saved_file["stored_filename"],
            file_type=file_ext,
            file_size=saved_file["file_size"],
            rows=metadata.rows,
            columns=metadata.columns,
        )

        dataset = DatasetRepository.create(db, dataset)

        return {
            "message": "Dataset uploaded successfully.",
            "dataset": {
                "id": str(dataset.id),
                "filename": dataset.filename,
                "rows": dataset.rows,
                "columns": dataset.columns,
                "status": dataset.status,
            },
            "profile": metadata.model_dump(),
            "statistics": statistics,
            "quality": quality,
            "outliers": outliers,
            "visualizations": visualizations,
            "ai_insight": insights,
            "recommendations": recommendations,
            "correlation": correlation,
        }

    @staticmethod
    def get_all_datasets(db: Session):
        return DatasetRepository.get_all(db)

    @staticmethod
    def query_dataset(request: QueryRequest, db: Session):
        dataset = DatasetRepository.get_by_id(db, request.dataset_id)
        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )

        file_path = StorageService.UPLOAD_DIR / dataset.stored_filename
        df = DataLoader.load(str(file_path))

        return QueryService.answer(request.question, df)

    @staticmethod
    def get_dataset(dataset_id: UUID, db: Session):
        dataset = DatasetRepository.get_by_id(db, dataset_id)
        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )
        return dataset
