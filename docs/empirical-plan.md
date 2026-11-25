# Empirical work plan

## Phase 1 — Maestas, Mullen, and Powell

1. **Build the country-decade panel.** Start with 1990–2000, 2000–2010, and 2010–2020 as candidate windows. Combine [UN World Population Prospects 2024](https://population.un.org/wpp) historical population estimates by age with [World Development Indicators real GDP](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD) (constant 2015 US dollars). Use ISO3 codes and a documented Europe–Africa country list. Audit missing endpoints and historical boundary changes before locking the sample.
2. **Describe aging and estimate OLS.** Compare decade changes in log real GDP per adult aged 20+ and log(60+ population / 20+ population). Plot the relationship by region. Start with decade effects, then assess controls for initial income and industry composition where consistently available. Report pooled estimates and test a regional interaction.
3. **Construct and assess the instrument.** Use a common lagged age distribution for both endpoints of each decade. As a candidate international adaptation, age each country's cohorts forward with leave-one-country-out reference cohort rates, then compute the change in the predicted log older share. Compare reference pools and a mechanical cohort-aging benchmark. The original paper uses national cohort rates for U.S. states. Cross-country starting age structures may proxy for prior development or migration trends, so report first-stage strength, pretrend checks, and weak-IV-robust inference before interpreting 2SLS. Cluster inference by country and account for shared cohort rates in sensitivity analysis.
4. **Decompose the result.** On a common sample, use GDP per hour, hours per employed person, and employment per adult. Check that the log changes and coefficients add up. If hours coverage is too sparse, report GDP per employed person and employment per adult on the broader sample, with the hours-based decomposition on the subset where available. Re-estimate the GDP result on each decomposition sample.

## Phase 2 — Acemoglu and Restrepo

Implement their aging measure and cross-country specification after the Maestas baseline. Compare results on matched country samples and periods before changing definitions or introducing automation. Audit automation coverage separately for Europe and Africa.

## First script

`scripts/build_maestas_panel.py` creates the two baseline log changes. It accepts two normalized CSVs already limited to the candidate countries:

- Population: `iso3,year,age,population`. Include both sexes together and one row per single age, coding the terminal 100+ group as 100. Use counts in persons.
- GDP: `iso3,year,real_gdp`. Use GDP levels in constant 2015 US dollars. Missing GDP can be blank or omitted.

```sh
python scripts/build_maestas_panel.py population.csv real_gdp.csv country_decades.csv
```

Country-decades with both population endpoints remain in the output even if GDP is missing. Country-decades missing a population endpoint are omitted, so check omissions against the country list. Source extraction, real-data coverage, and the choice of instrument reference series are pending. The script has been checked on synthetic data.
