from listaporCursor import ListaPorContenido

if __name__ == "__main__":
    cant = int(input("\nIngrese la cantidad de elementos de la lista:"))
    unaLista = ListaPorContenido(cant)
    i = 0
    x = int(input("\nIngrese el dato:"))
    while (x != -1) and (i < cant):
        pos = int(input("Ingrese la posicion donde quiere insertar el elemento:"))
        res = unaLista.insertar(x,pos)
        if res != 0:
            i+=1
        if i != cant:
            x = int(input("\nIngrese el dato, -1 para finalizar:"))
    print("\nEl primer elemento es: {}".format(unaLista.primerElemento()))
    print("\nEl ultimo elemento es: {}".format(unaLista.ultimoElemento()))
    x = int(input("\nIngrese el elemento a recuperar:"))
    print("\nEl numero recuperado es: {}".format(unaLista.recuperar(x)))
    print("\nEl anterior al numero recuperado es:{}".format(unaLista.anterior(x)))
    print("\nEl siguiente al numero recuperado es:{}".format(unaLista.siguiente(x)))
    unaLista.mostrar()
    elim = int(input("\nIngrese la posicion que desea eliminar:"))
    unaLista.suprimir(elim)
    unaLista.mostrar()