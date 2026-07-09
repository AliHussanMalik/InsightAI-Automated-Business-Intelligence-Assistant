import os

import matplotlib.pyplot as plt
import pandas as pd


class VisualizationAnalyzer:

    OUTPUT_DIR = "reports/figures"

    @classmethod
    def generate(cls, df: pd.DataFrame):

        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        generated_files = []

        numeric_columns = df.select_dtypes(include="number")

        for column in numeric_columns.columns:

            plt.figure(figsize=(8, 5))

            df[column].hist(bins=20)

            plt.title(f"{column} Distribution")

            plt.xlabel(column)

            plt.ylabel("Frequency")

            filename = f"{column}_histogram.png"

            path = os.path.join(cls.OUTPUT_DIR, filename)

            plt.savefig(path)

            plt.close()

            generated_files.append(path)

        return generated_files