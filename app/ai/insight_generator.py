class InsightGenerator:

    @staticmethod
    def generate(profile, statistics, quality, outliers):

        insights = []

        # Duplicate rows
        if profile.duplicate_rows > 0:
            insights.append(
                f"The dataset contains {profile.duplicate_rows} duplicate rows."
            )
        else:
            insights.append(
                "No duplicate rows were detected."
            )

        # Missing values
        total_missing = sum(profile.missing_values.values())

        if total_missing > 0:
            insights.append(
                f"The dataset contains {total_missing} missing values."
            )
        else:
            insights.append(
                "No missing values were detected."
            )

        # Statistics
        for column, values in statistics.items():

            insights.append(
                f"The average value of '{column}' is {round(values['mean'],2)}."
            )

        # Outliers
        for column, values in outliers.items():

            if values["outlier_count"] > 0:

                insights.append(
                    f"Column '{column}' contains {values['outlier_count']} potential outliers."
                )

        return insights