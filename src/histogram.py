# histogram.py

import matplotlib.pyplot as plt
from expenses import expenses_per_category, number_of_expenses_per_category

# Function to calculate percentages for the first histogram
def calculate_percentage(expenses):
    total = sum(expenses.values())
    return {category: (amount / total) * 100 for category, amount in expenses.items()}

# Generate the first histogram (percentage of total amount of expenses per category)
def generate_histogram_amounts():
    percentages = calculate_percentage(expenses_per_category)
    categories = list(percentages.keys())
    values = list(percentages.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title('Percentage of Total Amount of Expenses per Category')
    plt.xlabel('Category')
    plt.ylabel('Percentage')
    plt.show()

# Generate the second histogram (number of expenses per category)
def generate_histogram_counts():
    categories = list(number_of_expenses_per_category.keys())
    counts = list(number_of_expenses_per_category.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, counts, color='lightgreen')
    plt.title('Number of Expenses per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Expenses')
    plt.show()

# Call the functions to generate histograms
if __name__ == "__main__":
    generate_histogram_amounts()
    generate_histogram_counts()
