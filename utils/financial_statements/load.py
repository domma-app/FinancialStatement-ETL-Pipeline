# This file handles saving data to a CSV file
import pandas as pd
import os

def save_data_to_csv(data_to_save, folder_name="datasets"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created new folder: {folder_name}")
    
    df = pd.DataFrame(data_to_save)

    # Set Date sebagai indeks
    df.set_index('Date', inplace=True)

    # Sort berdasarkan tanggal jika diperlukan (gunakan datetime jika ingin benar-benar akurat)
    df.sort_index(ascending=False, inplace=True)

    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    
    file_path = os.path.join(folder_name, 'financial_metrics.csv')
    df.to_csv(file_path)
    print(f"Saved findings to: {file_path}")
    
    return df
