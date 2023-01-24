"""
msc_converter.writer cujo dstino são arquivos.
"""

class ToCsv:
    """
    Escreve os dados convertidos para arquivos CSV.
    """
    def __init__(self, filepath):
        self.destiny = filepath

    def write(self, df):
        df.to_csv(self.destiny, sep=';', index=False, decimal=',')


class ToPickle:
    """
    Escreve os dados convertidos para arquivos Pickle.
    """
    def __init__(self, filepath):
        self.destiny = filepath

    def write(self, df):
        df.to_pickle(self.destiny)

class ToExcel:
    """
    Escreve para arquivos do Excel
    """
    def __init__(self, filepath):
        self.destiny = filepath

    def write(self, df):
        df.to_excel(self.destiny, sheet_name='MSC', index = False)


class ToParquet:
    """
    Escreve para arquivos Parquet
    """

    def __init__(self, filepath):
        self.destiny = filepath

    def write(self, df):
        df.to_parquet(self.destiny)