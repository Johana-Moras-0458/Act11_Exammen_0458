print("Moras Martinez Johana Matricula:0458 Grado y Grupo: 5-I")
class Peluche_0458:
    #zona de atributos de la clase
    id_peluche=0
    id_proveedor=0
    nombre=0
    color=0
    tamaño=0
    precio=0
    tipo_de_tela=0
    #zona de funciones
    #-----mi lista------
    def mi_lista_id_producto_0458(self):
        lista_id_producto=["peluche 1: 01", "peluche 2: 02"]
        for id in lista_id_producto:
            print(id)
    #-----mi tupla------    
    def mi_tupla_id_proveedor_0458(self):
        tupla_id_proveedor=("proveedor 1: 01", "proveedor 2= 02")
        for id2 in tupla_id_proveedor:
            print(id2)
    #-----mi conjunto---
    def mi_conjunto_nombre_producto_0458(self):
        conjunto_nombre_producto={"peluche 1:tata", "peluche 1:koya"}
        for nom in conjunto_nombre_producto:
            print(nom)
    #-----mi diccionario---
    def dic_color_producto_0458(self):
        dic_color={
            "color": "rojo,azul y blanco",
            "tamaño" : "15 cm de alto, 20 cm de ancho",
            "tipo de tela" : "felpa",
            "precio" : "$1250"
        }
        for pe1,pe2 in dic_color.items():
            print(pe1,pe2)
    #zona de cracion de objeto
peluche1=Peluche_0458()
peluche2=Peluche_0458()
    #zona de uso de objetos
print("RESULTADO DE LOS DATOS DEL PELUCHE 1 y 2")

print("ID DEL PELUCHE")
peluche1.mi_lista_id_producto_0458()
print("PROVEEDOR DEL PELUCHE")
peluche1.mi_tupla_id_proveedor_0458()
print("NOMBRE DEL PELUCHE")
peluche1.mi_conjunto_nombre_producto_0458()
print("COLOR DEL PELUCHE")
peluche1.dic_color_producto_0458()
