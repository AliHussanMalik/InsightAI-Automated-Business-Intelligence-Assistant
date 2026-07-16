class QueryExecutor:

    @staticmethod
    def execute(intent, df):

        if intent == "rows":
            return len(df)

        if intent == "columns":
            return list(df.columns)

        ...