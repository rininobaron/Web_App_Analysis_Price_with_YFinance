import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
#from get_all_tickers import get_tickers as gt

#list_of_tickers = gt.get_tickers()
list_of_tickers = pd.read_csv('https://raw.githubusercontent.com/shilewenuw/get_all_tickers/master/get_all_tickers/tickers.csv')

print("Tickers disponibles: ")
print()
list_start = ['DDD']
list_end = list_of_tickers['DDD'].tolist()
list_of_tickers = list_start + list_end
#index = list_of_tickers.index('BZ')
#print(index)
counter = 0
for ticker in list_of_tickers:
    if counter == 10:
        break
    print(ticker)
    counter += 1
print()

ticker = input("Introduzca un YAHOO TICKER: ")
print()
print("Introduzca los siguientes datos.")
print()
start = input("Fecha de Inicio (AAAA-MM-DD): ")
print()
end = input("Fecha de Término (AAAA-MM-DD): ")
print()

aapl_df = yf.download(ticker, 
                      start=start, 
                      end=end, 
                      progress=False,
)

# time_interval = input('Intervalo de tiempo (daily, weekly, montly, annual): ')
# yahoo_financials = YahooFinancials('AAPL')
# aapl_df = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
#                                                   end_date='2019-12-31', 
#                                                   time_interval=time_interval)

aapl_df = pd.DataFrame(aapl_df)

print(aapl_df.head())
#print(help(yf.download))