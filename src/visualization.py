from __future__ import annotations

from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import pandas as pd

RAW_PATH = Path("data/raw/dtp_2015.csv")
FIG_DIR = Path("reports/figures")


def main() -> None:
    parser = argparse.ArgumentParser(description="Data visualization")
    parser.add_argument("--input", type=str, default=str(RAW_PATH), help="Path to CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.input, sep=None, engine="python", encoding="utf-8-sig", on_bad_lines="warn")

    FIG_DIR.mkdir(parents=True, exist_ok=True)


    col0 = df.columns[0]
    top10 = df[col0].astype(str).value_counts().head(10)

    plt.figure()
    top10.plot(kind="bar")
    plt.title(f"Top-10 values in column: {col0}")
    plt.xlabel(col0)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    out1 = FIG_DIR / "top10_first_column.png"
    plt.tight_layout()
    plt.savefig(out1, dpi=150)
    plt.close()


    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    out2 = None
    if num_cols:
        c = num_cols[0]
        plt.figure()
        df[c].dropna().plot(kind="hist", bins=20)
        plt.title(f"Histogram of numeric column: {c}")
        plt.xlabel(c)
        plt.ylabel("Frequency")
        out2 = FIG_DIR / "hist_first_numeric.png"
        plt.tight_layout()
        plt.savefig(out2, dpi=150)
        plt.close()

    print(f"Saved figure: {out1}")
    if out2:
        print(f"Saved figure: {out2}")
    else:
        print("No numeric columns found -> histogram was not created.")


if __name__ == "__main__":
    main()