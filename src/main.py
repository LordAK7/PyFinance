# import statements

import json
from datetime import datetime
import os

# Structure of the finance statement
finance_categories = [
    "groceries",
    "travel",
    "needed expenses",
    "books/courses",
    "others"
]


# Function to get user input
def get_finance_input():
    print("Enter your finance statement details:")

    # Get the category
    while True:
        category = input(f"Type of finance statement (category) {finance_categories}: ").lower()
        if category in finance_categories:
            break
        else:
            print("Invalid category. Please choose from the list.")

    # Get the date
    date_str = input("Date (YYYY-MM-DD): ")
    try:
        # Validate the date format
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return None

    # Get the amount
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Amount must be a number.")
        return None

    # Get the description
    description = input("Description: ")

    # Get the image file path
    image_path = input("Image path (image of the bill or the receipt): ")
    if not os.path.isfile(image_path):
        print("Image file does not exist.")
        return None

    # Create a dictionary for the finance statement
    finance_statement = {
        "category": category,
        "date": date_str,
        "amount": amount,
        "description": description,
        "image_path": image_path
    }

    return finance_statement


# Function to save the data to a JSON file
def save_to_json(data, filename="finance_statements.json"):
    try:
        # Load existing data
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Append new data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

        print("Data saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function to run the program
def main():
    finance_input = get_finance_input()
    if finance_input:
        save_to_json(finance_input)


if __name__ == "__main__":
    main()
