def exibirpoema (data_extenso,*args,**kwargs):
    texto = ".\n".join(args)
    metadados = "\n".join([f"{chave.title()}: {valor}" for chave,valor in kwargs.items()])
    mensage = f"\n{data_extenso} \n\n{texto} \n\n{metadados}"
    print(mensage)

exibirpoema(
    "Terça-feira, 17 de fevereiro de 20266",
    "batatinha quando nasce",
    "espalha a rama pelo chão",
    "meu chefinho querido",
    "mora no meu coração",
    nome="Corrimão do sucesso",
    autor="João das Couves",
    ano=2026
)