from __future__ import annotations

from pathlib import Path
from typing import Optional
import argparse
import shutil

import pandas as pd

RAW_DIR = Path("data/raw")


def load_data(url: Optional[str] = None,
              local_file: Optional[str] = None,
              out_filename: str = "dtp_2015.csv") -> Path:

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / out_filename

    if local_file:
        src = Path(local_file)
        if not src.exists():
            raise FileNotFoundError(f"Local file not found: {src}")
        shutil.copyfile(src, out_path)
        return out_path

    if not url:
        raise ValueError("Provide --url (direct CSV link) or --local-file.")

    df = pd.read_csv(url)
    df.to_csv(out_path, index=False)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Load open dataset into data/raw/")
    parser.add_argument("--url", type=str, default=None, help="Direct CSV URL")
    parser.add_argument("--local-file", type=str, default=None, help="Path to local file (CSV)")
    parser.add_argument("--out", type=str, default="dtp_2015.csv", help="Output name in data/raw/")
    args = parser.parse_args()

    saved = load_data(url=args.url, local_file=args.local_file, out_filename=args.out)
    print(f"Saved dataset to: {saved}")


if __name__ == "__main__":
    main()