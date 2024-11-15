DetectorPhishingCorreos
Descripción
La Phishing Detector Extension es una extensión de navegador diseñada para ayudar a detectar correos electrónicos sospechosos de phishing. Utilizando un backend en Flask, la extensión realiza análisis en tiempo real sobre el contenido del correo electrónico para determinar si es un posible intento de fraude.

Esta herramienta está orientada a prevenir el acceso a sitios fraudulentos y ayudar a los usuarios a proteger su información personal y financiera.

Características
Detección de phishing en correos electrónicos: Analiza el contenido del correo electrónico para identificar patrones sospechosos de phishing.
Interfaz simple y directa: La extensión ofrece una forma rápida y sencilla de verificar la seguridad de un correo electrónico.
Backend con Flask: El servidor de análisis funciona en el backend utilizando Flask para procesar las solicitudes de la extensión.
Requisitos
Navegador: Google Chrome (o cualquier otro navegador que permita instalar extensiones cargadas manualmente).
Python 3.12+: Necesario para ejecutar el servidor backend en Flask.

Dependencias:
Flask
Flask-CORS


python app.py
El servidor Flask debería estar ejecutándose en http://localhost:5000. Asegúrate de que el servidor esté corriendo mientras usas la extensión.

Uso
Una vez que la extensión esté cargada en el navegador, podrias copiar a la extensión el contenido del correo.
La extensión te informará si el correo electrónico es sospechoso de phishing o no.


Estructura del Proyecto
├── /static                # Archivos estáticos 
├── /templates             # Plantillas HTML
├── app.py                 # Servidor Flask que procesa las solicitudes
├── manifest.json          # Archivo de configuración de la extensión
├── background.js          # Lógica de fondo de la extensión
├── popup.html             
└── content_script.js      
