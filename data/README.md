# Data sources, files and conventions

**No actual data are bundled.** Download sources yourself and keep originals under `data/raw/`; the folder is excluded from git. Record the version and download date before transforming.

| Source | URL | Candidate content | Coverage/limitations |
|---|---|---|---|
| UN World Population Prospects | https://population.un.org/wpp/ | Age-specific country population | Annual, both sexes preferred; record population revision |
| World Bank WDI | https://databank.worldbank.org/source/world-development-indicators | GDP, real GDP per capita, employment | Missingness varies by country and year |
| Penn World Table | https://www.rug.nl/ggdc/productivity/pwt/ | Real output, employment/hours, productivity | Choose version, PPP concept and units explicitly |
| ILOSTAT | https://ilostat.ilo.org/data/ | Employment-to-population and labor indicators | Definitions and modeled series vary |
| IFR World Robotics | https://ifr.org/worldrobotics/ | Industrial robots/robot exposure | Restricted access and weak coverage in many African countries |

## Starter input contract

Supply **two CSV files** with a unique row for each `iso3,year` pair. ISO3 must be three-letter country codes, year four-digit. Use the same published country coding across both files; harmonize any special territories before merging.

1. `data/raw/population_annual.csv`

Columns:
```csv
iso3,year,pop_total,pop_age_60_plus,pop_age_50_plus,pop_age_20_49
```
Population columns must all use the **same unit** (persons, thousands or millions). `pop_total` must be positive; subgroups nonnegative. Do not include regional totals.

2. `data/raw/macro_annual.csv`

Columns:
```csv
iso3,year,real_gdp_per_capita,employment_to_population_ratio,real_output_per_worker
```
`real_gdp_per_capita` must be positive, consistently defined across countries and years; a real constant-price or PPP-adjusted series is preferable. The other columns are optional: if unavailable, create the headers with missing values. `employment_to_population_ratio` should be a **fraction** between 0 and 1 (not 0–100). `real_output_per_worker` is optional, positive when available.

## Outputs and definitions

`scripts/01_build_panel.py` writes `data/processed/panel_annual.csv` using an inner join on `iso3,year` and computes:
- `share_60_plus = pop_age_60_plus / pop_total`
- `aging_ratio_50_to_20_49 = pop_age_50_plus / pop_age_20_49`
- `log_gdp_pc = log(real_gdp_per_capita)`

The analysis sample must be defined later using explicit country lists and coverage checks. No region is assigned by guesswork. Do not silently fill missing population or GDP data.

## Provenance checklist

For every file, record its original URL, access/download date, table identifier, vintage/revision, variable series codes, country coverage, time coverage, transformations, license and known issues in this README or a source-specific manifest.
