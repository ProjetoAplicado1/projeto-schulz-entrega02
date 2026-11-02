class Medicao:
    def __init__(
        self,
        id_equipamento_fk,
        id_tecnico_fk,
        numero_certificado,
        data_calibracao,
        parametro_cota,
        valor_nominal,
        tolerancia_pos,
        tolerancia_neg,
        meas_1,
        meas_2,
        id_medicao=None
    ):
        self.id_medicao = id_medicao
        self.id_equipamento_fk = id_equipamento_fk
        self.id_tecnico_fk = id_tecnico_fk
        self.numero_certificado = numero_certificado
        self.data_calibracao = data_calibracao
        self.parametro_cota = parametro_cota
        self.valor_nominal = valor_nominal
        self.tolerancia_pos = tolerancia_pos
        self.tolerancia_neg = tolerancia_neg
        self.meas_1 = meas_1
        self.meas_2 = meas_2

        self.valor_obtidomean = None
        self.erro_calculado = None
        self.status_resultado = None

    def calcular_media(self):
        self.valor_obtidomean = (self.meas_1 + self.meas_2) / 2
        return self.valor_obtidomean

    def calcular_erro(self):
        media = self.calcular_media()
        self.erro_calculado = media - self.valor_nominal
        return self.erro_calculado

    def validar_tolerancia(self):
        erro = self.calcular_erro()

        tol_inferior = -abs(self.tolerancia_neg)    # função '-abs' garante que seja SEMPRE negativo
        tol_superior = abs(self.tolerancia_pos)     # função 'abs' garante que seja SEMPRE positivo

        if tol_inferior <= erro <= tol_superior:
            self.status_resultado = "APROVADO"
        else:
            self.status_resultado = "REPROVADO"

        return self.status_resultado