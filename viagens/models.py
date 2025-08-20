from django.db import models

class Viagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_partida = models.DateTimeField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    assentos_totais = models.IntegerField()
    assentos_reservados = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.origem} → {self.destino} ({self.data_partida})"


class Passageiro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name="reservas")
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE, related_name="reservas")
    assento_numero = models.IntegerField()
    telefone = models.CharField(max_length=20)
    data_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.passageiro.nome} - {self.viagem}"
