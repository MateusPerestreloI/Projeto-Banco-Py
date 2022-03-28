from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    contas.append(Conta(Cliente(nome='Fernando', email='fernando@gmail.com',
                        cpf='123.456.789-00', data_nascimento='05/06/1996')))
    contas.append(Conta(Cliente(nome='Juliana', email='juliajna@gmail.com',
                        cpf='987.654.321-00', data_nascimento='05/06/1985')))
    menu()


def menu() -> None:
    print('=================================================================')
    print('------------------------------ ATM ------------------------------')
    print('----------------------------- Banco -----------------------------')
    print('=================================================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Depósito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte Sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informa os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de Nascimento do cliente: ')

    cliente: Cliente = Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento)

    conta: Conta = Conta(cliente=cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('-----------------------------------------')
    print('Dados da conta: ')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        print('====================== Efetuar Saque ======================')
        numero: int = int(input('Informe o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero=numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor=valor)
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
    else:
        print('Ainda não existe(m) conta(s) cadastrada(s)')
    sleep(1)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        print('====================== Efetuar Depósito ======================')
        numero: int = int(input('Informe o numero da conta em que irá ser depósitado: '))

        conta: Conta = buscar_conta_por_numero(numero=numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
    else:
        print('Ainda não existe(m) conta(s) cadastrada(s)')
    sleep(1)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        print('====================== Efetuar Transfêrencia ======================')
        numero_origem: int = int(input('Informe o numero da conta sua conta: '))

        conta_origem: Conta = buscar_conta_por_numero(numero=numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o numero da conta conta que irá receber a transferência: '))

            conta_destino: Conta = buscar_conta_por_numero(numero=numero_destino)
            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_origem.transferir(destino=conta_destino, valor=valor)
            else:
                print(f'Não foi encontrada a conta de destino com número: {numero_origem} ')
        else:
            print(f'Não foi encontrada a sua conta com número: {numero_origem} ')
    else:
        print('Ainda não existe(m) conta(s) cadastrada(s)')
    sleep(1)
    menu()


def listar_contas() -> None:
    if len(contas):
        print('====================== Listar Contas ======================')

        for conta in contas:
            print(conta)
            print('-----------------------')
            sleep(1)
    else:
        print('Ainda não existe(m) conta(s) cadastrada(s)')
    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
