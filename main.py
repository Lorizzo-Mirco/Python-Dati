inventario = {}

def Aggiungi_Item():
    id = len(inventario) + 1
    nome = input("Inserisci il nome del prodotto ")
    qta = input("Inserisci la quantità ")
    while True:
        try:
            prezzo = float(input("Inserisci il prezzo "))
            break
        except:
            print("Inserisci un prezzo valido")
    product = {}
    product["nome"] = nome
    product["qta"] = qta
    product["prezzo"] = prezzo

    inventario[id] = product

