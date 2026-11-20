# Demographic Aging and Economic Growth

**An empirical comparison of the Maestas–Mullen–Powell and Acemoglu–Restrepo perspectives across European and African economies.**

> **Status:** Research design and data collection. No empirical results are claimed yet.

## Research question

How does population aging relate to economic growth, and does the relationship vary with automation and productivity responses? Can the mechanisms discussed by Maestas, Mullen & Powell (2023) and Acemoglu & Restrepo (2017) help explain differences between European and African economies?

The papers are complementary, not interchangeable: Maestas et al. use predetermined aging variation across **US states** to estimate effects on GDP per capita, employment and productivity; Acemoglu & Restrepo study **cross-country** aging–growth patterns and the potential automation response. Transferring causal claims from either design to a new sample requires separate identification work.

## Papers

- **Maestas, Mullen & Powell (2023)**, *The Effect of Population Aging on Economic Growth, the Labor Force, and Productivity*. [NBER working-paper PDF](https://www.nber.org/system/files/working_papers/w22452/w22452.pdf) · [Journal DOI](https://doi.org/10.1257/mac.20190196).
- **Acemoglu & Restrepo (2017)**, *Secular Stagnation? The Effect of Aging on Economic Growth in the Age of Automation*. [NBER working-paper PDF](https://www.nber.org/system/files/working_papers/w23077/w23077.pdf) · [Journal DOI](https://doi.org/10.1257/aer.p20171101).

See [papers/README.md](papers/README.md) for detailed reading notes.

## Planned empirical work

| Track | Question | Planned first-pass approach |
| --- | --- | --- |
| A — Demography & growth | Is greater aging associated with slower GDP-per-capita growth? | Country panel; 5- or 10-year differences, country/period effects and controls |
| B — Mechanisms | How much of the association operates through employment versus productivity? | Growth-accounting identity and separate outcome regressions |
| C — Automation | Does automation intensity moderate the aging–growth relationship? | Interaction regressions on the subset with reliable automation data |
| D — Heterogeneity | Are patterns different across Europe and Africa? | Region interactions, sample splits, common-support checks |

All baseline estimates are **associational** until an appropriate identification strategy is justified. The Maestas et al. identification method cannot simply be transplanted to countries.

## Data plan

Potential sources: [UN World Population Prospects](https://population.un.org/wpp/), [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators), [Penn World Table](https://www.rug.nl/ggdc/productivity/pwt/), [ILOSTAT](https://ilostat.ilo.org/data/), and [IFR](https://ifr.org/worldrobotics/) for restricted robot adoption coverage. No datasets are downloaded into this repository yet.

Start with a transparent Europe/Africa sample based on observable population and GDP coverage. Do not restrict the main panel to countries covered by IFR: robot data can be used for a separate, smaller automation extension.

**Important:** The aging measures differ across the papers (Maestas: share aged 60+; Acemoglu–Restrepo: ratio aged 50+ to ages 20–49). Construct and label both separately, and test alternative definitions.

## Repository layout

```text
.
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/                  # original downloaded datasets (not versioned)
│   ├── interim/              # cleaned source-by-source data
│   ├── processed/            # analysis-ready panels
│   └── README.md             # sources and construction instructions
├── docs/
│   ├── research_design.md
│   ├── data_dictionary.md
│   └── workplan.md
├── papers/
│   └── README.md
├── scripts/
│   ├── 00_check_environment.py
│   ├── 01_build_panel.py
│   └── 02_descriptive_analysis.py
├── results/
│   ├── figures/
│   └── tables/
└── notebooks/
```

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/ibrahimkhribch/Demographic_Aging_and_Economic_Growth.git
cd Demographic_Aging_and_Economic_Growth
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python scripts/00_check_environment.py
```

To produce a starter panel, place source files matching [the input schemas](data/README.md) into `data/raw/`, then run:

```bash
python scripts/01_build_panel.py
python scripts/02_descriptive_analysis.py
```

These scripts deliberately **do not fabricate data**. They fail with informative messages if required datasets are missing.

## Roadmap

The [first-week workplan](docs/workplan.md) starts with the literature, variables, country coverage and a minimal descriptive panel before estimation. See [research design](docs/research_design.md) for the estimands, econometric cautions and tentative models.

## Research practices

- Keep raw inputs unchanged; record source URL, vintage, units, extraction filters and license in `data/README.md`.
- Use ISO3 country codes and annual reference years; distinguish flow variables from stocks.
- Document coverage and missingness before dropping countries.
- Do not commit restricted IFR datasets or other licensed microdata.
- Commit code, documentation, source manifests and small reproducible outputs. Dataset files in `data/raw/`, `data/interim/` and `data/processed/` are ignored by default.

## Citation

Cite the two original papers and the underlying statistical providers when reporting results. This repository is an independent project and **not** an official replication package of either paper.
