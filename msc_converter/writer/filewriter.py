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