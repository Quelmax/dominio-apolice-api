from app.repositories.IApoliceRepository import IApoliceRepository
from app.domain.apolice import Apolice

class ApoliceRepositorioMemoriaMock(IApoliceRepository):
    def __init__(self):
        self.apolices = []

    def salvar(self, apolice:Apolice) -> Apolice:
        self.apolices.append(apolice)
        return apolice

    def listar(self):
        return self.apolices

    def buscar_por_id(self, id):
        for apolice in self.apolices:
            if apolice['id'] == id:
                return apolice
        return None

    def atualizar(self, id, dados_atualizados):
        for apolice in self.apolices:
            if apolice['id'] == id:
                apolice.update(dados_atualizados)
                return apolice
        return None

    def deletar(self, id):
        for apolice in self.apolices:
            if apolice['id'] == id:
                self.apolices.remove(apolice)
                return True
        return False