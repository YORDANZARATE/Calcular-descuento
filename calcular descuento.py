#  crear un programa que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar.
#creamos una funcion
def calcular_descuento(valor_compra=0, porcentaje_descuento=0):

    # Calcular el descuento
    descuento = (valor_compra / 100) * porcentaje_descuento

    # Calcular el valor a pagar
    valor_a_pagar = valor_compra - descuento

    return descuento, valor_a_pagar


# realizamos la impresion de los resultados
descuento, valor_final = calcular_descuento(70, 20)
print(f"Descuento: {descuento:.2f}, Valor a pagar: {valor_final:.2f}")



""" valor a pagar 56.00
descuento  del 20%  14 valor de descuento"""

#creamos otro programa

#creamos su funcion para calcular el descuento utilizando el valor de la compra y el valor del descuento

def calcular_descuento(valor_compra=0, porcentaje_descuento=0):

    descuento = (valor_compra*porcentaje_descuento)/100

    return descuento, valor_compra

print(calcular_descuento(100, 50))
nombre = input("¿Nesecitas comprar algo mas? ")
print(f"¡Gracias, ! Apreciamos tu visita.")