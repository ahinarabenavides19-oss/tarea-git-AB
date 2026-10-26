# Curso: Fundamentos de Tecnología Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Ahinara Benavides Espinoza 

# Programa que calcula el total de una compra de maquillaje.

print("=== Tienda de maquillaje ===")

precio_labial = 5000
precio_base = 8000

cantidad_labiales = int(input("¿Cuantos labiales desea comprar?"))
cantidad_bases = int(input("¿Cuantas bases desea comprar?"))

total= (cantidad_bases * precio_base)+(cantidad_labiales*precio_labial)
print ( "El total a pagar es de: ", total)