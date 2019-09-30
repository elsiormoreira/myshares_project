"""
Basic and preliminary script to evaluate stocks. This is a test file where
will be develop the firsts steps to create future functions. This is a lab
area.
"""

# import module
import pandas as pd

# set pandas parameters
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# save raw file as 'df' variable
df = pd.read_csv('raw.csv')

# read tickers file list
tickers = pd.read_csv('ibov.csv')

# convert tickers file into a list
tickers = tickers['ibov'].tolist()

# change data frame column type
df['data'] = pd.to_datetime(df['data'])

# clean and prepare data frame
df_prep = (df
           .loc[:, ['data', 'codigo', 'ajuste']]
           .query('codigo == @tickers')
           .assign(ajuste = df['ajuste'] / 100)
           .rename(columns = {'data': 'date',
                              'codigo': 'ticker',
                              'ajuste': 'price'})
           .set_index('date')
           )

# calculate mean, std and ic from each stock
df_calc = df_prep
df_calc['pct_change'] = round((df_calc
                               .groupby('ticker')
                               .price.pct_change() * 100
                               ), 2)


#TODO
# divide adjust column by 100
# check first elements
# check last elements
# get some information about dataset
# number of rows and columns
# column names
# row names
# count values by column
# df['mercado'].value_counts()
# count number of unique values by column
# df.nunique()
# find null values by column
# df.isnull().sum()
