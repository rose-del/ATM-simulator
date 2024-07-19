#Rosenilda Santos e Júlia Benjamin
import os

nome = str(input("Digite o seu nome: "))
cpf = str(input("Digite o seu CPF: ")) #Colocamos tipo string por causa da formatação do cpf que tem '.' e '-'
saldo = 1000

def caixa():
    print(f"SALDO: R${saldo},00")
    print("1-Depositar")
    print("2-Sacar")
    print("3-Transferir")
    print("4-Consultar Saldo")
    print("5-Sair")
    print()

caixa()

while True:
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        deposito = float(input("Digite o valor: "))
        
        saldo += deposito
    elif opcao == 2:
        sacar = float(input("Digite o valor: "))

        saldo -= sacar
    elif opcao == 3:
        transferencia = float(input("Digite o valor: "))

        if saldo >= transferencia:
            pessoa = 0

            saldo -= transferencia
            pessoa += transferencia

            print(f"VALOR ATUAL DEPOIS DA TRANSFERÊNCIA: R${saldo}")
            print(f"VALOR RECEBIDO: R${pessoa}")
    elif opcao == 4:
        print(f"SALDO: R${saldo},00")
    elif opcao == 5:
        os.system('clear')
        break



        






