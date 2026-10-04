def cal_potencia(v,r):
    if r<=0:
        print("No existe resistencia <0")
        return 0
    potencia=(v**2)/r
    return potencia

voltaje=float(input("Ingrese voltaje: "))
restistencia=float(input("ingrese resistencia: "))

resultado=cal_potencia(voltaje,restistencia)
print(f'El resultado con dos decimales es: {resultado:.2f} watts')
print(f'el valor redondeado es: {round(resultado)} watts')