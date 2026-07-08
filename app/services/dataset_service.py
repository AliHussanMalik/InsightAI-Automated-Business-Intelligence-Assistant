from app.data.profiler import DataProfiler
from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from fastapi import UploadFile

from app.data.validator import FileValidator
from app.services.storage_service import StorageService
from app.data.loader import DataLoader
from sqlalchemy.orm import Session

class DatasetService:

    @staticmethod
    async def upload_dataset(
        file: UploadFile,
        db:Session,
        ):

        await FileValidator.validate(file)
        
        saved_file = await StorageService.save_file(file)
        df = DataLoader.load(saved_file["file_path"])
        
        # metadata ={
        #     "rows": len(df),
        #     "columns": len(df.columns),
        #     "column_names": list(df.columns)
        # }
        metadata = DataProfiler.profile(df)
        
        dataset = Dataset(
            filename=saved_file["original_filename"],
            stored_filename=saved_file["stored_filename"],
            file_type=file.filename.split(".")[-1].lower(),
            file_size=saved_file["file_size"],
            rows=metadata.rows,
            columns=metadata.columns,
        )
        
        dataset = DatasetRepository.create(db, dataset)

        # return {
        #     "message": "Validation successful.",
        #     **saved_file,
        #     **metadata
        # }
        
        return {
    "id": str(dataset.id),
    "message": "Dataset uploaded successfully.",
    "filename": dataset.filename,
    "rows": dataset.rows,
    "columns": dataset.columns,
    "status": dataset.status,
}