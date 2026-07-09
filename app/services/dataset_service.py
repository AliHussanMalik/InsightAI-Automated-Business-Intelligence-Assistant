from app.data.profiler import DataProfiler
from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from fastapi import UploadFile
from app.analytics.statistics import StatisticsAnalyzer
from app.data.validator import FileValidator
from app.services.storage_service import StorageService
from app.data.loader import DataLoader
from sqlalchemy.orm import Session
from app.analytics.quality import DataQualityAnalyzer
from app.analytics.outliers import OutlierAnalyzer
from app.analytics.visualization import VisualizationAnalyzer

class DatasetService:

    @staticmethod
    async def upload_dataset(
        file: UploadFile,
        db:Session,
        ):

        await FileValidator.validate(file)
        
        saved_file = await StorageService.save_file(file)
        df = DataLoader.load(saved_file["file_path"])
        
        metadata = DataProfiler.profile(df)
        
        statistics = StatisticsAnalyzer.analyze(df)
        # print(statistics)
        
        quality = DataQualityAnalyzer.analyze(df)
        # print(quality)
        
        outliers = OutlierAnalyzer.analyze(df)
        # print(outliers)
        
        visualizations = VisualizationAnalyzer.generate(df)
        print(visualizations)
        
        
        analysis = {
            "profile": metadata.model_dump(),
            "statistics":statistics,
            "quality":quality,
            "outliers":outliers,
        }
        
        
        dataset = Dataset(
            filename=saved_file["original_filename"],
            stored_filename=saved_file["stored_filename"],
            file_type=file.filename.split(".")[-1].lower(),
            file_size=saved_file["file_size"],
            rows=metadata.rows,
            columns=metadata.columns,
        )
        
        dataset = DatasetRepository.create(db, dataset)
        
        return {
    "id": str(dataset.id),
    "message": "Dataset uploaded successfully.",
    "filename": dataset.filename,
    "rows": dataset.rows,
    "columns": dataset.columns,
    "status": dataset.status,
}