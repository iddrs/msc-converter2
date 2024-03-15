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
mes = str(input('Digite o mês [MM] (1 ~ 13): ')).zfill(2)

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

if mes == '13':
    f = f'MSCEncerramento{ano}.csv'
else:
    f = f'MSCAgregada{meses[mes]}{ano}.csv'
sourcefile = os.path.join(r'Z:\MSC', ano, f)
logger.info(f'Carregando dados de {sourcefile}')
reader = msc_converter.reader.filereader.FromCsv(sourcefile)

# Prepara os writeres
# destinycsv = os.path.join(r'C:\Users\Everton\Desktop\Prefeitura\MSC\csv', f'{ano}-{mes}.csv')
# destinypickle = os.path.join(r'C:\Users\Everton\Desktop\Prefeitura\MSC\pickle', f'{ano}-{mes}.pickle')
destinyexcel = os.path.join(r'C:\Users\Everton\OneDrive - independencia.rs.gov.br\Prefeitura\MSC\excel', f'{ano}-{mes}.xlsx')
destinyparquet = os.path.join(r'C:\Users\Everton\OneDrive - independencia.rs.gov.br\Prefeitura\MSC\parquet', f'{ano}-{mes}.parquet')
writers = [
    # msc_converter.writer.filewriter.ToCsv(destinycsv),
    # msc_converter.writer.filewriter.ToPickle(destinypickle),
    msc_converter.writer.filewriter.ToExcel(destinyexcel),
    msc_converter.writer.filewriter.ToParquet(destinyparquet)
]

# Executa a conversão
app = msc_converter.app.App(logger, reader, writers)
app.run()