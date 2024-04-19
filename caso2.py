class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def datos(self):
        return f"""
Codigo: {self.codigo}
Nombre: {self.nombre}
Precio: S/{self.precio:.2f}
"""
        
class Bebida:
    def __init__(self, tipo, capacidad) -> None:
        self.tipo = tipo
        self.capacidad = capacidad

    def aumento(self):
        match self.tipo:
            case "alcoholica":
                return 0.1
            case "gasificada":
                return 0.05
            case _:
                return 0

class Ready_to_drink(Producto, Bebida):
    def __init__(self, codigo, nombre, precio, tipo, capacidad):
        Producto.__init__(self, codigo, nombre, precio)
        Bebida.__init__(self, tipo, capacidad)
    
    def impuesto(self):
        return self.precio * self.aumento()
    
    def precio_final(self):
        return self.precio + self.impuesto()
    
    def imprimir(self):
        print(f"""{self.datos()}Tipo de Bebida: {self.tipo}
Capacidad: {self.capacidad}
Aumento: S/{self.impuesto():.2f}
Precio final: S/{self.precio_final()}
""")

obj = Ready_to_drink(
    input("Ingresar código de producto: "), 
    input("Ingresar nombre  de producto: "), 
    float(input("Ingresar precio: ")), 
    input("Ingresar tipo de bebida: "), 
    input("Ingresar capacidad [1L, 350ml]: "))
obj.imprimir()