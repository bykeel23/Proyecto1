from capaLogica.n_Data import NCliente, NProveedor, NProducto
import streamlit as st

class LCliente:
    def __init__(self):
        self._lcliente = NCliente()
        if 'formulariokey' not in st.session_state:
            st.session_state.formulariokey = 0
        if 'cliente_Seleccionado' not in st.session_state:
            st.session_state.cliente_Seleccionado = {}
        self.__construirInterfaz()
    
    def __construirInterfaz(self):
        st.title('Clientes')
        with st.form(f'FormularioClientes {st.session_state.formulariokey}'):
            txtCliente = st.number_input('id_cliente', min_value=0, max_value=500,
                                         value=st.session_state.cliente_Seleccionado.get('id_cliente', 0))
            txtCnombre = st.text_input('nombre', value=st.session_state.cliente_Seleccionado.get('nombre', ''))
            txtCdireccion = st.text_input('direccion', value=st.session_state.cliente_Seleccionado.get('direccion', ''))
            txtCtelefono = st.text_input('telefono', value=st.session_state.cliente_Seleccionado.get('telefono', ''))
            txtCcorreo = st.text_input('correo', value=st.session_state.cliente_Seleccionado.get('correo', ''))
            cliente = {
                'id_cliente': txtCliente,
                'nombre': txtCnombre,
                'direccion': txtCdireccion,
                'telefono': txtCtelefono,
                'correo': txtCcorreo
            }
            if st.session_state.cliente_Seleccionado:
                btnactua = st.form_submit_button('Actualizar', type='primary')
                if btnactua:
                    self.actualizarCliente(cliente)
            else:
                btnguardar = st.form_submit_button('Guardar', type='primary')
                if btnguardar:
                    self.insertarCliente(cliente)
        self.mostrarTodo()
    
    def mostrarTodo(self):
        tablaCliente = self._lcliente.mostrarTodo()
        col1, col2 = st.columns([10, 2])
        with col1:
            clienteSeleccionado = st.dataframe(tablaCliente, selection_mode='single-row', on_select='rerun')
        with col2:
            if clienteSeleccionado.selection.rows:
                indice_cliente = clienteSeleccionado.selection.rows[0]
                cliente_dict = tablaCliente[indice_cliente]
                if st.button('Editar'):
                    st.session_state.cliente_Seleccionado = cliente_dict
                    st.rerun()
                if st.button('Eliminar'):
                    self.eliminarCliente(cliente_dict['id_cliente'])
                    st.toast('Registro eliminado correctamente', duration='short')
                    st.rerun()
    
    def insertarCliente(self, cliente: dict):
        self._lcliente.insertarCliente(cliente)
        st.toast('Registro insertado correctamente', duration='short')
        self.limpiar()

    def actualizarCliente(self, cliente: dict):
        self._lcliente.actualizarCliente(cliente)
        st.toast('Registro actualizado correctamente', duration='short')
        self.limpiar()

    def eliminarCliente(self, id_cliente: int):
        self._lcliente.eliminarCliente(id_cliente)

    def limpiar(self):
        st.session_state.formulariokey += 1
        st.session_state.cliente_Seleccionado = {}
        st.rerun()


