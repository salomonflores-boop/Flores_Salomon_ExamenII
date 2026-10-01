import pytest

from main import (
    Producto,
    CatalogoProductos,
    ColaProductos,
    ProductoRepository
)


# ============================================================
# SEMANA 7 - TESTING UNITARIO CON PYTEST
# ============================================================

def test_crear_producto():
    producto = Producto(
        codigo="P100",
        nombre="Cautín",
        precio=15.50,
        categoria="Herramientas"
    )

    assert producto.codigo == "P100"
    assert producto.nombre == "Cautín"
    assert producto.precio == 15.50
    assert producto.categoria == "Herramientas"


def test_producto_precio_invalido():
    with pytest.raises(ValueError):
        Producto(
            codigo="P101",
            nombre="Cautín",
            precio=-10,
            categoria="Herramientas"
        )


def test_agregar_producto():
    catalogo = CatalogoProductos()

    producto = Producto(
        codigo="P200",
        nombre="Fuente de Poder",
        precio=50,
        categoria="Equipos"
    )

    catalogo.agregar_producto(producto)

    assert len(catalogo.listar_productos()) == 1


def test_codigo_duplicado():
    catalogo = CatalogoProductos()

    producto1 = Producto(
        codigo="P300",
        nombre="Producto 1",
        precio=20,
        categoria="Prueba"
    )

    producto2 = Producto(
        codigo="P300",
        nombre="Producto 2",
        precio=30,
        categoria="Prueba"
    )

    catalogo.agregar_producto(producto1)

    with pytest.raises(ValueError):
        catalogo.agregar_producto(producto2)


def test_cola_vacia():
    cola = ColaProductos()

    assert cola.esta_vacia() is True
    assert cola.cantidad() == 0


def test_agregar_a_cola():
    cola = ColaProductos()

    cola.agregar("Producto A")

    assert cola.esta_vacia() is False
    assert cola.cantidad() == 1


def test_siguiente_elemento():
    cola = ColaProductos()

    cola.agregar("Producto A")
    cola.agregar("Producto B")

    assert cola.siguiente() == "Producto A"


def test_eliminar_elemento():
    cola = ColaProductos()

    cola.agregar("Producto A")
    cola.agregar("Producto B")

    eliminado = cola.eliminar()

    assert eliminado == "Producto A"
    assert cola.cantidad() == 1


def test_comportamiento_fifo():
    cola = ColaProductos()

    cola.agregar("Producto A")
    cola.agregar("Producto B")
    cola.agregar("Producto C")

    primero = cola.eliminar()
    segundo = cola.eliminar()
    tercero = cola.eliminar()

    assert primero == "Producto A"
    assert segundo == "Producto B"
    assert tercero == "Producto C"


def test_eliminar_cola_vacia():
    cola = ColaProductos()

    with pytest.raises(IndexError):
        cola.eliminar()


def test_siguiente_cola_vacia():
    cola = ColaProductos()

    with pytest.raises(IndexError):
        cola.siguiente()


def test_cantidad_cola():
    cola = ColaProductos()

    cola.agregar("Producto A")
    cola.agregar("Producto B")
    cola.agregar("Producto C")

    assert cola.cantidad() == 3


def test_repository_guardar():
    repository = ProductoRepository()

    producto = Producto(
        codigo="P400",
        nombre="Osciloscopio",
        precio=200,
        categoria="Equipos"
    )

    repository.guardar(producto)

    assert repository.cantidad() == 1
    assert repository.siguiente() == producto


def test_repository_eliminar():
    repository = ProductoRepository()

    producto = Producto(
        codigo="P500",
        nombre="Multímetro",
        precio=25,
        categoria="Herramientas"
    )

    repository.guardar(producto)

    resultado = repository.eliminar()

    assert resultado == producto
    assert repository.esta_vacio() is True


def test_repository_fifo():
    repository = ProductoRepository()

    producto1 = Producto(
        codigo="P600",
        nombre="Producto 1",
        precio=10,
        categoria="Prueba"
    )

    producto2 = Producto(
        codigo="P601",
        nombre="Producto 2",
        precio=20,
        categoria="Prueba"
    )

    repository.guardar(producto1)
    repository.guardar(producto2)

    primero = repository.eliminar()

    assert primero.codigo == "P600"
    assert repository.siguiente().codigo == "P601"


def test_repository_listar():
    repository = ProductoRepository()

    producto1 = Producto(
        codigo="P700",
        nombre="Producto 1",
        precio=10,
        categoria="Prueba"
    )

    producto2 = Producto(
        codigo="P701",
        nombre="Producto 2",
        precio=20,
        categoria="Prueba"
    )

    repository.guardar(producto1)
    repository.guardar(producto2)

    productos = repository.listar()

    assert len(productos) == 2
    assert productos[0].codigo == "P700"
    assert productos[1].codigo == "P701"