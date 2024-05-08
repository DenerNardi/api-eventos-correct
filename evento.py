import json

class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def imprime_informacoes(self):
        print("ID do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)
        print("-------------------------")

    def toJSON(self):
        return json.dumps(self.__dict__)   


    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif area >= 10 and area < 20:
            return 15
        elif area >= 20:
            return 30
        else: 
            return 0




    

