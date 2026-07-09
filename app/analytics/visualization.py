import os

import matplotlib.pyplot as plt
import pandas as pd


class VisualizationAnalyzer:

    OUTPUT_DIR = "reports/figures"

    @classmethod
    def generate_histograms(cls, df: pd.DataFrame)-> list[str]:

        # os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

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
    
    
    @classmethod
    def generate_boxplots(cls, df: pd.DataFrame)->list[str]:

        generated = []

        numeric = df.select_dtypes(include="number")

        for column in numeric.columns:

            plt.figure(figsize=(8,5))

            plt.boxplot(df[column].dropna())

            plt.title(f"{column} Boxplot")

            plt.ylabel(column)

            filename = f"{column}_boxplot.png"

            path = os.path.join(cls.OUTPUT_DIR, filename)

            plt.savefig(path)

            plt.close()

            generated.append(path)

        return generated
    
    
    @classmethod
    def generate(cls, df: pd.DataFrame)-> list[str]:

        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        generated_files = []

        generated_files.extend(cls.generate_histograms(df))
        generated_files.extend(cls.generate_boxplots(df))

        return generated_files