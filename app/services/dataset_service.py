from app.data.profiler import DataProfiler
from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from fastapi import UploadFile
import seaborn as sns
from app.analytics.statistics import StatisticsAnalyzer
from app.data.validator import FileValidator
from app.services.storage_service import StorageService
from app.data.loader import DataLoader
from sqlalchemy.orm import Session
from app.analytics.quality import DataQualityAnalyzer
from app.analytics.outliers import OutlierAnalyzer
from app.analytics.visualization import VisualizationAnalyzer
from fastapi import HTTPException
from uuid import UUID
from app.ai.insight_generator import InsightGenerator
from app.ai.recommendation_engine import RecommendationEngine
from app.analytics.correlation import CorrelationAnalyzer
import matplotlib.pyplot as plt
import os

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
        
        analysis = {
            "profile": metadata.model_dump(),
            "statistics":statistics,
            "quality":quality,
            "outliers":outliers,
        }
        
        
        visualizations = VisualizationAnalyzer.generate(df)
        
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
    def get_all_datasets(db:Session):
        return DatasetRepository.get_all(db)
    
    
    @staticmethod
    def get_dataset(dataset_id: UUID, db:Session):
        
        dataset = DatasetRepository.get_by_id(db,dataset_id)
        
        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )
            
        return dataset
    
    
    
        
