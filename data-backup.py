import shutil
import win32serviceutil

service_name = 'MSSQL$SQLEXPRESS'

# parar o serviço sql server (SQLEXPRESS)
try:
    win32serviceutil.StopService(service_name)
    print(f'Serviço SQL Server ({service_name}) parado com sucesso!')
except Exception as e:
    print(f'Ocorreu um erro ao interromper o serviço SQL Server ({service_name}): {str(e)}')

# caminho dos arquivos .mdf e .ldf
mdf_file = 'C:/Program Files/Microsoft SQL Server/MSSQL15.SQLEXPRESS/MSSQL/DATA/siacRestaurante_Data.mdf'
ldf_file = 'C:/Program Files/Microsoft SQL Server/MSSQL15.SQLEXPRESS/MSSQL/DATA/siacRestaurante_Log.ldf'

# caminho destino da cópia dos arquivos .mdf e .ldf
mdf_backup = 'C:/Backup'
ldf_backup = 'C:/Backup'

try:
    # fazer cópia dos arquivos .mdf e .ldf
    shutil.copy(mdf_file, mdf_backup)
    shutil.copy(ldf_file, ldf_backup)

    print('Backup realizado com sucesso!')
except Exception as e:
    print(f'Erro ao realizar o backup: {e}')

# iniciar o serviço sql server (SQLEXPRESS)
try:
    win32serviceutil.StartService(service_name)
    print(f'Serviço SQL Server ({service_name}) foi iniciado novamente com sucesso.')
except Exception as e:
    print(f'Ocorreu um erro ao iniciar o serviço SQL Server ({service_name}): {str(e)}')