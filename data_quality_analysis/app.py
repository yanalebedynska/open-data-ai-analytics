import os
import json
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "accidents_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
TABLE_NAME = os.getenv("TABLE_NAME", "dtp_data")

REPORT_PATH = Path("/app/reports/quality_report.json")


def get_db_url() -> str:
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def main() -> None:
    engine = create_engine(get_db_url())
    df = pd.read_sql_table(TABLE_NAME, con=engine)

    empty_string_by_column = {}
    for col in df.columns:
        empty_string_by_column[col] = int(df[col].astype(str).str.strip().eq("").sum())

    report = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values_total": int(df.isna().sum().sum()),
        "missing_by_column": {k: int(v) for k, v in df.isna().sum().to_dict().items()},
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "empty_string_by_column": empty_string_by_column,
    }

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()