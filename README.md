# ChatbotFlask
Demo de chatbot web con flask 


# Chatbot con DialoGPT y Flask 🌐

Este proyecto implementa un chatbot utilizando el modelo `DialoGPT-medium` de Hugging Face y Flask como servidor web. La API permite realizar consultas al chatbot y obtener respuestas generadas automáticamente.

## 🚀 Características

- Conversación en lenguaje natural con el modelo `DialoGPT-medium` de Hugging Face
- API RESTful para integrar el chatbot en aplicaciones web o móviles
- Implementado con Flask para un fácil despliegue y escalabilidad

## 📋 Requisitos

- Python 3.7+
- Las siguientes bibliotecas de Python (puedes instalarlas ejecutando el comando):

    ```bash
    pip install transformers torch flask
    ```
## Antes de comenzar...
1. Crea una nueva carpeta para tu proyecto:
    ```bash
    mkdir chatbot
    cd chatbot
    ```
2. Verifica la versión de `pip`
      ```bash
    pip --version
    ```
3. Actualiza `pip`
```bash
  python -m pip install --upgrade pip
```
4. Asegúrate de tener permisos para ejecitar scripts en `PowerShell`
```bash
  Get-ExecutionPolicy
```
5. Cambiar la política de ejecución de scripts a `RemoteSigned`
```bash
  Set-ExecutionPolicy RemoteSigned
```
- Acepta el cambio en la política
```bash
  PS C:\> Set-ExecutionPolicy RemoteSigned
Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the security risks described in the about_Execution_Policies help topic at https://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
```
    
  ## Creación y activación de entorno virtual
Crea el entorno virtual
```bash
  python3 -m venv venv
```
- Activación en `PoweShell`
```bash
  python3 -m venv venv
```
- Activación en `cmd`
```bash
  .\venv\Scripts\Activate.ps1
```
## 💻 Instalar dependencias  
```bash
  pip install Flask transformers torch
```
_verificar que las librerias funcionen bien_

```bash
  py -m pip install torch sympy
  py -m pip show torch sympy
```
El comando `pip install Flask transformers torch` instala las bibliotecas `Flask` (para crear aplicaciones web y APIs), `transformers` (para trabajar con modelos de lenguaje de Hugging Face como DialoGPT), y `torch` (la biblioteca PyTorch necesaria para el procesamiento de redes neuronales y modelos de machine learning) en el entorno de Python actual.

## 📁 Estructura del Proyecto
 ```bash
chatbot/
│
├── app.py                    # Archivo principal de la aplicación Flask
├── knowledge_base.json       # Base de conocimientos en formato JSON
├── requirements.txt          # Archivo de dependencias
├── templates/                # Carpeta para archivos HTML
│   └── index.html            # Archivo HTML principal
└── static/                   # Carpeta para archivos estáticos (CSS, JS, imágenes)
    └── styles.css            # Archivo CSS para estilizar la aplicación
    ```
