# Research design (draft, not preregistered)

## Questions

1. How does population aging correlate with growth in real GDP per capita across European and African countries?
2. Is this relationship mediated by employment changes or labor productivity?
3. Does automation intensity moderate the aging-growth relationship, conditional on IFR data availability?
4. Do estimates differ by region and by alternative aging definitions?

## Two literatures, different designs

**Maestas, Mullen & Powell (2023):** US-state aging shocks, long differences and an instrument based on predicted demographic changes. Their empirical identification assumptions need to be understood and examined before extension to countries.

**Acemoglu & Restrepo (2017):** international aging-growth patterns with a mechanism involving automation responses. Automation may be endogenous to productivity and growth.

Do **not** describe a simple cross-country panel association as a causal replication of the papers.

## Candidate estimation framework

Start with an annual descriptive panel; aggregate to non-overlapping 5- or 10-year periods (compare both). Candidate baseline:

`Delta_h log(y_it) = beta * Delta_h aging_it + gamma' * X_it + alpha_i + tau_t + epsilon_it`

Here `Delta_h log(y_it)` is **cumulative** log GDP-per-capita change over h years. Annualized growth is `Delta_h log(y_it) / h`; choose one and state it. `aging` can be the 60+ population share (percentage points) or the 50+/20–49 ratio (change in ratio), with separate regressions; avoid interchanging coefficient units.

Check whether country fixed effects in a differenced specification are identifiable with the number of periods. Cluster standard errors by country; with few African countries consider small-cluster robustness.

Mechanisms:
- Repeat using employment-population measure and labor productivity.
- When components are definitionally consistent, `log(GDP/population) = log(GDP/employed) + log(employed/population)`. Avoid mixing different population denominators or national-account output definitions.

Automation extension:
`Delta_h log(y_it) = beta*Delta_h aging_it + theta*robots_it + delta*(Delta_h aging_it * robots_it) + controls + FE + epsilon_it`

Predefine whether robots are baseline or lagged; avoid contemporaneous endogenous robot deployment for causal interpretation. Restrict this model to documented IFR coverage and show how sample composition changes.

## Identification and threats

- Reverse causality (growth affects fertility, mortality, migration and population composition)
- Demographic projection instruments and their exclusion restrictions
- GDP measurement/PPP comparability and changing statistical definitions
- Unobserved structural transformation, education, institutions and migration
- Automation measurement/IFR selection across Africa
- Country composition, missingness, pre-trends, persistence, and finite sample

A Maestas-inspired IV is **future work contingent on credible country-level exclusion restrictions**. Do not generate instrumental variables solely to imitate the US paper.

## Planned deliverables

- Source and coverage table
- Age composition and GDP growth plots
- Transparent construction of nonoverlapping differences
- Main estimates with robustness checks, country-clustered uncertainty
- Separate automation results for a supported country sample
- Research note documenting interpretation and limitations
