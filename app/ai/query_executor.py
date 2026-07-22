import pandas as pd


class QueryExecutor:

    @staticmethod
    def execute(intent: str, df: pd.DataFrame):

        if intent == "rows":
            return len(df)

        if intent == "columns":
            return list(df.columns)

        return None
