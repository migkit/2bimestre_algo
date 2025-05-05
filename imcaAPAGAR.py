def calculadora_imc(pessoa):
    imc= pessoa["peso"]/ (pessoa["altura"] * pessoa["altura"])
    resultado = (f"O IMC {pessoa["nome"]} é {imc:.2f}")
    #comando ternario
    saudavel = 18.5 < imc < 25


    return {
        "nome": pessoa["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    }

pessoa1= {
    "nome":"josé",
    "peso": 110,
    "altura": 1.75
}

pessoa2= {
    "nome":"pedro",
    "peso": 70,
    "altura": 1.72
}

print (calculadora_imc(pessoa1))