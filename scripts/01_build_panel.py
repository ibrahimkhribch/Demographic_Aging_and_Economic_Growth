"""Build an annual country panel from documented local CSV inputs.

See data/README.md. Uses no synthetic data and no inferred region assignments.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed" / "panel_annual.csv"
KEYS = ["iso3", "year"]
POP = ["pop_total", "pop_age_60_plus", "pop_age_50_plus", "pop_age_20_49"]
MACRO = ["real_gdp_per_capita", "employment_to_population_ratio", "real_output_per_worker"]

def read_dataset(file: Path, required: list[str], optional: list[str] | None = None) -> pd.DataFrame:
    if not file.exists():
        raise FileNotFoundError(f"Missing {file}. Follow data/README.md and download the real source data.")
    df = pd.read_csv(file, dtype={"iso3": "string"})
    missing = set(KEYS + required) - set(df.columns)
    if missing:
        raise ValueError(f"{file.name}: required columns missing: {sorted(missing)}")
    for col in optional or []:
        if col not in df:
            df[col] = np.nan
    df["iso3"] = df["iso3"].str.strip().str.upper()
    if df["iso3"].isna().any() or not df["iso3"].str.fullmatch(r"[A-Z]{3}").all():
        raise ValueError(f"{file.name}: invalid or missing ISO3 code.")
    df["year"] = pd.to_numeric(df["year"], errors="raise")
    if df["year"].isna().any() or (df["year"] % 1 != 0).any():
        raise ValueError(f"{file.name}: year must be a whole number.")
    df["year"] = df["year"].astype(int)
    if df.duplicated(KEYS).any():
        raise ValueError(f"{file.name}: duplicate (iso3, year) rows.")
    return df

def main() -> None:
    pop = read_dataset(RAW / "population_annual.csv", POP)
    macro = read_dataset(RAW / "macro_annual.csv", ["real_gdp_per_capita"], MACRO[1:])
    for col in POP:
        pop[col] = pd.to_numeric(pop[col], errors="raise")
    for col in MACRO:
        macro[col] = pd.to_numeric(macro[col], errors="raise")
    if (pop["pop_total"].dropna() <= 0).any() or (pop[POP[1:]].dropna() < 0).any().any():
        raise ValueError("Population totals must be positive; age-group populations cannot be negative.")
    if (macro["real_gdp_per_capita"].dropna() <= 0).any():
        raise ValueError("Real GDP per capita must be positive where observed.")
    if ((macro["employment_to_population_ratio"].dropna() < 0) | (macro["employment_to_population_ratio"].dropna() > 1)).any():
        raise ValueError("Employment-to-population ratio must be a fraction between 0 and 1.")
    if (pop["pop_age_60_plus"] > pop["pop_total"]).any() or (pop["pop_age_50_plus"] > pop["pop_total"]).any():
        raise ValueError("Age-group populations cannot exceed total population.")
    panel = pop.merge(macro, on=KEYS, how="inner", validate="one_to_one")
    if panel.empty:
        raise ValueError("No common country-year records. Check ISO3 codes and calendar years.")
    panel["share_60_plus"] = panel["pop_age_60_plus"] / panel["pop_total"]
    panel["aging_ratio_50_to_20_49"] = panel["pop_age_50_plus"] / panel["pop_age_20_49"].replace(0, np.nan)
    panel["log_gdp_pc"] = np.log(panel["real_gdp_per_capita"])
    panel = panel.sort_values(KEYS).reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    panel.to_csv(OUT, index=False)
    print(f"Saved {len(panel):,} rows from {panel.iso3.nunique()} countries to {OUT}")
    print(f"Year range: {panel.year.min()}–{panel.year.max()}")
    print("Missingness (%):")
    print((panel.isna().mean() * 100).round(1).to_string())

if __name__ == "__main__":
    main()
