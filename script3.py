numero_acl = input("Ingrese el número de ACL IPv4: ")

if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if numero_acl >= 1 and numero_acl <= 99:
        print("Es una ACL Estándar.")
    elif numero_acl >= 100 and numero_acl <= 199:
        print("Es una ACL Extendida.")
    else:
        print("El número no corresponde a una lista de acceso.")
else:
    print("El número de ACL IPv4 ingresado no es válido.")