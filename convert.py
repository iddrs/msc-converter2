"""
Ponto de entrada da aplicação.
"""
import os
import msc_converter.app, msc_converter.reader.filereader, msc_converter.writer.filewriter
import logging as logger

# Prepara o logger
logger.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s', level=logger.DEBUG, datefmt='%Y-%m-%d %H:%M:s')

# Prepara o reader
ano = str(input('Digite o ano [AAAA]: '))
mes = str(input('Digite o mês [MM]: ')).zfill(2)

meses = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Marco',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro',
}
f = f'MSCAgregada{meses[mes]}{ano}.csv'
sourcefile = os.path.join(r'Z:\MSC', ano, f)
logger.info(f'Carregando dados de {sourcefile}')
reader = msc_converter.reader.filereader.FromCsv(sourcefile)

# Prepara os writeres
destinycsv = os.path.join(r'C:\Users\Everton\Desktop\Prefeitura\MSC\v2\csv', f'{ano}-{mes}.csv')
destinypickle = os.path.join(r'C:\Users\Everton\Desktop\Prefeitura\MSC\v2\pickle', f'{ano}-{mes}.pickle')
writers = [
    msc_converter.writer.filewriter.ToCsv(destinycsv),
    msc_converter.writer.filewriter.ToPickle(destinypickle)
]

# Executa a conversão
app = msc_converter.app.App(logger, reader, writers)
app.run()