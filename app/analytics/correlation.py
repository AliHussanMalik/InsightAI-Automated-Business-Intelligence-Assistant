import pandas as pd


class CorrelationAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        numeric = df.select_dtypes(include="number")

        if numeric.shape[1] < 2:
            return {
                "matrix": {},
                "strong_correlations": []
            }

        correlation = numeric.corr().round(2)

        strong = []

        columns = correlation.columns

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                value = correlation.iloc[i, j]

                if abs(value) >= 0.70:

                    strong.append(
                        {
                            "column_1": columns[i],
                            "column_2": columns[j],
                            "correlation": float(value)
                        }
                    )

        return {
            "matrix": correlation.to_dict(),
            "strong_correlations": strong
        }