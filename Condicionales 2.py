edad = int(input("Por favor, ingresa tu edad"))

if edad <0:
    print("Edad no valida, ingresa una edad valida")
elif edad <12:
    print("Eres un niño")
elif edad <18:
    print("Eres un Adolescente")
elif edad <65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")