#!/usr/bin/env python3
# locate_number.py
# Pide el número por consola, valida y genera myLocation.html

import sys
import phonenumbers
from phonenumbers import geocoder as ph_geocoder
from phonenumbers import timezone as ph_timezone
from phonenumbers import carrier as ph_carrier
import folium
from opencage.geocoder import OpenCageGeocode

# --- API key fija ---
OPENCAGE_KEY = "..............."  # <--- reemplaza con tu API key real

if not OPENCAGE_KEY or OPENCAGE_KEY.strip() == "":
    print("ERROR: No has configurado la API key de OpenCage.")
    sys.exit(1)

def pedir_numero():
    """Pide número al usuario y devuelve el string en crudo."""
    print("Introduce el número en formato internacional (ejemplo: +34123456789).")
    num = input("Número: ").strip()
    return num

def parsear_numero(num_raw):
    """Intenta parsear y validar el número. Lanza NumberParseException si falla."""
    return phonenumbers.parse(num_raw)

def main():
    num_raw = pedir_numero()
    if not num_raw:
        print("No ingresaste ningún número. Saliendo.")
        return

    try:
        numero = parsear_numero(num_raw)
    except phonenumbers.NumberParseException as e:
        print("Número inválido:", e)
        return

    # Zona horaria(s), descripción y carrier
    zonas = ph_timezone.time_zones_for_number(numero)
    geo_desc = ph_geocoder.description_for_number(numero, 'en')
    carrier_name = ph_carrier.name_for_number(numero, 'en')

    # Geocoding con OpenCage
    geocoder = OpenCageGeocode(OPENCAGE_KEY)
    query = str(geo_desc) if geo_desc else phonenumbers.region_code_for_number(numero) or ''
    results = None

    if query:
        try:
            results = geocoder.geocode(query, limit=3)
        except Exception as e:
            print("Error llamando a OpenCage:", e)
            results = None

    if not results:
        print("No se pudo geocodificar la ubicación:", repr(query))
        print("Número:", num_raw, "Zonas:", zonas, "Carrier:", carrier_name)
        return

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    # Crear mapa con folium
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=geo_desc or query).add_to(myMap)

    out_file = "myLocation.html"
    myMap.save(out_file)

    # Salida
    print("\n--- Resultado ---")
    print("Número:", num_raw)
    print("Zonas:", zonas)
    print("Geo description:", geo_desc)
    print("Compañía:", carrier_name)
    print("Lat,Lng:", lat, lng)
    print("Mapa guardado en:", out_file)
    print("-----------------\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Saliendo.")
        sys.exit(0)
