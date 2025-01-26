# Instrucciones para Configurar el Proyecto

## 1. Crear un Entorno Virtual

Para crear un entorno virtual, ejecuta el siguiente comando:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` que contendrá el entorno virtual.

---

## 2. Activar el Entorno Virtual

### En Windows:
```bash
venv\Scripts\activate
```

### En macOS/Linux:
```bash
source venv/bin/activate
```

Una vez activado, verás el nombre del entorno virtual (`venv`) en tu terminal.

---

## 3. Instalar Dependencias

Instala las dependencias del proyecto utilizando `pip` y el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 4. Configurar la Base de Datos

Asegúrate de tener configurada la base de datos en `settings.py`. Luego, ejecuta las migraciones:

```bash
python manage.py migrate
```

---

## 5. Variables de entorno

Recuerda añadir a tu archivo .env las siguientes variables:

```bash
BACKEND_URL = ""
ANTHROPIC_API_KEY = ""
```

---

## 6. Ejecutar el Servidor de Desarrollo

Para iniciar el servidor de desarrollo, usa el siguiente comando:

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.

---

## 7. Ejecutar interfaz de chat

Para interacturar con el chatbot, ejecuta el siguiente comando:

```bash
python ./view/chat_view.py
```

El servidor estará disponible en `http://127.0.0.1:7860/`.

---
