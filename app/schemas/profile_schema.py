from pydantic import BaseModel


class ProfileResponse(BaseModel):

    rows: int
    columns: int

    duplicate_rows: int

    missing_values: dict[str, int]

    memory_usage_mb: float

    numeric_columns: int

    categorical_columns: int

    column_names: list[str]

    recommendations: list[str]