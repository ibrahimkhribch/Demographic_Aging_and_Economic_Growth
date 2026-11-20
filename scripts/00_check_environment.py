"""Sanity-check the local Python setup; does not download or synthesize data."""
from pathlib import Path
import sys
import pandas
import numpy
import matplotlib
import statsmodels

root = Path(__file__).resolve().parents[1]
print(f"Python: {sys.version.split()[0]}")
print(f"pandas: {pandas.__version__}")
print(f"numpy: {numpy.__version__}")
print(f"matplotlib: {matplotlib.__version__}")
print(f"statsmodels: {statsmodels.__version__}")
print(f"Project root: {root}")
for folder in ("data/raw", "data/interim", "data/processed", "results/figures", "results/tables"):
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Ready: {path.relative_to(root)}")
print("Environment OK. Next: consult data/README.md for required source files.")
