class RecommendationEngine:

    @staticmethod
    def generate(profile, quality, outliers):

        recommendations = []

        if profile.duplicate_rows > 0:
            recommendations.append(
                "Remove duplicate rows before analysis."
            )

        if any(v > 0 for v in profile.missing_values.values()):
            recommendations.append(
                "Handle missing values before training ML models."
            )

        for column, values in outliers.items():

            if values["outlier_count"] > 0:

                recommendations.append(
                    f"Investigate outliers in '{column}'."
                )

        if not recommendations:

            recommendations.append(
                "Dataset quality is excellent."
            )

        return recommendations