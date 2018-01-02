from django.db import models
from django.utils import timezone


class Podroz(models.Model):
	cel_podrozy = models.TextField(max_length=50)
	przejezdza_przez = models.TextField(max_length=2000)
	godzina_odjazdu = models.TimeField(blank=True, null=True)

	def __str__(self):
		return self.cel_podrozy


'''
cel
godzina odjazdu
przejeżdża przez
stanowisko
numer/firma/

Etap 2:
kiedy przejeżdża przez daną miejscowość
godzina przyjazdu

- Czy to autobusy?
- Jak wygląda rozkład? Czy kursy są regularne czy też są wyjątki?
- W jakim stopniu trzeba zadbać o godziny odjazdu ze stacji pośrednich? Np. przy opóźnieniu autobusu.
'''