class LProducto:
    def __init__(self):
        self._lproducto = NProducto()
        if 'producto_Seleccionado' not in st.session_state:
            st.session_state.producto_Seleccionado = {}
        self.__construirInterfaz()
    
    def __construirInterfaz(self):
        st.title('Productos')
        with st.form('FormularioProductos'):
            txtProducto = st.number_input('id_producto', min_value=0, max_value=200,
                                          value=st.session_state.producto_Seleccionado.get('id_producto', 0))
            txtPnombre = st.text_input('nombre', value=st.session_state.producto_Seleccionado.get('nombre', ''))
            txtPcategoria = st.text_input('categoria', value=st.session_state.producto_Seleccionado.get('categoria', ''))
            txtPprecio = st.number_input('precio', min_value=1, max_value=1000,
                                         value=st.session_state.producto_Seleccionado.get('precio', 1))
            txtPstock = st.number_input('stock', min_value=1, max_value=200,
                                        value=st.session_state.producto_Seleccionado.get('stock', 1))
            producto = {
                'id_producto': txtProducto,
                'nombre': txtPnombre,
                'categoria': txtPcategoria,
                'precio': txtPprecio,
                'stock': txtPstock
            }
            if st.session_state.producto_Seleccionado:
                btnactua = st.form_submit_button('Actualizar', type='primary')
                if btnactua:
                    self.actualizarProducto(producto)
            else:
                btnguardar = st.form_submit_button('Guardar', type='primary')
                if btnguardar:
                    self.insertarProducto(producto)
        self.mostrarTodo()

    def mostrarTodo(self):
        tablaProducto = self._lproducto.mostrarTodo()
        col1, col2 = st.columns([10, 2])
        with col1:
            productoSeleccionado = st.dataframe(tablaProducto, selection_mode='single-row', on_select='rerun')
        with col2:
            if productoSeleccionado.selection.rows:
                indice_producto = productoSeleccionado.selection.rows[0]
                producto_dict = tablaProducto[indice_producto]
                if st.button('Editar'):
                    st.session_state.producto_Seleccionado = producto_dict
                    st.rerun()
                if st.button('Eliminar'):
                    self.eliminarProducto(producto_dict['id_producto'])
                    st.toast('Producto eliminado correctamente', duration='short')
                    st.rerun()
    
    def insertarProducto(self, producto: dict):
        self._lproducto.insertarProducto(producto)

    def actualizarProducto(self, producto: dict):
        self._lproducto.actualizarProducto(producto)

    def eliminarProducto(self, id_producto: int):
        self._lproducto.eliminarProducto(id_producto)


class LProveedor:
    def __init__(self):
        self._lproveedor = NProveedor()
        if 'proveedor_Seleccionado' not in st.session_state:
            st.session_state.proveedor_Seleccionado = {}
        self.__construirInterfaz()
    
    def __construirInterfaz(self):
        st.title('Proveedores')
        with st.form('FormularioProveedor'):
            txtProveedor = st.number_input('id_proveedor', min_value=0, max_value=200,
                                           value=st.session_state.proveedor_Seleccionado.get('id_proveedor', 0))
            txtPnombre = st.text_input('nombre', value=st.session_state.proveedor_Seleccionado.get('nombre', ''))
            txtPcontacto = st.text_input('contacto', value=st.session_state.proveedor_Seleccionado.get('contacto', ''))
            txtdireccion = st.text_input('direccion', value=st.session_state.proveedor_Seleccionado.get('direccion', ''))
            proveedor = {
                'id_proveedor': txtProveedor,
                'nombre': txtPnombre,
                'contacto': txtPcontacto,
                'direccion': txtdireccion
            }
            if st.session_state.proveedor_Seleccionado:
                btnactua = st.form_submit_button('Actualizar', type='primary')
                if btnactua:
                    self.actualizarProveedor(proveedor)
            else:
                btnguardar = st.form_submit_button('Guardar', type='primary')
                if btnguardar:
                    self.insertarProveedor(proveedor)
        self.mostrarTodo()

    def mostrarTodo(self):
        tablaproveedores = self._lproveedor.mostrarTodo()
        col1, col2 = st.columns([10, 2])
        with col1:
            proveedorSeleccionado = st.dataframe(tablaproveedores, selection_mode='single-row', on_select='rerun')
        with col2:
            if proveedorSeleccionado.selection.rows:
                indice_proveedor = proveedorSeleccionado.selection.rows[0]
                proveedor_dict = tablaproveedores[indice_proveedor]
                if st.button('Editar'):
                    st.session_state.proveedor_Seleccionado = proveedor_dict
                    st.rerun()
                if st.button('Eliminar'):
                    self.eliminarProveedor(proveedor_dict['id_proveedor'])
                    st.toast('Proveedor eliminado correctamente', duration='short')
                    st.rerun()
    
    def insertarProveedor(self, proveedor: dict):
        self._lproveedor.insertarProveedor(proveedor)

    def actualizarProveedor(self, proveedor: dict):
        self._lproveedor.actualizarProveedor(proveedor)

    def eliminarProveedor(self, id_proveedor: int):
        self._lproveedor.eliminarProveedor(id_proveedor)