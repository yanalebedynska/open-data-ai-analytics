import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine


DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "accidents_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
TABLE_NAME = os.getenv("TABLE_NAME", "dtp_data")

PLOTS_DIR = Path("/app/plots")


def get_db_url() -> str:
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def main() -> None:
    engine = create_engine(get_db_url())
    df = pd.read_sql_table(TABLE_NAME, con=engine)

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    first_col = df.columns[0]
    top10 = df[first_col].astype(str).value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top10.plot(kind="bar")
    plt.title(f"Top-10 values in column: {first_col}")
    plt.xlabel(first_col)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "top10_first_column.png", dpi=150)
    plt.close()

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if numeric_cols:
        col = numeric_cols[0]
        plt.figure(figsize=(10, 6))
        df[col].dropna().plot(kind="hist", bins=20)
        plt.title(f"Histogram of numeric column: {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(PLOTS_DIR / "hist_first_numeric.png", dpi=150)
        plt.close()
    else:
        second_col = df.columns[1] if len(df.columns) > 1 else df.columns[0]
        top10_second = df[second_col].astype(str).value_counts().head(10)

        plt.figure(figsize=(10, 6))
        top10_second.plot(kind="bar")
        plt.title(f"Top-10 values in column: {second_col}")
        plt.xlabel(second_col)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(PLOTS_DIR / "top10_second_column.png", dpi=150)
        plt.close()

    print("Plots created successfully.")


if __name__ == "__main__":
    main()