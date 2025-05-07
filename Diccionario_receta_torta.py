# Diccionario de ingredientes para una torta de chocolate

ingredientes_torta_de_chocolate = {
    "chocolate": "1 libra",
    "harina": "2 libras",
    "sal": "3 cucharadas",
    "huevos": "3 unidades"
}

print("Ingredientes para preparar una torta de chocolate:\n")
for ingrediente, cantidad in ingredientes_torta_de_chocolate.items():
    print(f"- {ingrediente.capitalize()}: {cantidad}")
