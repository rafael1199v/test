from .data import cursor

class Credenciales():
    def __init__(self, id: int, nombre_usuario: str, correo: str, contrasenha: str) -> None:
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasenha = contrasenha


    def get_nombre(self) -> str:
        return self.nombre_usuario
    
    def get_correo(self) -> str:
        return self.correo
    
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre_usuario = nuevo_nombre

    def set_correo(self, nuevo_correo: str) -> None:
        self.correo = nuevo_correo


    def get_credenciales(correo: str, contrasenha: str) -> tuple:
        cursor.execute("SELECT * FROM credenciales WHERE correo = :correo and contrasenha = :contrasenha", {'correo': correo, 'contrasenha': contrasenha})
        fila = cursor.fetchone()
        return fila
        


class Usuario(Credenciales):
    def __init__(self, id, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        super().__init__(id_credenciales)

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales


    def get_datos(id_credenciales) -> tuple:
        cursor.execute("SELECT * FROM USUARIO WHERE ID_CREDENCIALES = :id_c", {'id_c': id_credenciales})
        fila = cursor.fetchone()
        print(fila)
        return fila




    def agregar_amigo(self, other) -> None:
        pass


class TipoPublicacion():
    def __init__(self, id: int, tema_publicacion: str, tipo_publicacion: str) -> None:
        self.id = id
        self.tema_publicacion = tema_publicacion
        self.tipo_publicacion = tipo_publicacion


class Mensaje(Usuario):

    def __init__(self, id: int, contenido: str, fecha_publicacion: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:
        super().__init__(id_usuario_emisor, id_usuario_receptor)

        self.id = id
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion

    def get_mensajes(id_usuario_receptor) -> tuple:
        cursor.execute("select m.contenido, u.nombre from mensaje m, usuario u where m.id_usuario_emisor = u.id and m.id_usuario_receptor = :id_r", {'id_r': id_usuario_receptor})
        filas = cursor.fetchall()

        return filas
    
