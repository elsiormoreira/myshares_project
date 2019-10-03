
# import modules
import pandas as pd


# list of functions
def set_view():
    """Set pandas screen view parameters"""

    # set parameters
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


def read_raw():
    """Read B3 stock data and save it as raw csv file"""

    # list of columns names
    col_names = ['tipo', 'data', 'bdi', 'codigo', 'mercado', 'empresa',
                 'especificacao', 'prazo', 'moeda', 'abertura', 'max',
                 'min', 'medio', 'ajuste', 'of_compra', 'of_venda',
                 'negocios', 'quantidade', 'volume', 'preco', 'indicador',
                 'data_venc', 'fator', 'ponto', 'isi', 'distribuicao']

    # list of columns widths
    col_widths = [2, 8, 2, 12, 3, 12, 10, 3, 4, 13, 13, 13, 13, 13, 13, 13, 5,
                  16, 18, 15, 1, 8, 7, 13, 12, 3]

    # file path
    file_path = 'COTAHIST_A2019.TXT'

    # read tab delimited file
    df = pd.read_fwf(file_path,
                     widths=col_widths,
                     names=col_names,
                     #dtype=col_type,
                     skiprows=1,
                     skipfooter=1,
                     parse_dates=['data', 'data_venc']
                     )

    # export csv raw file
    df.to_csv('raw.csv', index=None)

    # read raw dataset and save as df variable
    df = pd.read_csv('raw.csv')


def read_stock():
    """Read raw data frame as df variable"""

    # set global variable
    global df

    # read raw.csv file as df variable
    df = pd.read_csv('raw.csv')

    # set date column as index
    df = df.set_index('data')

    # divide by 100 adjust column
    df['ajuste'] = df['ajuste'] / 100

    # add day percentage variation column


def choose_stock(stock_names, file_name):
    """Filter stock info from raw data set based on a stock
    code supplied as argument"""

    # change stock_name to capital letters
    stock_names = stock_names.upper()

    # filter by stock name
    df1 = df[df['codigo'] == stock_names]

    # select columns
    df1 = df1[['data', 'ajuste']]

    # change column name
    df1 = df1.rename(columns={'ajuste': stock_names})

    # print first 5 rows on screen
    print(df1.head())

    # save as csv file
    df1.to_csv(file_name, index=None)
