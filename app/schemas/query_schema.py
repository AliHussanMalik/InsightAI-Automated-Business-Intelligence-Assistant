from uuid import UUID

from pydantic import BaseModel


class QueryRequest(BaseModel):
    dataset_id: UUID
    question: str


class QueryResponse(BaseModel):
    answer: str