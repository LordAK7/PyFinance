# import statements
import json
from datetime import datetime

# Define the path to the JSON file
json_file_path = 'finance_statements.json'

# Define the current month and year
current_month = datetime.now().month
current_year = datetime.now().year

# Initialize the variables
total_expenses_for_month = 0
expenses_per_category = {
    "groceries": 0,
    "travel": 0,
    "needed expenses": 0,
    "books/courses": 0,
    "others": 0
}
number_of_expenses_per_category = {
    "groceries": 0,
    "travel": 0,
    "needed expenses": 0,
    "books/courses": 0,
    "others": 0
}

# Function to read the JSON file and calculate expenses
def calculate_expenses():
    global total_expenses_for_month

    # Read the JSON file
    try:
        with open(json_file_path, 'r') as file:
            finance_statements = json.load(file)
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"File {json_file_path} is not a valid JSON.")
        return

    # Calculate the expenses
    for statement in finance_statements:
        # Parse the date from the statement
        date = datetime.strptime(statement['date'], "%Y-%m-%d")
        # Check if the statement is for the current month and year
        if date.month == current_month and date.year == current_year:
            amount = statement['amount']
            category = statement['category']
            # Add to total expenses for the month
            total_expenses_for_month += amount
            # Add to total and count per category
            expenses_per_category[category] += amount
            number_of_expenses_per_category[category] += 1

# Execute the function
calculate_expenses()

# Print the results
print(f"Total expenses for month = {total_expenses_for_month}")
for category, total in expenses_per_category.items():
    print(f"Total {category} expense = {total}")
    print(f"Number of {category} expenses = {number_of_expenses_per_category[category]}")


# At the end of expenses.py, after the calculations
if __name__ == "__main__":
    calculate_expenses()