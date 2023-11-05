# PyFinance

# Finance Tracker

## Overview
This project consists of a simple finance tracking system that allows users to input their financial statements, categorize them, and then analyze the expenses through various metrics and visualizations.

## Files
- `main.py`: The main script to input finance statements and save them to a JSON file.
- `expenses.py`: A script that calculates the total expenses for the current month, as well as the total and number of expenses per category.
- `histogram.py`: A script that generates histograms to visualize the data calculated by `expenses.py`.
- `finance_statements.json`: The JSON file where finance statements are stored.

## Usage

### Adding Finance Statements
To add a finance statement, run the `main.py` script and follow the prompts:

```bash
python main.py
