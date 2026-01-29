import pandas as pd
import os

DTYPES = {
    'id': 'string',
    'fecha': 'string',
    'año': 'int32',
    'latitud': 'float32',
    'longitud': 'float32'
}

def actulizar_sensores():
    if os.path.exists('data.csv'):
        df_old = pd.read_csv('data.csv', dtype=DTYPES)
    else:
        df_old = pd.DataFrame(columns=DTYPES.keys())

    if not os.path.exists('nuevo.csv'):
        print("No hay novedades.")
        return

    df_new = pd.read_csv('nuevo.csv', dtype=DTYPES)

    df_total = pd.concat([df_old, df_new])

    df_final = df_total.drop_duplicates(subset=['id'], keep='last')

    df_final.to_csv('data.csv', index=False)


if __name__ == '__main__':
    actulizar_sensores()