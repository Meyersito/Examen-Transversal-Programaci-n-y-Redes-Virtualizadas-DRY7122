def determinar_rango_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "La VLAN corresponde al rango normal."
    elif 1006 <= vlan <= 4094:
        return "La VLAN corresponde al rango extendido."
    else:
        return "error"
while True:
    try:
        vlan = int(input("Ingrese el número de VLAN (1-4094): "))
        resultado = determinar_rango_vlan(vlan)
        if resultado == "error":
            print("Número de VLAN no válido. Inténtelo de nuevo.")
        else:
            print(resultado)
            break
    except ValueError:
        print("VLAN ingresada fuera del rango. Por favor, ingrese un número entero entre el rango de 1 a 4094.")
