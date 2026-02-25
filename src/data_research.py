from __future__ import annotations

from pathlib import Path
import argparse
import json
import pandas as pd

RAW_PATH = Path("data/raw/dtp_2015.csv")


def research(df: pd.DataFrame) -> dict:
    result: dict = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "columns_list": list(df.columns),
        "numeric_summary": {},
        "top_values": {}
    }

    num_df = df.select_dtypes(include=["number"])
    if not num_df.empty:
        result["numeric_summary"] = num_df.describe().to_dict()

    first_col = df.columns[0]
    top = df[first_col].astype(str).value_counts().head(10).to_dict()
    result["top_values"] = {"column": first_col, "top10": top}

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Data research / EDA summary")
    parser.add_argument("--input", type=str, default=str(RAW_PATH), help="Path to CSV file")
    parser.add_argument("--out", type=str, default="reports/research_summary.json", help="Output summary path")
    args = parser.parse_args()

    df = pd.read_csv(args.input, sep=None, engine="python", encoding="utf-8-sig", on_bad_lines="warn")
    summary = research(df)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Research summary saved to: {out_path}")
    print(f"Rows: {summary['rows']}, Columns: {summary['columns']}")


if __name__ == "__main__":
    main()