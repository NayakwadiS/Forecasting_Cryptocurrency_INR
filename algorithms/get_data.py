import yfinance as yf
import pandas as pd
# To disable SettingWithCopyWarning
pd.options.mode.chained_assignment = None  # default='warn'


def crypto_data(ticker, period, intervals):
    df = yf.download(ticker, period=period, interval=intervals)
    i = 0
    while i < 12:       # predict next 12hrs
        last_date = df.iloc[[-1]].index + pd.Timedelta(hours=1)     # for time adjustment getting last pos time
        # print(last_date)
        # last_date = last_date + dt.timedelta(minutes=60)
        df = df.append(pd.DataFrame(index=[last_date[0]]))
        i += 1
    df = df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'])
    df.index.name = 'Datetime'
    df_pred = df
    return df,df_pred


# def get_Data():
#     data = yf.download(tickers='BTC-INR, ETH-INR, LTC-INR', period='1mo', interval="15m",
#                        group_by='ticker')
#     # print(eth)
#     # tickers = yf.Tickers('BTC-INR, ETH-INR,LTC-INR')
#     # print(tickers.tickers)
#       print(tickers.tickers['BTC-INR'].info)
#     # ltc = tickers.tickers['LTC-INR'].history(period="1m",interval="5m")
#     btc = data['BTC-INR']
#     eth = data['ETH-INR']
#     ltc = data['LTC-INR']
#     df_btc = btc.dropna()
#     df_btc.reset_index(inplace=True)
#     df_btc["closeDiff"] = df_btc["Close"].diff()
#     # df_btc['Datetime'] = pd.to_datetime(df_btc['Datetime'], unit='s')
#     print(df_btc)
#
#     # df_btc.plot(x='Datetime',y='Close')
#     plt.plot(df_btc['Datetime'], df_btc['Close'], color='blue', label='Trend')
#     plt.show()
