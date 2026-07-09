import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  

class VisualizationAnalyzer:

    OUTPUT_DIR = "reports/figures"

    @classmethod
    def generate(cls, df: pd.DataFrame):

        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        visualizations = []

        numeric = df.select_dtypes(include="number")

        for column in numeric.columns:

            # Histogram
            plt.figure(figsize=(8, 5))
            df[column].hist(bins=20)
            plt.title(f"{column} Distribution")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            histogram = f"{column}_histogram.png"
            histogram_path = os.path.join(cls.OUTPUT_DIR, histogram)

            plt.savefig(histogram_path)
            plt.close()

            # Boxplot
            plt.figure(figsize=(8, 5))
            plt.boxplot(df[column].dropna())
            plt.title(f"{column} Boxplot")
            plt.ylabel(column)

            boxplot = f"{column}_boxplot.png"
            boxplot_path = os.path.join(cls.OUTPUT_DIR, boxplot)

            plt.savefig(boxplot_path)
            plt.close()
            
            correlation = df.select_dtypes(include="number").corr()
            
            plt.figure(figsize=(8,6))

            sns.heatmap(
                 correlation,
                annot=True,
                cmap="coolwarm"
                )

            heatmap = os.path.join(
                    cls.OUTPUT_DIR,
                    "correlation_heatmap.png"
                )

            plt.savefig(heatmap)

            plt.close()

        visualizations.append(
                {
                    "column": column,
                    "histogram": histogram_path,
                    "boxplot": boxplot_path,
                }
            )

        return visualizations