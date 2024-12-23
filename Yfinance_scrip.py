import yfinance as yf
PFE=yf.Ticker('PFE')
data=PFE.history(period='5y') # Retrieve 5 years of historical data
print(data.head())# Print the first few rows of the data
data.to_csv('PFE_stock_data.csv')# Save the data to a CSV file

LLY=yf.Ticker('LLY')
data=LLY.history(period='5y') 
print(data.head())
data.to_csv('LLY_stock_data.csv')

JNJ=yf.Ticker('JNJ')
data=JNJ.history(period='5y') # Retrieve 5 years of historical data
print(data.head())
data.to_csv('JNJ_stock_data.csv')