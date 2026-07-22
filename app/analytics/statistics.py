import pandas as pd


class StatisticsAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame) -> dict:
        numeric_columns = df.select_dtypes(include="number")
        statistics = {}

        for column in numeric_columns.columns:
            series = df[column].dropna()
            if series.empty:
                continue

            modes = series.mode()
            mode_val = float(modes.iloc[0]) if not modes.empty else None

            statistics[column] = {
                "mean": float(series.mean()),
                "median": float(series.median()),
                "mode": mode_val,
                "min": float(series.min()),
                "max": float(series.max()),
                "std": float(series.std()),
                "variance": float(series.var()),
                "q1": float(series.quantile(0.25)),
                "q2": float(series.quantile(0.50)),
                "q3": float(series.quantile(0.75)),
            }

        return statistics