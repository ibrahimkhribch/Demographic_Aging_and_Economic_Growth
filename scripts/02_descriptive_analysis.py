"""Make simple descriptive figures using a real prebuilt panel (no estimates)."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data" / "processed" / "panel_annual.csv"
FIGURES = ROOT / "results" / "figures"
TABLES = ROOT / "results" / "tables"

def main() -> None:
    if not PANEL.exists():
        raise FileNotFoundError("First run: python scripts/01_build_panel.py")
    df = pd.read_csv(PANEL)
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    coverage = df.groupby("iso3").agg(first_year=("year", "min"), last_year=("year", "max"),
                                      observations=("year", "size"),
                                      gdp_nonmissing=("real_gdp_per_capita", "count"),
                                      aging_nonmissing=("share_60_plus", "count"))
    coverage.to_csv(TABLES / "country_coverage.csv")
    means = df.groupby("year", as_index=False).agg(
        mean_share_60_plus=("share_60_plus", "mean"),
        countries=("share_60_plus", "count"))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(means["year"], means["mean_share_60_plus"] * 100)
    ax.set(xlabel="Year", ylabel="Mean share aged 60+ (%)",
           title="Unweighted mean among available country observations")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIGURES / "mean_aging_share.png", dpi=180)
    plt.close(fig)
    print(f"Created {TABLES / 'country_coverage.csv'}")
    print(f"Created {FIGURES / 'mean_aging_share.png'}")
    print("Note: country composition may vary across years; inspect coverage before interpreting the trend.")

if __name__ == "__main__":
    main()
