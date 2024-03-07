class cuenta():
    
    def _init_ (self, identidad, cliente, tipo, saldo):
        self.identidad  = identidad
        self. cliente = cliente
        self.tipo = tipo
        self. saldo = saldo

    def saldo_cliente (self):
        if self.saldo <= 0:
            return " error "

        else :
            return self.saldo
        

    def credit (self, monto):
        if monto > 0 :
            self.saldo += monto
            return " se agrego saldo,  saldo actual:"  +str(self.saldo)

        else:
    
            self.saldo-= monto
            return( " se saco saldo, saldo actual:",monto)       



    def cargar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return "Se retiró saldo, saldo actual: " + str(self.saldo)
        else:
            return "El monto a cargar excede el saldo de la cuenta"
   
        
carlos = cuenta ( 123, " carlos ", " ahorros ", 0)
james = cuenta ( 100, " james ", "ahorros ", 500 )
sara = cuenta ( 124, " sara ", " corriente ", 700)

print ( " su saldo es : ", james.saldo_cliente())
print(james.credit(200))
print(james.cargar(100))

print ( " su saldo es : ", carlos.saldo_cliente())
print(carlos.credit(200))
print(carlos.cargar(100))