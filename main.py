import flet as ft
from pydantic import BaseModel, Field, field_validator, ValidationError
from abc import ABC, abstractmethod


# ============================================================
# SEMANA 1 - ENCAPSULACIÓN
# ============================================================

class PlacaCelular:

    def __init__(self, marca, modelo, imei, estado):
        self.__marca = marca
        self.__modelo = modelo
        self.__imei = imei
        self.__estado = estado

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_imei(self):
        return self.__imei

    def set_imei(self, imei):
        self.__imei = imei

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def mostrar_informacion(self):
        print("\n----- INFORMACIÓN DE LA PLACA -----")
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"IMEI: {self.__imei}")
        print(f"Estado: {self.__estado}")


# ============================================================
# SEMANA 2 - HERENCIA
# ============================================================

class PlacaSamsung(PlacaCelular):

    def reparar(self):
        return "Reparación de placa Samsung realizada."


class PlacaXiaomi(PlacaCelular):

    def reparar(self):
        return "Reparación de placa Xiaomi realizada."


# ============================================================
# SEMANA 2 - COMPOSICIÓN
# ============================================================

class Tecnico:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__placa = None

    def asignar_placa(self, placa):
        self.__placa = placa

    def realizar_reparacion(self):
        if self.__placa is not None:
            return self.__placa.reparar()

        return "No hay ninguna placa asignada."


# ============================================================
# SEMANA 3 - ABSTRACCIÓN
# ============================================================

class Cliente(ABC):

    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    @abstractmethod
    def calcular_descuento(self, monto):
        pass


# ============================================================
# SEMANA 3 - POLIMORFISMO
# ============================================================

class ClienteMayorista(Cliente):

    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.__porcentaje_descuento = 0.15

    def calcular_descuento(self, monto):
        return monto * self.__porcentaje_descuento


class ClienteMinorista(Cliente):

    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.__porcentaje_descuento = 0.05

    def calcular_descuento(self, monto):
        return monto * self.__porcentaje_descuento


# ============================================================
# SEMANA 5 - MODELO PRODUCTO CON PYDANTIC
# ============================================================

class Producto(BaseModel):

    codigo: str = Field(min_length=2, max_length=20)
    nombre: str = Field(min_length=2, max_length=50)
    precio: float = Field(gt=0)
    categoria: str = Field(min_length=2, max_length=40)

    @field_validator("codigo")
    @classmethod
    def validar_codigo(cls, valor):

        valor = valor.strip().upper()

        if not valor:
            raise ValueError("El código no puede estar vacío.")

        return valor

    @field_validator("nombre", "categoria")
    @classmethod
    def validar_texto(cls, valor):

        valor = valor.strip()

        if not valor:
            raise ValueError("El campo no puede estar vacío.")

        return valor


# ============================================================
# SEMANA 5 - CATÁLOGO
# ============================================================

class CatalogoProductos:

    def __init__(self):

        self.productos = []
        self.productos_por_codigo = {}
        self.codigos_registrados = set()

    def agregar_producto(self, producto):

        if producto.codigo in self.codigos_registrados:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto
        self.codigos_registrados.add(producto.codigo)

    def buscar_producto(self, codigo):

        codigo = codigo.strip().upper()

        return self.productos_por_codigo.get(codigo)

    def listar_productos(self):

        return self.productos

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio,
        categoria
    ):

        codigo = codigo.strip().upper()

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        producto_actualizado = Producto(
            codigo=codigo,
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )

        posicion = self.productos.index(producto)

        self.productos[posicion] = producto_actualizado
        self.productos_por_codigo[codigo] = producto_actualizado

    def eliminar_producto(self, codigo):

        codigo = codigo.strip().upper()

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        self.productos.remove(producto)
        del self.productos_por_codigo[codigo]
        self.codigos_registrados.remove(codigo)


# ============================================================
# DATOS INICIALES
# ============================================================

catalogo = CatalogoProductos()


def cargar_datos_prueba():

    productos = [

        Producto(
            codigo="P001",
            nombre="Multímetro Digital",
            precio=25.50,
            categoria="Herramientas"
        ),

        Producto(
            codigo="P002",
            nombre="Estación de Soldadura",
            precio=75.00,
            categoria="Herramientas"
        ),

        Producto(
            codigo="P003",
            nombre="Microscopio Digital",
            precio=120.00,
            categoria="Equipos"
        )
    ]

    for producto in productos:
        catalogo.agregar_producto(producto)


cargar_datos_prueba()


# ============================================================
# SEMANA 7 - COLA
# ============================================================

