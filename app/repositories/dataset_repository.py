from sqlalchemy.orm import Session

from app.models.dataset import Dataset

from uuid import UUID
from pydantic import BaseModel
class DatasetRepository:

    @staticmethod
    def create(db: Session, dataset: Dataset):
        db.add(dataset)
        db.commit()
        db.refresh(dataset)
        return dataset
    
    @staticmethod
    def get_all(db:Session):
        return db.query(Dataset).order_by(
            Dataset.uploaded_at.desc()
        ).all()
        
    @staticmethod
    def get_by_id(db:Session, dataset_id:UUID):
        
        return(
            db.query(Dataset)
            .filter(Dataset.id == dataset_id)
            .first()
        )
        