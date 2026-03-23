import os
import json
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text


DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "accidents_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
TABLE_NAME = os.getenv("TABLE_NAME", "dtp_data")
CSV_PATH = Path(os.getenv("CSV_PATH", "/app/data/dtp_2015.csv"))
REPORT_PATH = Path("/app/reports/load_report.json")


def get_db_url() -> str:
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def wait_for_db(engine, retries: int = 30, delay: int = 2) -> None:
    for attempt in range(1, retries + 1):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database is ready.")
            return
        except Exception as e:
            print(f"[{attempt}/{retries}] Waiting for DB... {e}")
            time.sleep(delay)
    raise RuntimeError("Database is not available.")


def main() -> None:
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

    df = pd.read_csv(
        CSV_PATH,
        sep=None,
        engine="python",
        encoding="utf-8-sig",
        on_bad_lines="skip"
    )

    engine = create_engine(get_db_url())
    wait_for_db(engine)

    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False, method="multi", chunksize=1000)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "status": "success",
        "csv_path": str(CSV_PATH),
        "table_name": TABLE_NAME,
        "rows_loaded": int(df.shape[0]),
        "columns_loaded": int(df.shape[1]),
        "column_names": list(df.columns),
    }

    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()