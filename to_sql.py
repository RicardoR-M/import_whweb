import pandas as pd

from sqlalchemy.types import VARCHAR


def importar_sql(folder, file_name, tbl_name, engine):
    converters = {'DNI_USUARIO': str, 'DNI_AGENTE': str, 'ID_GESTION': str, 'NUMERO_LLAMANTE': str}

    with open(folder + file_name, 'r', encoding='latin-1') as doc:
        tabla = doc.read()
        df = pd.read_html(tabla, flavor='bs4', converters=converters)[0]

    df.to_sql(tbl_name, con=engine, if_exists='replace', index=False, dtype={col_name: VARCHAR for col_name in df})
