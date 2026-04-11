# Python-data-toolbox

A structured Python practice repository for data work.

This repository documents a progressive learning path from Python fundamentals to applied data workflows, including CSV processing, automation, API ingestion, JSON handling, and pandas analysis.

## Project goal

The goal of this repository is to build strong Python foundations for data work through a clean, step-by-step progression.

The path followed in this repo is:

- Python fundamentals
- intermediate Python concepts
- data processing with CSV and files
- simple automation scripts
- API and JSON ingestion
- pandas analysis on real datasets

This repository is a learning environment focused on practical, GitHub-friendly work.

## Repository structure

```text
python-data-toolbox/
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── ticket_sales.csv
│   │   ├── api/
│   │   │   └── github/
│   │   │       ├── repo_response.json
│   │   │       └── issues_response.json
│   │   └── retail/
│   │       └── online_retail.csv
│   ├── cleaned/
│   │   ├── clean_ticket_sales.csv
│   │   ├── pipeline_clean_ticket_sales.csv
│   │   ├── github_issue_records.csv
│   │   └── retail/
│   │       └── online_retail_clean.csv
│   └── exports/
│       ├── daily_sales_report.txt
│       ├── match_ticket_report.txt
│       ├── sales_summary.txt
│       ├── vip_customer_list.txt
│       └── retail/
│           ├── monthly_revenue.csv
│           └── country_revenue.csv
├── exercises/
│   ├── 01_basics/
│   ├── 02_intermediate/
│   ├── 03_data_structures/
│   └── 04_problem_solving/
├── scripts/
│   ├── 01_basics/
│   ├── 02_data_processing/
│   ├── 03_automation/
│   └── 04_api_and_json_github/
├── notebooks/
│   ├── 01_pandas_basics_retail/
│   └── 02_pandas_api_tech/
└── notes/

## Folder overview

### `data/`

Stores raw inputs, cleaned datasets, and exported outputs.

- `raw/` → source files and API responses
- `cleaned/` → cleaned and normalized datasets
- `exports/` → final exported outputs and summaries

### `exercises/`

Contains focused Python exercises used to reinforce fundamentals.

- `01_basics/`
- `02_intermediate/`
- `03_data_structures/`
- `04_problem_solving/`

### `scripts/`

Contains applied Python scripts with a more workflow-oriented structure.

- `01_basics/` → first business-style scripts
- `02_data_processing/` → CSV cleaning, transformation, validation, export
- `03_automation/` → simple automation logic
- `04_api_and_json_github/` → GitHub API, JSON ingestion, and issue flattening

### `notebooks/`

Contains Jupyter notebooks for pandas practice and exploratory analysis.

- `01_pandas_basics_retail/` → pandas fundamentals on the Online Retail dataset
- `02_pandas_api_tech/` → pandas work on GitHub API JSON data

### `notes/`

Contains short learning notes and reminders.

## Completed blocks

### Python exercises

- basics
- intermediate concepts
- data structures
- problem solving

### Python scripts

- ticketing basics
- CSV processing
- automation
- GitHub API and JSON

### Pandas notebooks

- retail dataset loading
- cleaning
- filtering and sorting
- groupby analysis
- pivot analysis
- export
- GitHub JSON loading
- issue normalization
- time-based issue analysis

## Main datasets and sources

### Online Retail dataset

Used for pandas practice on:

- cleaning
- filtering
- sorting
- aggregations
- pivot tables
- exports

### GitHub public API

Used for:

- fetching repository metadata
- saving JSON responses
- loading JSON into pandas
- normalizing issue records
- time-based analysis

## Skills covered

This repository includes practice with:

- Python fundamentals
- functions and control flow
- file handling
- CSV import / export
- JSON reading and writing
- API requests with `requests`
- date handling with `datetime`
- pandas DataFrames
- filtering and sorting
- `groupby`
- `pivot_table`
- dataset cleaning
- exporting analysis results

## Environment

This project uses a local virtual environment:

```text
.venv/

