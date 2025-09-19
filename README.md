# 📍 Localizador de Números Telefónicos - Geolocalización

## 📖 Introducción

Este proyecto es una herramienta de **geolocalización de números telefónicos** desarrollada en Python. Permite obtener información de ubicación a partir de un número de teléfono utilizando APIs de geocodificación y la librería `phonenumbers`.

**⚠️ Nota importante**: Esta herramienta se ha desarrollado únicamente con fines educativos y de investigación legítima. El uso debe cumplir siempre con las leyes locales de privacidad y protección de datos. 

**🔐 Ética de prueba**: Todas las pruebas realizadas durante el desarrollo utilizaron **números de ejemplo públicos y permitidos**, específicamente diseñados para testing (como el número +12065550100, que es un número de prueba estándar). En ningún caso se utilizaron números personales reales sin autorización explícita.

## 🎯 Funcionalidades

- 🔍 **Validación de números** telefónicos internacionales
- 🌍 **Geolocalización aproximada** basada en el prefijo del número
- 🕐 **Detección de zona horaria** asociada al número
- 📍 **Mapa interactivo** con la ubicación estimada
- 📞 **Identificación de compañía** telefónica (cuando está disponible)

## 📋 Requisitos del Sistema

- **Sistema Operativo**: Kali Linux o cualquier distribución Linux
- **Python**: Versión 3.6 o superior
- **Memoria**: Mínimo 512MB RAM
- **Espacio**: 100MB de espacio libre
- **Conexión a Internet**: Para consultas a la API de geocodificación

## 🚀 Instalación Rápida

### Script de Configuración Automática

El proyecto incluye un script de setup que automatiza toda la instalación:

```bash
# Descargar el script de instalación
chmod +x setup_locate_number.sh
sudo ./setup_locate_number.sh
```

**¿Qué hace el script?**
1. ✅ Actualiza los repositorios del sistema
2. ✅ Instala Python3, pip y virtualenv
3. ✅ Crea un entorno virtual aislado
4. ✅ Instala todas las dependencias necesarias
5. ✅ Configura el ambiente para su uso inmediato

![Configuración del Entorno](media/abriendo-el-archivo.png)
*Estructura de archivos del proyecto después de la instalación*

## 🔧 Configuración Manual

Si prefieres realizar la instalación manual:

```bash
# Instalar dependencias del sistema
sudo apt update && sudo apt install -y python3 python3-pip python3-venv

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
pip install --upgrade pip
pip install phonenumbers folium opencage
```

## 🔑 Obtención de API Key

Para utilizar la funcionalidad de geocodificación, necesitas una API key de OpenCage:

