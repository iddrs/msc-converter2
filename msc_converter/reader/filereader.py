"""
msc_converter.reader cuja origem são arquivos.
"""
import pandas


class FromCsv:
    """
    Lê a MSC a partir de arquivos CSV gerados para o envio ao SICONFI.
    """
    def __init__(self, filepath):
        self.source = filepath
        self.metadata = self.get_metadata()

    def load(self):
        dtype = {
            'ContaContabil': str,
            'InformacaoComplementar1': str,
            'TipoInformacaoComplementar1': str,
            'InformacaoComplementar2': str,
            'TipoInformacaoComplementar2': str,
            'InformacaoComplementar3': str,
            'TipoInformacaoComplementar3': str,
            'InformacaoComplementar4': str,
            'TipoInformacaoComplementar4': str,
            'InformacaoComplementar5': str,
            'TipoInformacaoComplementar5': str,
            'InformacaoComplementar6': str,
            'TipoInformacaoComplementar6': str,
            'Valor': float,
            'TipoValor': str,
            'NaturezaValor': str
        }
        df = pandas.read_csv(self.source, sep=';', header=0, dtype=dtype, skiprows=1, index_col=False)
        return df

    def get_metadata(self):
        buffer = ''
        with open(self.source, 'r') as f:
            for l in f:
                buffer = l
                break
        buffer = buffer.split(';')
        ente = buffer[0]
        buffer = buffer[1].split('-')
        ano = buffer[0]
        mes = buffer[1]
        metadata = {
            'ente': ente,
            'ano': ano,
            'mes': mes
        }
        return metadata