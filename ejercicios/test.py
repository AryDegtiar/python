class Documento:
    remito = 0
    notaCredito = 0
    notaDebito = 0
    notaRecibo = 0
    
    def __init__(self):
        remito += 1
        notaCredito += 1
        notaDebito += 1
        notaRecibo += 1

class Factura(Documento):
    def __init__(self):
        Documento.__init__(self)
        self.numero = Documento.remito
        self.tipo = "Factura"
    