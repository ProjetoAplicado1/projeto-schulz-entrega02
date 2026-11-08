
class Tecnico:
    def __init__(self, matricula, nome, turno, id_tecnico=None):
        self.id_tecnico = id_tecnico
        self.matricula = matricula
        self.nome = nome
        self.turno = turno

    def __repr__(self):
        return f"<Tecnico {self.matricula} - {self.nome}>"
