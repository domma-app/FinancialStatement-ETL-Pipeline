# This file handles saving data to a CSV file
import pandas as pd
import os

def save_data_to_csv(data_to_save, folder_name="datasets"):
    """Save our financial data to a CSV file"""
    if not os.path.exists(folder_name):
        # Create folder datasets if it doesn't exist
        os.makedirs(folder_name)
        print(f"Created new folder: {folder_name}")
    
    # Convert data into a pandas DataFrame
    df = pd.DataFrame(data_to_save)
    
    # Set the Year column as the index
    df.set_index('Year', inplace=True)
    
    # Sort the years from newest to oldest
    df.sort_index(ascending=False, inplace=True)
    
    # Format numbers as integers
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    
    # Create the full path for our CSV file
    file_path = os.path.join(folder_name, 'financial_metrics.csv')
    
    # Save the data to the CSV file
    df.to_csv(file_path)
    print(f"Saved findings to: {file_path}")
    
    return df

if __name__ == "__main__":
    # Example data to test with
    test_data = [
        {
            'Year': 2022,
            'Revenue': 150000000,
            'Total Profit Loss': 70000000,
            'Total Assets': 500000000,
            'Liabilities': 250000000,
            'Equity': 250000000
        },
        {
            'Year': 2021,
            'Revenue': 140000000,
            'Total Profit Loss': 65000000,
            'Total Assets': 480000000,
            'Liabilities': 240000000,
            'Equity': 240000000
        }
    ]
    
    # Save the test data and get back the DataFrame
    saved_data = save_data_to_csv(test_data)
    
    print("\nSaved DataFrame:")
    print(saved_data)