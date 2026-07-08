from pathlib import Path

import pandas as pd


class DataLoader:

    @staticmethod
    def load(file_path: str) -> pd.DataFrame:

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".csv":
            return pd.read_csv(path)

        elif suffix in [".xlsx", ".xls"]:
            return pd.read_excel(path)

        raise ValueError(f"Unsupported file type: {suffix}")