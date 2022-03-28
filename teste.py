from models.cliente import Cliente
from models.conta import Conta

fernando: Cliente = Cliente(nome='Fernando', email='fernando@gmail.com',
                            cpf='123.456.789-00', data_nascimento='02/06/1991')
juliana: Cliente = Cliente(nome='juliana', email='juliana@gmail.com',
                           cpf='987.654.321-00', data_nascimento='29/01/1982')

contaf: Conta = Conta(fernando)
contaj: Conta = Conta(juliana)

print(contaf)
print(contaj)
