# This file handles transforming the data  from the PDF

def prepare_data_for_saving(raw_data):
    """Make the data ready for saving to file"""
    # List to store transformed data
    transformed_data = []
    
    for annual_data in raw_data:
        current_year = {}
        
        # Save the year
        current_year['Year'] = annual_data['Year']
        
        # Go through all other items (like Revenue, Assets, etc)
        for item_name in annual_data:
            if item_name != 'Year':
                value = annual_data[item_name]
                
                # Save the value if it exists
                if value is not None:
                    current_year[item_name] = value
                # If no value, save None
                else:
                    current_year[item_name] = None
        
        # Add this year's data to list
        transformed_data.append(current_year)
    
    return transformed_data

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
    
    # Transform the test data
    transformed = prepare_data_for_saving(test_data)
    
    for year_data in transformed:
        print(f"\nData for year {year_data['Year']}:")
        
        for item_name, value in year_data.items():
            if item_name != 'Year':
                print(f"{item_name}: {value}")