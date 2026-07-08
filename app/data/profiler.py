import pandas as pd

from app.schemas.profile_schema import ProfileResponse


class DataProfiler:

    @staticmethod
    def profile(df: pd.DataFrame) -> ProfileResponse:
        
        rows = len(df)
        
        columns = len(df.columns)
        
        duplicates = int(df.duplicated().sum())
        
        missing = df.isnull().sum().to_dict()
        
        memory = round(
            df.memory_usage(deep=True).sum() /1024 /1024 , 2 ,
        )
        numeric = len(
            df.select_dtypes(include="number").columns
        )
        categorical = len(
            df.select_dtypes(exclude="number").columns
        )
        
        recommendations = []
        
        if duplicates:
            recommendations.append(
                "Dataset contains duplicate rows."
            )
            
        if any(v > 0 for v in missing.values()):
            recommendations.append(
                "Dataset contains missing values."
            )
        
        if not recommendations:
            recommendations.append(
                "Dataset quality looks good."
            )
        return ProfileResponse(
            rows = rows,
            columns = columns,
            duplicate_rows = duplicates,
            missing_values = missing,
            memory_usage_mb=memory,
            numeric_columns= numeric,
            categorical_columns=categorical,
            column_names = list(df.columns),
            recommendations= recommendations,
            
        )