class ColaProductos:

    def __init__(self):
        self.__elementos = []

    def agregar(self, elemento):

        self.__elementos.append(elemento)

    def eliminar(self):

        if self.esta_vacia():
            raise IndexError(
                "No se puede eliminar. La cola está vacía."
            )

        return self.__elementos.pop(0)

    def siguiente(self):

        if self.esta_vacia():
            raise IndexError(
                "La cola está vacía."
            )

        return self.__elementos[0]

    def esta_vacia(self):

        return len(self.__elementos) == 0

    def cantidad(self):

        return len(self.__elementos)

    def obtener_elementos(self):

        return self.__elementos.copy()


# ============================================================
# SEMANA 7 - REPOSITORY
# ============================================================

class ProductoRepository:

    def __init__(self):

        self.__cola = ColaProductos()

    def guardar(self, producto):

        self.__cola.agregar(producto)

    def eliminar(self):

        return self.__cola.eliminar()

    def siguiente(self):

        return self.__cola.siguiente()

    def esta_vacio(self):

        return self.__cola.esta_vacia()

    def cantidad(self):

        return self.__cola.cantidad()

    def listar(self):

        return self.__cola.obtener_elementos()


# ============================================================
# SEMANA 7 - COLA DE ATENCIÓN
# ============================================================

cola_productos = ProductoRepository()


# ============================================================
# SEMANA 6 - INTERFAZ GRÁFICA CON FLET
# ============================================================

