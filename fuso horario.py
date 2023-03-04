import datetime
import pytz
UTC = pytz.utc 
POR = pytz.timezone('Portugal') 
SPO = pytz.timezone('America/Sao_Paulo') 
agora = datetime.datetime.now(SPO)
print('Data e Hora Atual', agora)
print('Dia Atual    ', agora.day)
print('Mês Atual    ', agora.month)
print('Ano Atual    ', agora.year)
print('Hora Atual   ', agora.hour)
print('Minuto Atual ', agora.minute)
print('Segundo Atual ', agora.secon