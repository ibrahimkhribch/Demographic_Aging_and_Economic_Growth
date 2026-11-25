"""Build a Maestas-style baseline panel from normalized UN WPP and WDI CSVs."""

import argparse
import csv
import math
from pathlib import Path


def load_population(path):
    populations = {}
    with path.open(newline="", encoding="utf-8-sig") as source:
        for row in csv.DictReader(source):
            key = (row["iso3"], int(row["year"]))
            age = int(row["age"])
            count = float(row["population"])
            cohorts = populations.setdefault(key, {})
            if age in cohorts or not math.isfinite(count) or count < 0:
                raise ValueError(f"Invalid or duplicate population for {key}, age {age}")
            cohorts[age] = count

    totals = {}
    for key, cohorts in populations.items():
        if cohorts.keys() != set(range(101)):
            raise ValueError(f"Expected single ages 0 through 99 and age 100+ for {key}")
        adults = sum(cohorts[age] for age in range(20, 101))
        older = sum(cohorts[age] for age in range(60, 101))
        if not 0 < older <= adults:
            raise ValueError(f"Invalid adult or older population for {key}")
        totals[key] = (adults, older)
    return totals


def load_gdp(path):
    gdp = {}
    with path.open(newline="", encoding="utf-8-sig") as source:
        for row in csv.DictReader(source):
            key = (row["iso3"], int(row["year"]))
            if key in gdp:
                raise ValueError(f"Duplicate GDP observation for {key}")
            value = row["real_gdp"].strip()
            gdp[key] = float(value) if value else None
    return gdp


def log_change(start, end):
    if start is None or end is None:
        return ""
    return math.log(end) - math.log(start)


def build_panel(population, gdp, output, start, end):
    fields = (
        "iso3", "start_year", "end_year", "older_share_start", "older_share_end",
        "real_gdp_per_adult_start", "real_gdp_per_adult_end",
        "dlog_older_share", "dlog_real_gdp_per_adult",
    )

    def measures(key):
        adults, older = population[key]
        output_value = gdp.get(key)
        if output_value is not None and (not math.isfinite(output_value) or output_value <= 0):
            raise ValueError(f"Invalid real GDP for {key}")
        return older / adults, output_value / adults if output_value is not None else None

    with output.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.writer(destination)
        writer.writerow(fields)
        for iso3 in sorted({iso3 for iso3, _ in population}):
            for first in range(start, end, 10):
                last = first + 10
                if (iso3, first) not in population or (iso3, last) not in population:
                    continue
                older_first, gdp_first = measures((iso3, first))
                older_last, gdp_last = measures((iso3, last))
                writer.writerow((
                    iso3, first, last, older_first, older_last, gdp_first, gdp_last,
                    log_change(older_first, older_last), log_change(gdp_first, gdp_last),
                ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("population", type=Path)
    parser.add_argument("gdp", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--start", type=int, default=1990)
    parser.add_argument("--end", type=int, default=2020)
    args = parser.parse_args()
    if args.end <= args.start or (args.end - args.start) % 10:
        parser.error("the endpoint must be one or more full decades after the start")
    if args.output.resolve() in {args.population.resolve(), args.gdp.resolve()}:
        parser.error("the output must differ from both inputs")
    build_panel(load_population(args.population), load_gdp(args.gdp), args.output, args.start, args.end)


if __name__ == "__main__":
    main()
