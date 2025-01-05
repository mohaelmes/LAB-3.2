
## Requisitos

Para ejecutar este proyecto en tu máquina, necesitas instalar las siguientes dependencias:

1. Python 3.7 o superior
2. Flask
3. SQLite
4. Requests
5. pytest

Puedes instalar todas las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt

```

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina:

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local y accede al directorio del proyecto


```
git clone https://github.com/usuario/rest-api-python-sqlite.git
cd rest-api-python-sqlite
```


### Paso 2: Crear un entorno virtual (opcional pero recomendado)

Crea un entorno virtual para evitar conflictos entre dependencias:
```
python -m venv venv
```
Activa el entorno virtual:

- **En Windows**:
```
venv\Scripts\activate
```

- **En macOS/Linux**:
```
source venv/bin/activate
```

### Paso 3: Instalar las dependencias

Instala todas las dependencias necesarias desde el archivo `requirements.txt`:
```
pip install -r requirements.txt
```

### Paso 4: Ejecutar la API

Ejecuta la API usando el siguiente comando:

```
python app.py

```

El servidor estará disponible en la siguiente dirección:

http://127.0.0.1:5000

Puedes utilizar herramientas como **Postman**, **Insomnia**, o simplemente tu navegador para probar las diferentes rutas de la API.

---

## Uso

El proyecto proporciona una API REST con las siguientes rutas básicas para realizar operaciones CRUD sobre la base de datos SQLite:

1. **GET** `/items` - Obtener todos los elementos.
2. **GET** `/items/<id>` - Obtener un elemento específico.
3. **POST** `/items` - Crear un nuevo elemento.
   - Cuerpo del JSON esperado:
     ```json
     {
       "name": "Nombre del ítem",
       "description": "Descripción del ítem"
     }
     ```
4. **PUT** `/items/<id>` - Actualizar un elemento existente.
   - Cuerpo del JSON esperado:
     ```json
     {
       "name": "Nombre actualizado",
       "description": "Descripción actualizada"
     }
     ```
5. **DELETE** `/items/<id>` - Eliminar un elemento.

Prueba las rutas utilizando los métodos HTTP correspondientes.

---

## Pruebas

El proyecto incluye diferentes tipos de pruebas. Para ejecutarlas, asegúrate de estar en el entorno del proyecto y de que las dependencias necesarias están instaladas. Luego ejecuta los siguientes comandos según el tipo de prueba:

Asegúrate de cambiar de directorio al de tests/
```
cd tests
```

### Pruebas unitarias e integradas

Para verificar la funcionalidad de los métodos y las rutas de la API:

```
pytest tests/test_api.py
```

### Pruebas de seguridad

Para comprobar que la API no es vulnerable a ciertos ataques:
```
pytest tests/test_security.py
```

### Pruebas de rendimiento

Para evaluar la capacidad de la API bajo carga:
```
pytest tests/test_performance.py
```

Los resultados se mostrarán directamente en la terminal.

También podemos usar pytest general (desde la raíz del proyecto):


![image](https://github.com/user-attachments/assets/f79695ba-61a5-42f1-a455-3d38480efe5c)
