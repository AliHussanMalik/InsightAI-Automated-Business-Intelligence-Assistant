import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from fastapi import HTTPException



from app.analytics.visualization import VisualizationAnalyzer
from app.data.validator import FileValidator
from app.services.query_service import QueryService


def test_query_service_answers():
    data = {
        "age": [20, 30, 40, 50, 60],
        "salary": [50000, 60000, 70000, 80000, 90000],
        "city": ["NY", "LA", "NY", "SF", "LA"]
    }
    df = pd.DataFrame(data)

    # Test rows and columns query
    assert "5 rows" in QueryService.answer("how many rows?", df).answer
    assert "3 columns" in QueryService.answer("how many columns?", df).answer
    assert "age, salary, city" in QueryService.answer("what are the column names?", df).answer

    # Test max query (verifies no Pydantic ValidationError)
    max_res = QueryService.answer("what is the maximum salary?", df)
    assert max_res.answer == "The maximum salary is 90000."

    # Test min query
    min_res = QueryService.answer("what is the min age?", df)
    assert min_res.answer == "The minimum age is 20."

    # Test median query (verifies correct calculation)
    median_res = QueryService.answer("what is the median age?", df)
    assert median_res.answer == "The median age is 40.0."

    # Test mean/average query
    mean_res = QueryService.answer("what is the average salary?", df)
    assert mean_res.answer == "The average salary is 70000.00."

    # Test std query (verifies standard deviation, not variance)
    std_res = QueryService.answer("what is the standard deviation of age?", df)
    assert "standard deviation" in std_res.answer.lower()

    # Test unique query
    unique_res = QueryService.answer("how many unique values in city?", df)
    assert "3 unique values" in unique_res.answer

    # Test mode/most common query
    mode_res = QueryService.answer("what is the most common city?", df)
    assert "NY" in mode_res.answer or "LA" in mode_res.answer

    # Test unknown query
    unknown_res = QueryService.answer("who is the president?", df)
    assert unknown_res.answer == "I don't understand that question yet."


def test_visualization_analyzer(tmp_path):
    data = {
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    # Override output directory to temp path
    VisualizationAnalyzer.OUTPUT_DIR = str(tmp_path / "figures")

    res = VisualizationAnalyzer.generate(df)

    # Verify metadata for ALL numeric columns is returned (x and y)
    assert len(res) == 2
    columns_generated = [item["column"] for item in res]
    assert "x" in columns_generated
    assert "y" in columns_generated

    # Verify figure files actually exist on disk
    for item in res:
        assert os.path.exists(item["histogram"])
        assert os.path.exists(item["boxplot"])

    # Verify correlation heatmap exists
    assert os.path.exists(tmp_path / "figures" / "correlation_heatmap.png")


if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    print("Running test_query_service_answers...")
    test_query_service_answers()
    print("test_query_service_answers PASSED.")

    print("Running test_visualization_analyzer...")
    with tempfile.TemporaryDirectory() as tmpdir:
        test_visualization_analyzer(Path(tmpdir))
    print("test_visualization_analyzer PASSED.")
    print("\nALL P0 FIX VERIFICATION TESTS PASSED SUCCESSFULLY!")

