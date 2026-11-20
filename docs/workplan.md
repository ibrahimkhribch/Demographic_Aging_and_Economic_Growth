# First-week workplan

**Suggested start: Monday 23 November 2026.** The goal is a clean, auditable descriptive panel, not premature regression results.

- [ ] **Monday — Literature:** Read both foundational papers; write a one-page comparison of outcomes, aging measures, sample, estimator and identification.
- [ ] **Tuesday — Data inventory:** Choose a preliminary list of European and African countries; retrieve UN WPP age bands; select WDI or PWT GDP per capita with documented units.
- [ ] **Wednesday — Harmonization:** Standardize ISO3 identifiers and population age groups; run the starter panel script and inspect coverage/missingness; record dropped observations.
- [ ] **Thursday — Descriptives:** Plot aging and GDP across countries/regions; inspect outliers and identify feasible 5- and 10-year windows.
- [ ] **Friday — Design review:** Decide sample and estimand; write a short design memo on causal limitations; decide what would be needed for Maestas-style IV and Acemoglu–Restrepo automation tests.

## Definition of done for week 1

1. Source manifest and stable raw files on disk.
2. Country × year panel with documented variables, no duplicate keys.
3. Coverage tables and at least two exploratory plots.
4. Written decision about the baseline aging measure and outcome.
5. A list of identification and data-coverage obstacles.

## Later milestones

**Week 2:** long-difference data, benchmark regressions and robust uncertainty.

**Week 3:** employment/productivity mechanisms and sensitivity to definitions.

**Week 4+:** automation subset, IV feasibility assessment and first draft.
