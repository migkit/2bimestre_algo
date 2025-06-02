codigo = ("ABC123" , "XYZ789" , "DEF456" , "JKL321" , "MNO654" , "PQR987" , "STU741" )
status = ( "enviado", "recebido" , "em transito" , "enviado" , "recebido" , "em transito" , "enviado")

print("foram enviados: ", status.count ("enviado"))
print("estao em transito: ", status.count("em transito"))
print("foram recebidos: ", status.count("recebido"))

for i in range(len(codigo)):
if status == "em transito":
    print(codigo)
