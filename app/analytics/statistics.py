# import pandas as pd


# class StatisticsAnalyzer:

#     @staticmethod
#     def analyze(df: pd.DataFrame):

#         statistics = {}

#         numeric_columns = df.select_dtypes(include="number")

#         for column in numeric_columns.columns:

#             statistics[column] = {
#                 "mean": float(numeric_columns[column].mean()),
#                 "median": float(numeric_columns[column].median()),
#                 "mode": float(numeric_columns[column].mode().iloc[0]),
#                 "min": float(numeric_columns[column].min()),
#                 "max": float(numeric_columns[column].max()),
#                 "std": float(numeric_columns[column].std()),
#                 "variance": float(numeric_columns[column].var()),
#                 "q1": float(numeric_columns[column].quantile(0.25)),
#                 "q2": float(numeric_columns[column].quantile(0.50)),
#                 "q3": float(numeric_columns[column].quantile(0.75)),
#             }

#         return statistics



import pandas as pd


class StatisticsAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        print("\n========== DATAFRAME INFO ==========")
        print(df.head())
        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        numeric_columns = df.select_dtypes(include="number")

        print("\nNumeric Columns:")
        print(numeric_columns.columns.tolist())

        statistics = {}

        for column in numeric_columns.columns:

            statistics[column] = {
                "mean": float(df[column].mean()),
                "median": float(df[column].median()),
                "mode": float(df[column].mode().iloc[0]),
                "min": float(df[column].min()),
                "max": float(df[column].max()),
                "std": float(df[column].std()),
                "variance": float(df[column].var()),
                "q1": float(df[column].quantile(0.25)),
                "q2": float(df[column].quantile(0.50)),
                "q3": float(df[column].quantile(0.75)),
            }

        print("\nStatistics:")
        print(statistics)

        return statistics