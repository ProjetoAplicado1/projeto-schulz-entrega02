
class Equipamento:
    def __init__(self, tag_codigo, descricao, setor_cliente, id_equipamento=None):
        self.id_equipamento = id_equipamento
        self.tag_codigo = tag_codigo
        self.descricao = descricao
        self.setor_cliente = setor_cliente
