
# Este codigo é o desafio do projeto do modulo sintaxe bascia com python do curso Suzano - Python Developer


from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
operacoes = []


# valida se p valor digitado é um número positivo
def valida_valor(valor_digitado) :
    
    
    
    if valor_digitado.isnumeric():
          
          valor_convertido = int(valor_digitado)
          return valor_convertido
              
    else:
          
          print('Utilize somente valores numéricos positivos')
          return None
            

# Função que valida o seque, considera valor válido, limite quantidade de saques
def valida_saques ():
    global numero_saques
    global LIMITE_SAQUES
    global saldo
    global limite

    if numero_saques > (LIMITE_SAQUES-1):
          print(f"O limite de {LIMITE_SAQUES} saques diário foi atingido.")
          return None
    
    else:
          valor_digitado = input("infome o valor para saque: ")
          valor_validado = valida_valor(valor_digitado)

          if valor_validado is None:
                return


          if valor_validado > saldo:
               print(f"\nSaldo insuficiente para realizar a operação \nSaldo atual: {saldo}")
               return None
    
          elif valor_validado > limite:
                print(f"\nO limite por operação é RS{limite}. Tente novamente!") 
                return None

          else:
               return valor_validado

        
# processo que consolida as operações na lista operacoes
def processa_operacoes(operacao, sinal_operacao, valor_operacao):
     global operacoes
    
     dt_operacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    #  operacao_montada = (f"{dt_operacao}  {operacao}  {sinal_operacao}R$ {valor_operacao:.2f}")
     operacao_montada = (
        f"{dt_operacao} - "
        f"{operacao:<10} "
        f"{sinal_operacao} "
        f"R$ {valor_operacao:>12.2f}"
     )
     
     operacoes.append(operacao_montada)


# exibe resumo de operações
def exibe_operacoes():
    global operacoes
    global saldo

    largura = 60
    cabecalho = "  BANCO DIO S/A  ".center(largura, "-")
    quebra_linha = "".center(largura, "=")

    if not operacoes:
        operacoes_listadas = "Não foram realizadas movimentações."
    else:
        operacoes_listadas = "\n".join(operacoes)

    saldo_atual = f"Saldo R$ {saldo:>10.2f}".rjust(largura)

    print(f"{cabecalho}\n"
          f"{quebra_linha}\n"
          f"{operacoes_listadas}\n"
          f"{quebra_linha}\n"
          f"{saldo_atual}")

# executa o deposito, mas valida o valor antes
def processa_deposito ():
    global saldo
    global operacoes  
    
    valor_digitado = input("infome o valor para deposito: ")
     
    valor_deposito =  valida_valor(valor_digitado)
   
    if valor_deposito is None:
        return

    saldo += float(valor_deposito)
   
    processa_operacoes("Deposito","+",valor_deposito )
    
    print (f"\nValor do depósito: {valor_deposito} \nSaldo atual: {saldo}")


# executa o saque
def processa_saque ():
      global saldo
      global numero_saques
    
      valor_validado = valida_saques()

      if valor_validado is None:
            return

      saldo -= float(valor_validado)
      numero_saques += 1
         
      processa_operacoes("Saque","-",valor_validado )
      
      print (f"Valor do Saque: {valor_validado} \nSaldo atual: {saldo}\nNúmero de saques: {numero_saques}")




while True:
 
    opcao = input(menu)

    if opcao == "d":
        # print("Depósito")    
        processa_deposito()

    elif opcao == "s":
        # print("Saque")
        processa_saque ()
        

    elif opcao == "e":
        
        # print("Extrato")
        exibe_operacoes()

    elif opcao == "q":
        break
    
    else: print("Opção inválida! por favor, selecione novamente a opção desejada")