def main(page: ft.Page):

    page.title = "Catálogo de Productos - Salomón Flores"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    codigo = ft.TextField(
        label="Código",
        hint_text="Ejemplo: P004"
    )

    nombre = ft.TextField(
        label="Nombre",
        hint_text="Nombre del producto"
    )

    precio = ft.TextField(
        label="Precio",
        hint_text="Ejemplo: 25.50"
    )

    categoria = ft.TextField(
        label="Categoría",
        hint_text="Ejemplo: Herramientas"
    )

    mensaje = ft.Text()

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Código")),
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Precio")),
            ft.DataColumn(label=ft.Text("Categoría")),
        ],
        rows=[]
    )

    tabla_cola = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Posición")),
            ft.DataColumn(label=ft.Text("Código")),
            ft.DataColumn(label=ft.Text("Producto")),
        ],
        rows=[]
    )

    def limpiar_campos():

        codigo.value = ""
        nombre.value = ""
        precio.value = ""
        categoria.value = ""

    def actualizar_tabla():

        tabla.rows.clear()

        for producto in catalogo.listar_productos():

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(producto.codigo)
                        ),
                        ft.DataCell(
                            ft.Text(producto.nombre)
                        ),
                        ft.DataCell(
                            ft.Text(
                                f"${producto.precio:.2f}"
                            )
                        ),
                        ft.DataCell(
                            ft.Text(producto.categoria)
                        ),
                    ]
                )
            )

        tabla.update()

    def actualizar_tabla_cola():

        tabla_cola.rows.clear()

        elementos = cola_productos.listar()

        for posicion, producto in enumerate(
            elementos,
            start=1
        ):

            tabla_cola.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(str(posicion))
                        ),
                        ft.DataCell(
                            ft.Text(producto.codigo)
                        ),
                        ft.DataCell(
                            ft.Text(producto.nombre)
                        ),
                    ]
                )
            )

        tabla_cola.update()

    def mostrar_mensaje(texto, error=False):

        mensaje.value = texto

        if error:
            mensaje.color = ft.Colors.RED
        else:
            mensaje.color = ft.Colors.GREEN

        mensaje.update()

    def agregar_click(e):

        try:

            if not codigo.value.strip():
                raise ValueError(
                    "Debe ingresar un código."
                )

            if not nombre.value.strip():
                raise ValueError(
                    "Debe ingresar un nombre."
                )

            if not precio.value.strip():
                raise ValueError(
                    "Debe ingresar un precio."
                )

            if not categoria.value.strip():
                raise ValueError(
                    "Debe ingresar una categoría."
                )

            try:

                precio_numero = float(precio.value)

            except ValueError:

                raise ValueError(
                    "El precio debe ser un número."
                )

            producto = Producto(
                codigo=codigo.value,
                nombre=nombre.value,
                precio=precio_numero,
                categoria=categoria.value
            )

            catalogo.agregar_producto(producto)

            actualizar_tabla()

            mostrar_mensaje(
                "Producto agregado correctamente."
            )

            limpiar_campos()

            page.update()

        except ValidationError as error:

            mostrar_mensaje(
                "Error de validación: revise los datos.",
                True
            )

            print(error)

        except ValueError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def buscar_click(e):

        try:

            codigo_busqueda = codigo.value.strip()

            if not codigo_busqueda:

                raise ValueError(
                    "Ingrese un código para buscar."
                )

            producto = catalogo.buscar_producto(
                codigo_busqueda
            )

            if producto is None:

                mostrar_mensaje(
                    "Producto no encontrado.",
                    True
                )

                return

            nombre.value = producto.nombre
            precio.value = str(producto.precio)
            categoria.value = producto.categoria

            mostrar_mensaje(
                "Producto encontrado correctamente."
            )

            page.update()

        except ValueError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def actualizar_click(e):

        try:

            if not codigo.value.strip():

                raise ValueError(
                    "Ingrese el código del producto."
                )

            try:

                precio_numero = float(precio.value)

            except ValueError:

                raise ValueError(
                    "El precio debe ser un número."
                )

            catalogo.actualizar_producto(
                codigo.value,
                nombre.value,
                precio_numero,
                categoria.value
            )

            actualizar_tabla()

            mostrar_mensaje(
                "Producto actualizado correctamente."
            )

            limpiar_campos()

            page.update()

        except ValidationError as error:

            mostrar_mensaje(
                "Los datos ingresados no son válidos.",
                True
            )

            print(error)

        except ValueError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def eliminar_click(e):

        try:

            codigo_eliminar = codigo.value.strip()

            if not codigo_eliminar:

                raise ValueError(
                    "Ingrese el código del producto."
                )

            catalogo.eliminar_producto(
                codigo_eliminar
            )

            actualizar_tabla()

            mostrar_mensaje(
                "Producto eliminado correctamente."
            )

            limpiar_campos()

            page.update()

        except ValueError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def listar_click(e):

        actualizar_tabla()

        mostrar_mensaje(
            "Catálogo actualizado correctamente."
        )

    def agregar_cola_click(e):

        try:

            codigo_cola = codigo.value.strip()

            if not codigo_cola:

                raise ValueError(
                    "Ingrese el código del producto."
                )

            producto = catalogo.buscar_producto(
                codigo_cola
            )

            if producto is None:

                raise ValueError(
                    "El producto no existe en el catálogo."
                )

            cola_productos.guardar(producto)

            actualizar_tabla_cola()

            mostrar_mensaje(
                f"{producto.nombre} agregado a la cola."
            )

            page.update()

        except ValueError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def siguiente_cola_click(e):

        try:

            producto = cola_productos.siguiente()

            mostrar_mensaje(
                f"Siguiente producto: "
                f"{producto.codigo} - {producto.nombre}"
            )

        except IndexError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def atender_cola_click(e):

        try:

            producto = cola_productos.eliminar()

            actualizar_tabla_cola()

            mostrar_mensaje(
                f"Producto atendido: "
                f"{producto.codigo} - {producto.nombre}"
            )

            page.update()

        except IndexError as error:

            mostrar_mensaje(
                str(error),
                True
            )

    def cantidad_cola_click(e):

        cantidad = cola_productos.cantidad()

        mostrar_mensaje(
            f"Cantidad de productos en la cola: {cantidad}"
        )

    botones = ft.Row(
        controls=[
            ft.Button(
                content="Agregar",
                on_click=agregar_click
            ),
            ft.Button(
                content="Buscar",
                on_click=buscar_click
            ),
            ft.Button(
                content="Actualizar",
                on_click=actualizar_click
            ),
            ft.Button(
                content="Eliminar",
                on_click=eliminar_click
            ),
            ft.Button(
                content="Listar",
                on_click=listar_click
            ),
        ],
        wrap=True
    )

    botones_cola = ft.Row(
        controls=[
            ft.Button(
                content="Agregar a Cola",
                on_click=agregar_cola_click
            ),
            ft.Button(
                content="Siguiente",
                on_click=siguiente_cola_click
            ),
            ft.Button(
                content="Atender",
                on_click=atender_cola_click
            ),
            ft.Button(
                content="Cantidad",
                on_click=cantidad_cola_click
            ),
        ],
        wrap=True
    )

    page.add(

        ft.Text(
            "CATÁLOGO DE PRODUCTOS",
            size=28,
            weight=ft.FontWeight.BOLD
        ),

        ft.Text(
            "Semanas 5, 6 y 7 - Pydantic, "
            "interfaz gráfica, eventos, cola y testing",
            size=16
        ),

        ft.Divider(),

        codigo,
        nombre,
        precio,
        categoria,

        botones,

        ft.Divider(),

        mensaje,

        tabla,

        ft.Divider(),

        ft.Text(
            "SEMANA 7 - COLA DE ATENCIÓN",
            size=22,
            weight=ft.FontWeight.BOLD
        ),

        ft.Text(
            "Los productos se atienden en orden FIFO "
            "(primero en entrar, primero en salir)."
        ),

        botones_cola,

        tabla_cola
    )

    actualizar_tabla()
    actualizar_tabla_cola()


if __name__ == "__main__":
    ft.run(main)