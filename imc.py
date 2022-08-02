#Pedir datos
nombre = input("Buenas tardes favor de ingresar su nombre: ")
print("Muy bien " + nombre + ", ahora por favor ingresa lo que se te pida a continuación")
peso = int(input("Ingrese su peso en kg (Ejemplo: 70): "))
altura = float(input("Ingrese su altura en mt (Ejemplo: 1.70): "))

#Formula del IMC
def formulaIMC(peso, altura):
    imc = peso // (altura ** 2)
    return imc

imc = formulaIMC(peso, altura)

#Dar resultado
if imc < 19:
    print("Tu IMC indica que entras en el rango de delgado." + " Este es tu IMC representado en número: " + str(imc))
if imc >= 20 and imc < 26:
    print("Tu IMC indica que entras en el rango de normal." + " Este es tu IMC representado en número: " + str(imc))
if imc >= 26 and imc < 30:
    print("Tu IMC indica que entras en el rango de sobrepeso." + " Este es tu IMC representado en número: " + str(imc))
if imc >= 30:
    print("Tu IMC indica que entras en el rango de obesidad." + " Este es tu IMC representado en número: " + str(imc))