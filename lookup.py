import requests
from forex_python.converter import CurrencyRates
import datetime

c = CurrencyRates()

convert_date_str = input("Please enter the date of currency conversion (mm/dd/yyyy) > ")
cmonth, cday, cyear = convert_date_str.split('/')
date_obj = datetime.datetime(int(cyear),int(cmonth),int(cday), 17, 00)
COUNTRY = 'USD'
convert_currency = input("Please enter the currency you are converting to USD (CAD, EUR, GBP) > ").upper()
rate = c.get_rate(convert_currency, COUNTRY, date_obj)
print(f"The currency exchange rate for {convert_currency} to USD on {convert_date_str} was {rate} > {round(rate, 2)}")
