class NLQEngine:

    @staticmethod
    def classify(question: str):

        question = question.lower()

        if "average" in question or "mean" in question:
            return "average"

        if "duplicate" in question:
            return "duplicates"

        if "missing" in question:
            return "missing"

        if "column" in question:
            return "columns"

        if "row" in question:
            return "rows"

        return "unknown"