1. **Registrarse en OpenCage**: Visita [opencagedata.com](https://opencagedata.com/)
2. **Obtener API key gratuita**: El plan free permite 2500 consultas diarias
3. **Configurar la clave**: Reemplaza la API key en el archivo `geonumber.py`

![Registro API](media/obtener-el-api.png)
*Página de registro para obtener la API key de OpenCage*

![API Configurada](media/api-conseguida.png)
*Documentación de la API de OpenCage con la clave configurada*

## 🎯 Uso de la Herramienta

### Ejecución Básica
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar el localizador
python3 geonumber.py
```

### Ejemplo de Uso
```
Introduce el número en formato internacional (ejemplo: +34123456789).
Número: +12065550100

--- Resultado ---
Número: +12065550100
Zonas: ('America/Los_Angeles',)
Geo description: Washington State
Compañía: 
Lat,Lng: 47.2868352 -120.212613
Mapa guardado en: myLocation.html
```

![Ejecución del Programa](media/escaneo-del-movil.png)
*Ejemplo de ejecución mostrando la geolocalización de un número*

## 📊 Resultados y Output

### Archivos Generados
- **`myLocation.html`**: Mapa interactivo con la ubicación estimada
- **Salida por consola**: Información detallada del número analizado

### Información Obtenida
- 📞 **Número validado** en formato internacional
- 🌍 **Descripción geográfica** del área del número
- 🕐 **Zonas horarias** asociadas
- 📍 **Coordenadas GPS** (latitud y longitud)
- 🏢 **Compañía telefónica** (cuando está disponible)

![Mapa Generado](media/localizacion.png)
*Mapa interactivo generado con la ubicación estimada*

## ⚠️ Limitaciones y Consideraciones

### Precisión de la Geolocalización
- La ubicación es **aproximada** basada en el prefijo del número
- **No proporciona ubicación exacta** del dispositivo
- La precisión varía según el país y la compañía telefónica

### Aspectos Legales
- 🔒 **Solo para uso educativo** y de investigación autorizada
- 📝 **Cumplimiento de leyes** de protección de datos requerido
- 👤 **Respeto de la privacidad** es fundamental

## 🛡️ Medidas de Seguridad

### Entorno Aislado
El uso de virtualenv garantiza que las dependencias no afecten al sistema principal

### Gestión de API Keys
- Las claves se almacenan en el código (mejorable para producción)
- Se recomienda usar variables de entorno para entornos reales

### Limitación de Uso
La herramienta incluye validaciones para prevenir uso malintencionado

## 🔧 Personalización y Extensión

### Modificar la API Key
Edita el archivo `geonumber.py` y reemplaza:
```python
OPENCAGE_KEY = "tu_api_key_aqui"
```

### Añadir Nuevas Funcionalidades
La estructura modular permite fácil extensión para:
- ✅ Soporte de más APIs de geocodificación
- ✅ Exportación a diferentes formatos
- ✅ Integración con bases de datos
- ✅ Análisis de múltiples números

## 🐛 Solución de Problemas

### Error: API Key no configurada
```bash
ERROR: No has configurado la API key de OpenCage.
```
**Solución**: Obtener y configurar una API key válida de OpenCage

### Error: Número inválido
**Solución**: Usar formato internacional correcto (+34XXXXXXXXX)

### Error: Sin conexión a internet
**Solución**: Verificar la conexión para consultas a la API

## 📝 Ejemplos Prácticos

### Caso de Uso 1: Validación de números
```bash
python3 geonumber.py
# Introduce: +34600000000
```

### Caso de Uso 2: Investigación legítima
```bash
# Para números reportados en phishing
python3 geonumber.py
# Introduce: +12345678900
```

## 🎓 Aplicaciones Educativas

- **Estudios de seguridad**: Análisis de técnicas OSINT
- **Investigación forense**: Trazabilidad de comunicaciones
- **Desarrollo Python**: Ejemplo de integración de APIs
- **Geolocalización**: Understanding de tecnologías LBS

## 📞 Soporte y Contribuciones

### Reportar Issues
Si encuentras algún problema, por favor:
1. Verifica que la API key esté correctamente configurada
2. Confirma que el número tenga formato internacional
3. Revisa que tengas conexión a internet

### Mejoras Futuras
- [ ] Soporte para múltiples APIs de geocodificación
- [ ] Interfaz gráfica de usuario
- [ ] Exportación a formatos estándar (KML, CSV)
- [ ] Análisis por lotes de números

## 📚 Recursos Adicionales

### Documentación Oficial
- [phonenumbers Python library](https://github.com/daviddrysdale/python-phonenumbers)
- [OpenCage Geocoding API](https://opencagedata.com/api)
- [Folium Maps](https://python-visualization.github.io/folium/)

### Herramientas Relacionadas
- **Google's libphonenumber**: Biblioteca original de Google
- **PhoneInfoga**: Herramienta avanzada de OSINT
- **Truecaller**: Servicio de identificación de llamadas

---

**⚖️ Disclaimer Legal**: Esta herramienta está diseñada únicamente para fines educativos y de investigación legítima. El usuario es responsable de cumplir con todas las leyes locales y regulaciones de privacidad. No me hago responsable del uso indebido de esta software.

**🔐 Ética de Uso**: Siempre obtén el consentimiento apropiado antes de realizar cualquier tipo de análisis o investigación con números telefónicos.
