# This file handles transforming the data  from the PDF

def prepare_data_for_saving(raw_data):
    """Transform raw data for saving"""
    # Initialize an empty list for the transformed data
    transformed_data = []
    
    for annual_data in raw_data:
        # Store the current data in dictionary format
        current_data = {}

        # Add the date to the current data
        current_data['Date'] = annual_data['Date']
        
        for item_name in annual_data:
            # Skip the 'Date' field
            if item_name != 'Date':
                value = annual_data[item_name]
                # Add the value or None if the value is missing
                current_data[item_name] = value if value is not None else None

        # Append the current data to the transformed list
        transformed_data.append(current_data)
    
    # Return the transformed data
    return transformed_data


