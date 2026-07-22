import re

import pandas as pd

from app.schemas.query_schema import QueryResponse


class QueryService:

    @staticmethod
    def answer(question: str, df: pd.DataFrame) -> QueryResponse:

        question = question.lower().strip()

        numeric_columns = list(df.select_dtypes(include="number").columns)

        if "column names" in question or "columns names" in question:
            return QueryResponse(
                answer=", ".join(df.columns)
            )

        if "dataset size" in question:
            return QueryResponse(
                answer=f"The dataset contains {len(df)} rows and {len(df.columns)} columns."
            )

        if "rows" in question:
            return QueryResponse(
                answer=f"The dataset contains {len(df)} rows."
            )

        if "columns" in question:
            return QueryResponse(
                answer=f"The dataset contains {len(df.columns)} columns."
            )

        if "missing" in question:
            missing = df.isnull().sum()
            text = [f"{col}: {count}" for col, count in missing.items() if count > 0]
            if not text:
                return QueryResponse(answer="The dataset has no missing values.")
            return QueryResponse(
                answer="Missing values -> " + ", ".join(text)
            )

        for column in numeric_columns:
            name = column.lower()
            pattern = r"\b" + re.escape(name) + r"\b"

            if re.search(pattern, question):

                if "average" in question or "mean" in question:
                    return QueryResponse(
                        answer=f"The average {column} is {df[column].mean():.2f}."
                    )

                if "maximum" in question or "max" in question:
                    return QueryResponse(
                        answer=f"The maximum {column} is {df[column].max()}."
                    )

                if "minimum" in question or "min" in question:
                    return QueryResponse(
                        answer=f"The minimum {column} is {df[column].min()}."
                    )

                if "median" in question:
                    return QueryResponse(
                        answer=f"The median {column} is {df[column].median()}."
                    )

                if "sum" in question or "total" in question:
                    return QueryResponse(
                        answer=f"The total {column} is {df[column].sum():.2f}."
                    )

                if "standard deviation" in question or "std" in question:
                    return QueryResponse(
                        answer=f"The standard deviation of {column} is {df[column].std():.2f}."
                    )

                if "count" in question:
                    return QueryResponse(
                        answer=f"There are {df[column].count()} values in {column}."
                    )

        for col in df.columns:
            col_lower = col.lower()
            pattern = r"\b" + re.escape(col_lower) + r"\b"
            if re.search(pattern, question):
                if "unique" in question:
                    unique_count = df[col].nunique()
                    return QueryResponse(
                        answer=f"'{col}' has {unique_count} unique values."
                    )

                if "most common" in question or "mode" in question:
                    modes = df[col].mode()
                    val = modes.iloc[0] if not modes.empty else "N/A"
                    return QueryResponse(
                        answer=f"The most common value in '{col}' is '{val}'."
                    )

        return QueryResponse(
            answer="I don't understand that question yet."
        )
