import pandas as pd
from pathlib import Path

# Location of our raw data
DATA_DIR = Path("data/raw")

# Find all CSV files
csv_files = sorted(DATA_DIR.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    df = pd.read_csv(file)

    print("=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    # --------------------------------------------------
    # BASIC INFORMATION
    # --------------------------------------------------

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    # --------------------------------------------------
    # COLUMN INFORMATION
    # --------------------------------------------------

    print("\nColumns:")
    for column in df.columns:
        print(f"  - {column}")

    # --------------------------------------------------
    # MISSING VALUES
    # --------------------------------------------------

    print("\nMissing values:")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("  None")
    else:
        for column, count in missing.items():
            percentage = (count / len(df)) * 100
            print(f"  - {column}: {count:,} ({percentage:.2f}%)")

    # --------------------------------------------------
    # DUPLICATE ROWS
    # --------------------------------------------------

    print("\nDuplicate rows:")
    duplicate_rows = df.duplicated().sum()
    print(f"  {duplicate_rows:,}")

    # --------------------------------------------------
    # UNIQUE VALUES
    # --------------------------------------------------

    print("\nUnique values per column:")

    for column in df.columns:
        unique_count = df[column].nunique()
        print(f"  - {column}: {unique_count:,}")

    # --------------------------------------------------
    # SAMPLE DATA
    # --------------------------------------------------

    print("\nSample rows:")
    print(df.head(3).to_string(index=False))

    print()