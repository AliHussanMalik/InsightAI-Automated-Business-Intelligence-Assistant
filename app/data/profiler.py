import pandas as pd


class DataProfiler:

    @staticmethod
    def profile(df: pd.DataFrame) -> dict:
        return {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "duplicate_rows": int(df.duplicated().sum())
        }