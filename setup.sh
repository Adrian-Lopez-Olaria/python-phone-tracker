#!/bin/bash
# setup_locate_number.sh
# Script para preparar entorno en Kali Linux para locate_number.py

set -e  # parar si hay errores

echo "[*] Actualizando repositorios..."
sudo apt update -y

echo "[*] Instalando Python3, pip y venv..."
sudo apt install -y python3 python3-pip python3-venv

echo "[*] Creando entorno virtual..."
python3 -m venv venv

echo "[*] Activando entorno virtual..."
source venv/bin/activate

echo "[*] Instalando dependencias (phonenumbers, folium, opencage)..."
pip install --upgrade pip
pip install phonenumbers folium opencage

echo ""
echo "[✓] Entorno listo."
echo "Para activarlo en futuras sesiones usa:"
echo "   source venv/bin/activate"
