import shutil

# caminho dos arquivos .mdf e .ldf
mdf_file = 'C:/Program Files/Microsoft SQL Server/MSSQL15.SQLEXPRESS/MSSQL/DATA/siacRestaurante_Data.mdf'
ldf_file = 'C:/Program Files/Microsoft SQL Server/MSSQL15.SQLEXPRESS/MSSQL/DATA/siacRestaurante_Log.ldf'

# caminho destino da cópia dos arquivos .mdf e .ldf
mdf_backup = 'C:/Backup'
ldf_backup = 'C:/Backup'

try:
    # Fazer cópia dos arquivos .mdf e .ldf
    shutil.copy(mdf_file, mdf_backup)
    shutil.copy(ldf_file, ldf_backup)

    print('Backup realizado com sucesso!')
except Exception as e:
    print(f'Erro ao realizar o backup: {e}')