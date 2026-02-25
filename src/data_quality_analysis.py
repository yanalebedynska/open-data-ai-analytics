from __future__ import annotations

from pathlib import Path
import argparse
import json
import pandas as pd

RAW_PATH = Path("data/raw/dtp_2015.csv")
REPORTS_DIR = Path("reports")


def quality_report(df: pd.DataFrame) -> dict:
    report = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values_total": int(df.isna().sum().sum()),
        "missing_by_column": df.isna().sum().sort_values(ascending=False).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Data quality analysis")
    parser.add_argument("--input", type=str, default=str(RAW_PATH), help="Path to CSV file")
    parser.add_argument("--out", type=str, default="reports/quality_report.json", help="Output report path")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    rep = quality_report(df)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Quality report saved to: {out_path}")
    print(f"Rows: {rep['rows']}, Columns: {rep['columns']}, Duplicates: {rep['duplicate_rows']}")


if __name__ == "__main__":
    main()