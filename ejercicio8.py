producto = float(input("Ingrese precio de un producto: "))

IVA = 0.21
IMP_MUN = 0.015
ING_BRUTO = 0.025

iva = producto * IVA
ingBruto = producto * ING_BRUTO
impMun = producto * IMP_MUN
precioFinal = producto + iva + ingBruto + impMun

print(f"Producto \nIVA: {iva} \nIngreso Bruto: {ingBruto} \nImpuesto Municipal: {impMun} \nPrecio Final: {precioFinal}")