# ui.py

from algorithms import analyze_data
import pandas as pd

def main():
    # Load financial data
    data = pd.read_csv('../data/financial_data.csv')
    
    # Display options to the user
    print("Welcome to Personalized Financial Coaching!")
    print("1. Analyze financial data")
    choice = input("Enter your choice: ")
    
    # Perform actions based on user choice
    if choice == '1':
        analyze_data(data)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
