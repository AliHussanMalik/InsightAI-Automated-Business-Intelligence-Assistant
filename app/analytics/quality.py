import pandas as pd


class DataQualityAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        rows = len(df)
        columns = len(df.columns)

        # Missing values
        missing = df.isnull().sum().to_dict()

        # Missing percentage
        missing_percentage = (
            (df.isnull().sum() / rows) * 100
        ).round(2).to_dict()

        # Duplicate rows
        duplicate_rows = int(df.duplicated().sum())

        # Constant columns
        constant_columns = [
            col for col in df.columns
            if df[col].nunique(dropna=False) == 1
        ]

        # High-cardinality columns
        high_cardinality = [
            col for col in df.columns
            if df[col].nunique() > rows * 0.9
        ]

        # Empty columns
        empty_columns = [
            col for col in df.columns
            if df[col].isnull().all()
        ]

        return {
            "rows": rows,
            "columns": columns,
            "duplicate_rows": duplicate_rows,
            "missing_values": missing,
            "missing_percentage": missing_percentage,
            "constant_columns": constant_columns,
            "high_cardinality_columns": high_cardinality,
            "empty_columns": empty_columns,
        }