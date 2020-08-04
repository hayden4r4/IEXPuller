#Importing Packages
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
import datetime
import pandas
import os
#Requesting Inputs
ticker=input('Please Type Ticker Symbol...:')
start=(input('Please Enter Start Date in YearMonthDay Format...:'))
end=(input('Please Enter End Date in YearMonthDay Format...:'))
close_only=input('Would You Like Closing Price Only? Select No for a Full Quote. Please Enter Y or N (default is N):')
if close_only==['Y', 'y']:
  close_only='True'
elif close_only==['N', 'n']:
  close_only='False'
elif not close_only:
  close_only='False'
#Assigning API Key from file in My Drive
token=os.getenv('IEX_API_KEY')
quote=get_historical_data(ticker, start, end, close_only=close_only, output_format='pandas', token=token)
print(f'{ticker} Quote:')
print(quote)