# Data dictionary (initial)

| Variable | Unit | Meaning / provenance |
|---|---|---|
| `iso3` | ISO3 string | Harmonized country identifier, no aggregate regions |
| `year` | year | Calendar year |
| `pop_total` | consistent population unit | All ages, both sexes; UN WPP |
| `pop_age_60_plus` | same population unit | Population ages 60+ |
| `pop_age_50_plus` | same population unit | Population ages 50+ |
| `pop_age_20_49` | same population unit | Population ages 20–49 |
| `share_60_plus` | fraction | pop_age_60_plus / pop_total |
| `aging_ratio_50_to_20_49` | ratio | pop_age_50_plus / pop_age_20_49 |
| `real_gdp_per_capita` | constant-price/PPP units | Pick one consistent series and vintage |
| `log_gdp_pc` | natural log | log(real_gdp_per_capita) |
| `employment_to_population_ratio` | fraction | Specify denominator and source before decomposing |
| `real_output_per_worker` | output/worker | Must share numerator concept with GDP/population for accounting |
| `robots_per_worker` | robots/worker | Proposed extension, not yet included in baseline panel |

## Decisions pending

- Exact Europe and Africa country definitions and inclusion rules
- Country boundary changes and ISO code harmonization
- Whether output is PWT real GDP per capita or WDI GDP per capita
- Sample window, 5-year vs 10-year nonoverlapping changes
- Employment data denominator and automation exposure definition
