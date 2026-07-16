from fastapi import APIRouter, UploadFile, File , Depends

from sqlalchemy.orm import Session
from app.api.dependencies.database import get_db

from app.services.dataset_service import DatasetService

from app.schemas.query_schema import QueryRequest

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"] 
)


@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    db:Session = Depends(get_db),
):
    return await DatasetService.upload_dataset(file,db)

@router.get("/")
def get_all_datasets(
    db:Session = Depends(get_db),
):
    return DatasetService.get_all_datasets(db)


@router.post("/query")
def query_request(
    request: QueryRequest,
    db: Session = Depends(get_db),
):
    return DatasetService.query_dataset(request, db)