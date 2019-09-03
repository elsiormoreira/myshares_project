
# import modules
import pandas as pd

# functions
def raw_b3():
    """Read B3 data and save raw data as csv file"""

    # import modules
    import pandas as pd

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

    # export csv raw dataset
    df.to_csv('raw.csv', index=None)


def standardize_view():
    """Set pandas screen view parameters"""

    # set parameters
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.max_colwidth', 30)
    pd.set_option('display.precision', 2)