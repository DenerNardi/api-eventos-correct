from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"https://tamacardo.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local)


    def imprime_informacoes(self):
        print("ID do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Link para acessar o evento:", self.local)
        print("-------------------------")