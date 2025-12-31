from capaDatos.d_Data import DCliente, DProducto, DProveedor

class NCliente:
    def __init__(self):
        self.__ncliente = DCliente()

    def mostrarTodo(self):
        return self.__ncliente.mostrarTodo()
    
    def insertarCliente(self, cliente: dict):
        self.__ncliente.insertarCliente(cliente)

    def actualizarCliente(self, cliente: dict):
        self.__ncliente.actualizarCliente(cliente)

    def eliminarCliente(self, id_cliente: int):
        self.__ncliente.eliminarCliente(id_cliente)


class NProducto:
    def __init__(self):
        self.__nproducto = DProducto()

    def mostrarTodo(self):
        return self.__nproducto.mostrarTodo()  
    
    def insertarProducto(self, producto: dict):
        self.__nproducto.insertarProducto(producto)

    def actualizarProducto(self, producto: dict):
        self.__nproducto.actualizarProducto(producto)

    def eliminarProducto(self, id_producto: int):
        self.__nproducto.eliminarProducto(id_producto)


class NProveedor:
    def __init__(self):
        self.__nproveedor = DProveedor()
    
    def mostrarTodo(self):
        return self.__nproveedor.mostrarTodo()
    
    def insertarProveedor(self, proveedor: dict):
        self.__nproveedor.insertarProveedor(proveedor)

    def actualizarProveedor(self, proveedor: dict):
        self.__nproveedor.actualizarProveedor(proveedor)

    def eliminarProveedor(self, id_proveedor: int):
        self.__nproveedor.eliminarProveedor(id_proveedor)