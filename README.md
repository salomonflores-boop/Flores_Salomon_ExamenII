# Salomón Flores - Catálogo de Productos y Gestión de Cola

## Descripción breve

Este proyecto es una aplicación desarrollada en Python que integra los conocimientos aprendidos durante las diferentes semanas de la asignatura de programación.

El proyecto comenzó con conceptos de Programación Orientada a Objetos como encapsulación, herencia, composición, abstracción y polimorfismo. Posteriormente se implementó un catálogo de productos utilizando colecciones de Python y validación de datos con Pydantic. También se agregó una interfaz gráfica utilizando Flet y, finalmente, una estructura de datos tipo cola, el patrón de diseño Repository y pruebas unitarias con pytest.

## Objetivo del proyecto

El objetivo principal es desarrollar una aplicación que permita gestionar productos de manera organizada, aplicando diferentes conceptos de programación.

Además, el proyecto busca integrar en una sola aplicación los conocimientos de Programación Orientada a Objetos, colecciones, validación de datos, interfaces gráficas, estructuras de datos, patrones de diseño y testing unitario.

## Principales funcionalidades

### Programación Orientada a Objetos

El proyecto incluye diferentes conceptos de POO:

- Encapsulación mediante atributos privados.
- Herencia mediante las clases `PlacaSamsung` y `PlacaXiaomi`.
- Composición mediante la clase `Tecnico`.
- Abstracción mediante la clase `Cliente`.
- Polimorfismo mediante los diferentes tipos de clientes.

### Catálogo de productos

Para la gestión de productos se implementaron operaciones CRUD:

- Agregar productos.
- Buscar productos.
- Listar productos.
- Actualizar productos.
- Eliminar productos.
- Validar que no existan códigos repetidos.

Para almacenar y organizar la información se utilizaron:

- `list` para almacenar los productos.
- `dict` para relacionar los productos con su código.
- `set` para controlar códigos registrados y evitar duplicados.

### Validación con Pydantic

Se utilizó la librería Pydantic mediante `BaseModel`, `Field` y `field_validator`.

La clase `Producto` valida los datos ingresados antes de agregarlos al catálogo.

Por ejemplo, el precio debe ser mayor que cero y los campos de texto deben cumplir con las condiciones establecidas.

### Interfaz gráfica

La aplicación cuenta con una interfaz gráfica desarrollada utilizando Flet.

Desde la interfaz se pueden realizar las principales operaciones del catálogo mediante botones y campos de entrada.

Entre las opciones disponibles están:

- Agregar.
- Buscar.
- Actualizar.
- Eliminar.
- Listar.
- Agregar producto a la cola.
- Consultar siguiente producto.
- Atender producto.
- Consultar cantidad de productos en la cola.

La información de los productos se muestra mediante una tabla dentro de la aplicación.

### Cola de productos

En la Semana 7 se implementó manualmente una estructura de datos tipo cola mediante la clase `ColaProductos`.

La cola utiliza el principio FIFO:

**First In, First Out**

Esto significa que el primer producto que entra a la cola es el primero que será atendido.

La clase implementa las siguientes operaciones:

- `agregar()`
- `eliminar()`
- `siguiente()`
- `esta_vacia()`
- `cantidad()`

### Patrón Repository

También se implementó el patrón de diseño Repository mediante la clase `ProductoRepository`.

Su función es separar la gestión de los datos de la lógica principal de la aplicación.

El Repository permite realizar operaciones sobre la cola como:

- Guardar productos.
- Eliminar productos.
- Consultar el siguiente producto.
- Verificar si está vacía.
- Consultar la cantidad.
- Listar los productos.

### Persistencia

La aplicación utiliza las estructuras de datos del proyecto para mantener y gestionar la información durante la ejecución.

La organización mediante listas, diccionarios y conjuntos permite manejar los productos de forma estructurada.

### Pruebas unitarias

Para comprobar el funcionamiento del proyecto se creó el archivo `test_main.py`.

Las pruebas fueron realizadas utilizando `pytest`.

Se prueban diferentes funcionalidades como:

- Creación de productos.
- Validación de precios.
- Registro de productos.
- Control de códigos duplicados.
- Agregar elementos a la cola.
- Consultar el siguiente elemento.
- Eliminar elementos.
- Verificar el funcionamiento FIFO.
- Comprobar la cantidad de elementos.
- Funcionamiento del Repository.

## Estructura del proyecto

```text
Salomon-Flores-Proyecto/
│
├── main.py
├── test_main.py
└── README.md
```

### `main.py`

Contiene el programa principal, las clases desarrolladas durante las diferentes semanas, el catálogo de productos, la cola, el Repository y la interfaz gráfica con Flet.

### `test_main.py`

Contiene las pruebas unitarias realizadas con pytest para comprobar el funcionamiento de las diferentes partes del proyecto.

### `README.md`

Contiene la descripción del proyecto y las instrucciones necesarias para ejecutarlo.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.x
- Pydantic
- Flet
- Pytest

## Instalación de librerías

Abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```bash
pip install pydantic
pip install flet
pip install pytest
```

## Instrucciones para ejecutar el proyecto

### 1. Descargar o clonar el repositorio

Abrir el repositorio de GitHub y descargar el proyecto o clonarlo utilizando Git.

### 2. Abrir el proyecto

Abrir la carpeta del proyecto utilizando PyCharm u otro editor compatible con Python.

### 3. Instalar las dependencias

En la terminal ejecutar:

```bash
pip install pydantic flet pytest
```

### 4. Ejecutar la aplicación

Para iniciar la aplicación principal ejecutar:

```bash
python main.py
```

También se puede ejecutar directamente `main.py` desde PyCharm.

### 5. Ejecutar las pruebas

Para ejecutar las pruebas unitarias utilizar:

```bash
python -m pytest -v
```

Esto permite comprobar mediante pytest que las funcionalidades principales del proyecto funcionen correctamente.

## Lenguaje utilizado

**Python**

## Librerías utilizadas

- **Pydantic:** validación y manejo de datos.
- **Flet:** desarrollo de la interfaz gráfica.
- **Pytest:** realización de pruebas unitarias.

## Autor

**Salomón Flores**

Proyecto académico desarrollado para la asignatura de programación.