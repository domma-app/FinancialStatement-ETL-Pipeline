# This file handles extracting the financial data from the text
import re
from datetime import datetime

def find_date(text):
    """
    Finds a date in DD/MM/YYYY format and converts it to 'DD Month YYYY'.
    """
    pattern = re.search(r"Bulan yang berakhir pada\s*(\d{1,2}/\d{1,2}/\d{4})", text)

    if pattern:
        raw_date = pattern.group(1)
        try:
            date_obj = datetime.strptime(raw_date, "%d/%m/%Y")
            return date_obj.strftime("%d %B %Y")  # e.g., 30 September 2024
        except ValueError:
            return None

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
    # Get the date from the text
    date = find_date(text)
    if date is None:
        print("Could not find any date in the text!")
        return []
    
    financial_data = {'Date': date}
    
    # Split text into lines
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        
        # Check for Revenue
        if "revenue" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                financial_data['Revenue'] = numbers[0]
        
        # Check for Total Profit (Loss)
        elif "total profit (loss)" in line_lower or "jumlah laba (rugi)" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                financial_data['Total Profit (Loss)'] = numbers[0]
        
        # Check for Total Assets
        elif "total assets" in line_lower or "jumlah aset" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                financial_data['Total Assets'] = numbers[0]
        
        # Check for Liabilities
        elif "total liabilities" in line_lower or "jumlah liabilitas" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                financial_data['Total Liabilities'] = numbers[0]
        
        # Check for Equity
        elif "total equity" in line_lower or "jumlah ekuitas" in line_lower:
            numbers = get_numbers_from_line(line)
            if len(numbers) >= 2:
                financial_data['Total Equity'] = numbers[0]
    
    # Return extracted financial data
    return [financial_data]
