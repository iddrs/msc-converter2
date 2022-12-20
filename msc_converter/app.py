"""
Controller da conversão
"""
import pandas
from tqdm import tqdm


class App:
    """
    Classe principal da aplicação.

    Comanda o processo de leitura, conversão e salvamento.
    """
    def __init__(self, logger, reader, writers):
        self.logger = logger
        self.reader = reader
        self.writers = writers
        self.df = None
        self.metadata = []
        self.logger.info('Aplicação de conversão preparada.')

    def run(self):
        """
        Executa o pipeline da conversão.

        :return: None
        """
        self.logger.info('Conversão iniciada...')
        self.df = self.reader.load()
        self.metadata = self.reader.metadata
        df = self.parse()
        self.write(df)
        self.logger.info('Conversão finalizada!')

    def parse(self):
        """
        Executa a conversão.

        :return: pandas.DataFrame
        """
        self.logger.info('Iniciando parsing...')

        dfparsed = pandas.DataFrame(columns=['ContaContabil', 'PO', 'FP', 'DC', 'FR', 'CO', 'NR', 'ND', 'FS', 'AI', 'Valor', 'TipoValor', 'NaturezaValor'])
        df = self.reader.load()

        with tqdm(total=len(df)) as progressbar:
            for index, row in df.iterrows():
                data = {
                    'ContaContabil': row['ContaContabil'],
                    'PO': None,
                    'FP': None,
                    'DC': None,
                    'FR': None,
                    'CO': None,
                    'NR': None,
                    'ND': None,
                    'FS': None,
                    'AI': None,
                    'Valor': row['Valor'],
                    'TipoValor': row['TipoValor'],
                    'NaturezaValor': row['NaturezaValor']
                }
                for i in range(1, 7, 1):
                    match row['TipoInformacaoComplementar' + str(i)]:
                        case 'PO':
                            data['PO'] = row['InformacaoComplementar' + str(i)]
                        case 'FP':
                            data['FP'] = row['InformacaoComplementar' + str(i)]
                        case 'DC':
                            data['DC'] = row['InformacaoComplementar' + str(i)]
                        case 'FR':
                            data['FR'] = row['InformacaoComplementar' + str(i)]
                        case 'CO':
                            data['CO'] = row['InformacaoComplementar' + str(i)]
                        case 'NR':
                            data['NR'] = row['InformacaoComplementar' + str(i)]
                        case 'ND':
                            data['ND'] = row['InformacaoComplementar' + str(i)]
                        case 'FS':
                            data['FS'] = row['InformacaoComplementar' + str(i)]
                        case 'AI':
                            data['AI'] = row['InformacaoComplementar' + str(i)]
                        case other:
                            pass
                dfparsed = pandas.concat([dfparsed, pandas.DataFrame([data])])
                progressbar.update(1)

        dfparsed.Ente = self.metadata['ente']
        dfparsed.Periodo = '{0}-{1}'.format(self.metadata['ano'], self.metadata['mes'])

        return dfparsed


    def write(self, df):
        """
        Escreve os dados através dos writers.

        :return:
        """
        self.logger.info('Escrevendo so dados...')

        for w in self.writers:
            self.logger.debug(f'Escrevendo para {w.destiny} ...')
            w.write(df)

        self.logger.info('Dados escritos.')