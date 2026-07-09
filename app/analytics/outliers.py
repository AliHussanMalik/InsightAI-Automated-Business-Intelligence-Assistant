import pandas as pd


class OutlierAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        results = {}

        numeric_columns = df.select_dtypes(include="number")

        for column in numeric_columns.columns:

            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outliers = df[
                (df[column] < lower) |
                (df[column] > upper)
            ]

            results[column] = {
                "lower_bound": round(float(lower), 2),
                "upper_bound": round(float(upper), 2),
                "outlier_count": len(outliers),
                "outlier_percentage": round(
                    len(outliers) / len(df) * 100,
                    2
                ),
            }

        return results