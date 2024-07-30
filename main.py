import os
from sqlalchemy import create_engine
from config.Servicios import servicios
from rich.console import Console
from to_sql import importar_sql

if __name__ == '__main__':
    cwd = os.getcwd()
    data_dir = r'..\data\\'
    db_conn = os.getenv('DB_CONN')

    engine = create_engine(db_conn)
    console = Console()
    console.print(f'Herramienta de importado V1.1 - Ricardo R.', style='yellow')

    with console.status("[bold green]Importando datos...", spinner='arrow3') as status:
        for serv in servicios:
            try:
                importar_sql(data_dir, serv['file_name'], serv['tabla'], engine)
                console.log(f"{serv['file_name']} - [green]Completado")
            except Exception as e:
                console.log(f"{serv['file_name']} - [red]Error - {e}")

    console.print(f'Presiona ENTER para salir', style='green')
    input()
