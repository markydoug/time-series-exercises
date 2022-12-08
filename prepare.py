import pandas as pd
from datetime import timedelta, datetime
import numpy as np

def acquire_and_prep_sales():
    df = pd.read_csv('tsa_store_data.csv')
    git 
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.igitndex.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def acquire_and_prep_ops():
    df = pd.read_csv('opsd_germany_daily.csv')
    df['Date'] = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['Year'] = df.index.year
    gi
    df = df.fillna(0) 

    return df