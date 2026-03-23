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

REPORT_PATH = Path("/app/reports/research_summary.json")


def get_db_url() -> str:
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def main() -> None:
    engine = create_engine(get_db_url())
    df = pd.read_sql_table(TABLE_NAME, con=engine)

    numeric_df = df.select_dtypes(include=["number"])
    numeric_summary = {}
    if not numeric_df.empty:
        numeric_summary = numeric_df.describe().round(2).to_dict()

    top_values = {}
    for col in df.columns[:3]:
        top_values[col] = {
            str(k): int(v)
            for k, v in df[col].astype(str).value_counts().head(10).to_dict().items()
        }

    summary = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "numeric_summary": numeric_summary,
        "top_values": top_values,
    }

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()