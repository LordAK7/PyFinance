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
```

### Calculating Expenses

To calculate the expenses for the current month, run the expenses.py 
it will also update the global variables with the total expenses for the month and the expenses per category.

```bash
python expenses.py
```

### Generating Histograms

To generate histograms based on the calculated expenses, first ensure that expenses.py has been run, then execute:
Two histograms will be displayed:
The percentage of the total amount of expenses per category.
The number of expenses per category.

```bash
python histogram.py
```
The percentage of the total amount of expenses per category.
![image](https://github.com/LordAK7/PyFinance/assets/90541300/70380c6a-a45c-4bd1-b5af-4d448ffa870d)

The number of expenses per category.
![image](https://github.com/LordAK7/PyFinance/assets/90541300/6f45cf5d-7fa2-4978-8011-b3edb2587a6f)



## Contributing

### Contributions to this project are welcome. Please fork the repository and submit a pull request.
License

This project is open-source and available under the MIT License.
