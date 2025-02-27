import os
import weatherapi
from weatherapi .rest import ApiException

# Aquí se consulta la api del clima
# Tenemos que pasarle la clave api proporcionada por weatherapi
configuration = weatherapi.Configuration()
configuration.api_key['key'] = os.environ.get('weatherapi')

# Crear instancia de la api de clima
api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))

def clima_actual(ciudad):
    try:
        respuesta_api = api_instance.realtime_weather(ciudad, lang="es")

        # Convertir el objeto a diccionario si es necesario
        datos_clima = respuesta_api.to_dict() if hasattr(respuesta_api, "to_dict") else respuesta_api

        # Acceder directamente a los valores
        return f"""
        El clima en {datos_clima['location']['country']} es {datos_clima['current']['condition']['text']} y la temperatura es de {datos_clima['current']['temp_c']} grados centígrados."""
    except ApiException as e:
        print(f"""Ha ocurrido un error con la API de clima:
        {e}""")
        return None


