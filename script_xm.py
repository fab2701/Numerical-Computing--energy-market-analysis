from pydataxm import pydataxm
import pandas as pd
import datetime

objeto_xm = pydataxm.ReadDB()

try:
    print("Extrayendo precios de bolsa de XM...")
    
    # Firma con argumentos posicionales exactos: coleccion, metrica, fecha_inicio, fecha_fin
    df_precio = objeto_xm.request_data(
        "PrecBolsNaci",                 # coleccion / metrica
        "Sistema",                      # entidad
        datetime.date(2024, 1, 1),      # fecha_inicio
        datetime.date(2024, 1, 31)      # fecha_fin
    )

    print("\n¡DESCARGA EXITOSA!")
    print(df_precio.head())

    # Guardar archivo CSV localmente
    df_precio.to_csv("datos_xm_2024.csv", index=False)
    print("\n-> Archivo 'datos_xm_2024.csv' guardado exitosamente en tu PC.")

except Exception as e:
    print(f"Error durante la extracción: {e}")