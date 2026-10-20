import json
import requests
from datetime import datetime

def obtener_datos_economicos():
    # Valores de respaldo por defecto en caso de que alguna API falle individualmente
    uf_val = 41162.73
    utm_val = 72151.0
    dolar_val = 987.03
    euro_val = 1099.02
    fuente = "FIndic.cl"

    headers = {'User-Agent': 'Mozilla/5.0'}

    # 1. Obtener UF
    try:
        r = requests.get("https://findic.cl/api/uf", headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            # Extrae el valor más reciente de la serie
            uf_val = float(data["serie"][0]["valor"])
    except Exception as e:
        print(f"Error obteniendo UF: {e}")

    # 2. Obtener UTM
    try:
        r = requests.get("https://findic.cl/api/utm", headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            utm_val = float(data["serie"][0]["valor"])
    except Exception as e:
        print(f"Error obteniendo UTM: {e}")

    # 3. Obtener Dólar
    try:
        r = requests.get("https://findic.cl/api/dolar", headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            dolar_val = float(data["serie"][0]["valor"])
    except Exception as e:
        print(f"Error obteniendo Dólar: {e}")

    # 4. Obtener Euro
    try:
        r = requests.get("https://findic.cl/api/euro", headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            euro_val = float(data["serie"][0]["valor"])
    except Exception as e:
        print(f"Error obteniendo Euro: {e}")

    # Estructura final para tu archivo JSON
    indicadores = {
        "fecha": datetime.now().isoformat(),
        "uf": uf_val,
        "utm": utm_val,
        "dolar": dolar_val,
        "euro": euro_val,
        "origen": fuente
    }

    # Guardado local en el archivo que lee tu web
    with open("indicadores.json", "w", encoding="utf-8") as f:
        json.dump(indicadores, f, ensure_ascii=False, indent=4)
    
    print("¡Archivo indicadores.json actualizado correctamente con los datos de FIndic!")

if __name__ == "__main__":
    obtener_datos_economicos()