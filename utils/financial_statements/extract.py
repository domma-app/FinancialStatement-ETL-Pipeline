# This file handles extracting the financial data from the text
import re

def find_years(text):
    """Find the years from the text"""
    # List to store years 
    found_years = []
    
    # Split the text into lines
    text_lines = text.split('\n')
    
    for line in text_lines:
        # Gathering dates
        if "31 December" in line:
            # Find all 4-digit numbers that start with 20 (2021, 2022, etc)
            year_matches = re.findall(r'20\d\d', line)
            
            # Convert each year from text to number
            for year in year_matches:
                year_number = int(year)
                found_years.append(year_number)
    
    if len(found_years) > 0:
        # Sort years from newest to oldest
        found_years.sort()
        found_years.reverse()
        
        # Return the current and the previous year
        return [found_years[0], found_years[0] - 1]
    
    return None

def get_numbers_from_line(line):
    """Get numbers from a line of text"""
    line = line.replace('Rp', '')
    line = line.replace('$', '')
    line = line.replace(',', '')
    
    # List to store numbers
    numbers_found = []
    
    # Split line into words
    words = line.split()
    
    for word in words:
        # Remove parentheses from the word
        clean_word = word.replace('(', '').replace(')', '')
        
        # Try to convert the word to a number
        try:
            if clean_word.strip() != '':
                number = float(clean_word)
                numbers_found.append(number)
        except:
            continue
    
    return numbers_found

def get_financial_data(text):
    """Get financial information from the text"""
    # Get the years from the text
    years = find_years(text)
    if years is None:
        print("Could not find any years in the text!")
        return []
    
    this_year = {'Year': years[0]}
    last_year = {'Year': years[1]}
    
    # Split text into lines
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        
        # Check for Revenue
        if "revenue" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                this_year['Revenue'] = numbers[0]
                last_year['Revenue'] = numbers[1]
        
        # Check for Total Profit (Loss)
        elif "total profit (loss)" in line_lower or "jumlah laba (rugi)" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                this_year['Total Profit (Loss)'] = numbers[0]
                last_year['Total Profit (Loss)'] = numbers[1]
        
        # Check for Total Assets
        elif "total assets" in line_lower or "jumlah aset" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                this_year['Total Assets'] = numbers[0]
                last_year['Total Assets'] = numbers[1]
        
        # Check for Liabilities
        elif "total liabilities" in line_lower or "jumlah liabilitas" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                this_year['Total Liabilities'] = numbers[0]
                last_year['Total Liabilities'] = numbers[1]
        
        # Check for Equity
        elif "total equity" in line_lower or "jumlah ekuitas" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                this_year['Total Equity'] = numbers[0]
                last_year['Total Equity'] = numbers[1]
    
    # Return both years' data
    return [this_year, last_year]

if __name__ == "__main__":
    # Example text to test with
    test_text = """
    Statement of financial position 31 December 2022 31 December 2021
    
    Revenue: 150000000 140000000
    Total Profit (Loss): 70000000 65000000
    Total Assets: 500000000 480000000
    Total Liabilities: 250000000 240000000
    Total Equity: 250000000 240000000
    """
    
    # Get the results
    results = get_financial_data(test_text)
    
    for year_data in results:
        print(f"\nData for year {year_data['Year']}:")

        for item_name, value in year_data.items():
            if item_name != 'Year':
                print(f"{item_name}: {value}") 