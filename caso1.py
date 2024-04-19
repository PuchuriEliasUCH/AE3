class Personal:
    def __init__(self, codigo, nombre, apellido, ciudad):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def reporte(self):
        print(f"""
Codigo: {self.codigo}
nombre: {self.nombre}
Apellido: {self.apellido}
Ciudad: {self.ciudad}
""")
    
class Vendedor(Personal):
    def __init__(self, codigo, nombre, apellido, ciudad, horas_t, tarifa):
        super().__init__(codigo, nombre, apellido, ciudad)
        self.horas_t = horas_t
        self.tarifa =  tarifa
    
    def sueldo_basico(self):
        return self.horas_t * self.tarifa

    def bono(self):
        return (0 if self.horas_t <= 40 else (self.horas_t - 40) * self.tarifa * 0.25)  
    
    def sueldo_neto(self):
        return self.sueldo_basico() + self.bono()

    def imprimir(self):
        print(f"""
Codigo: {self.codigo}
Nombre: {self.nombre}
Apellido: {self.apellido}
Ciudad: {self.ciudad}
Horas Trabajadas: {self.horas_t}
Tarifa por hora: {self.tarifa}
Sueldo base: S/{self.sueldo_basico()}
Bonificación: S/{self.bono()}
Sueldo Neto: S/{self.sueldo_neto()}
""")

class Cajero(Personal):
    def __init__(self, codigo, nombre, apellido, ciudad, categoria, num_hijos):
        super().__init__(codigo, nombre, apellido, ciudad)
        self.categoria = categoria
        self.num_hijos = num_hijos

    def sueldo_basico(self):
        match self.categoria:
            case "a":
                return 4500
            case "b":
                return 3200
            case "c":
                return 3000
            case "d":
                return 2800
            case "e":
                return 3500
            case "f":
                return 2000
            case _:
                return 0
    
    def bono(self):
        if 0 <= self.num_hijos < 4:
            return self.sueldo_basico() * 0.055
        elif 4 <= self.num_hijos < 7:
            return self.sueldo_basico() * 0.072
        elif 7 <= self.num_hijos < 10:
            return self.sueldo_basico() * 0.085
        elif 10 <= self.num_hijos :
            return self.sueldo_basico() * 0.1
        else:
            return 0
        
    def sueldo_neto(self):
        return self.sueldo_basico() + self.bono()
    
    def imprimir(self):
        print(f"""
Codigo: {self.codigo}
nombre: {self.nombre}
Apellido: {self.apellido}
Ciudad: {self.ciudad}
Categoría: {self.categoria}
Número de hijos: {self.num_hijos}
Sueldo base: S/{self.sueldo_basico()}
Bonificación: S/{self.bono()}
Sueldo Neto: S/{self.sueldo_neto()}
""")
        
obj1 = Vendedor(
    input("Ingrese código: "), 
    input("Ingrese nombre: "), 
    input("Ingrese apellido: "), 
    input("Ingrese ciudad: "), 
    int(input("Ingrese número de horas trabajadas: ")),
    int(input("Ingrese tarifa por hora"))
)
obj1.imprimir()

obj2 = Cajero(
    input("Ingrese código: "), 
    input("Ingrese nombre: "), 
    input("Ingrese apellido: "), 
    input("Ingrese ciudad: "),
    input("Ingrese categoría: "),
    int(input("Ingrese número de hijos: "))
)

obj2.imprimir()