#Clases

# === FORMULA === ** me refiero a lo basico de como se logra iniciar
class MyPerson:
    pass 
print(MyPerson) # con o sin () parametros 

# === CONSTRUCTOR === ** lo mismo que java
class Person:
    def __init__(self, name, surname): # aca van parametros propios de la clase
        self.name = name  # se reescribe a si mismo con el parametro name
        self.surname = surname # es igualito lo que haciamos con clases en java

# === ASIGNACION DATOS ===
my_person = Person("Exexd", "39")
print(my_person.name) # forma basica de imprimir un parametro ya habiendole pasado datos
print(f"{my_person.name} {my_person.surname}")

# === OTROS EJEMPLOS ===
class NombreEjemplo:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.fullname = f"{name} {surname} {alias}" # dato publico
        self.__name = name # dato privado

    def get_name(self):
        return self.__name 
    
    def caminar(self): # NECESARIO para poder utilizar fullname
        print(f"{self.fullname} Esta caminando")

# nombre
nombre_ejemplo = NombreEjemplo("Exexd", "39") # si no se pasa un alias solo dira "Sin alias"
print("1.- Esto es del fullname: ",nombre_ejemplo.fullname)
# metodo caminar
nombre_ejemplo.caminar() # se utiliza de esta forma metodos de la propia clase

