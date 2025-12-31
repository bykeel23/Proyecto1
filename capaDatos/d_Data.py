from conexion import ConexionDB

class d_Data:
    def __init__(self, nombre_tabla):
        self._db = ConexionDB().conexionSupabase()
        self._nombretabla = nombre_tabla
    
    def mostrarTodo(self):
        consulta = self._db.table(self._nombretabla).select('*')
        return self.ejecutarConsultas(consulta, 'SELECT')
        
    def ejecutarConsultas(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
                return resultado
            else:
                resultado = consulta.execute()
                return resultado
        except Exception as e:
            raise e
    
class DCliente(d_Data):
    def __init__(self):
        super().__init__('cliente')
    
    def insertarCliente(self, cliente: dict):
        consulta = self._db.table(self._nombretabla).insert(cliente)
        return self.ejecutarConsultas(consulta)

    def actualizarCliente(self, cliente: dict):
        consulta = self._db.table(self._nombretabla).update(cliente).eq('id_cliente', cliente['id_cliente'])
        return self.ejecutarConsultas(consulta)

    def eliminarCliente(self, id_cliente: int):
        consulta = self._db.table(self._nombretabla).delete().eq('id_cliente', id_cliente)
        return self.ejecutarConsultas(consulta)

class DProducto(d_Data):
    def __init__(self):
        super().__init__('producto')
    
    def insertarProducto(self, producto: dict):
        consulta = self._db.table(self._nombretabla).insert(producto)
        return self.ejecutarConsultas(consulta)

    def actualizarProducto(self, producto: dict):
        consulta = self._db.table(self._nombretabla).update(producto).eq('id_producto', producto['id_producto'])
        return self.ejecutarConsultas(consulta)

    def eliminarProducto(self, id_producto: int):
        consulta = self._db.table(self._nombretabla).delete().eq('id_producto', id_producto)
        return self.ejecutarConsultas(consulta)

class DProveedor(d_Data):
    def __init__(self):
        super().__init__('proveedor')
    
    def insertarProveedor(self, proveedor: dict):
        consulta = self._db.table(self._nombretabla).insert(proveedor)
        return self.ejecutarConsultas(consulta)

    def actualizarProveedor(self, proveedor: dict):
        consulta = self._db.table(self._nombretabla).update(proveedor).eq('id_proveedor', proveedor['id_proveedor'])
        return self.ejecutarConsultas(consulta)

    def eliminarProveedor(self, id_proveedor: int):
        consulta = self._db.table(self._nombretabla).delete().eq('id_proveedor', id_proveedor)
        return self.ejecutarConsultas(consulta)