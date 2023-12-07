"""CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y
públicos para el saldo y titular. Definir métodos para depositar, retirar y
consultar el saldo de la cuenta."""


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.saldo = saldo  
    
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")
    
    def consultar_saldo(self):
        return self.saldo
    
    def consultar_titular(self):
        return self.__titular


cuenta = CuentaBancaria("Leo Ponce", 100000)

print(f"Titular: {cuenta.consultar_titular()}")
print(f"Saldo actual: {cuenta.consultar_saldo()}")

cuenta.depositar(500)
print(f"Saldo después del depósito: {cuenta.consultar_saldo()}")

cuenta.retirar(200)
print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")

cuenta.retirar(1500) 
print(f"Saldo después del segundo retiro: {cuenta.consultar_saldo()}")
