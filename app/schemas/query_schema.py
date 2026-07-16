from pydantic import BaseModel
from uuid import UUID

class QueryRequest(BaseModel):
    dataset_id: UUID
    question:str
    
    
class QueryResponse(BaseModel):
    answer:str