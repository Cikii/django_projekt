from django.db import models

class Interpret(models.Model):
    name=models.CharField(max_length=50, verbose_name="Jmeno interpreta")

    text=models.TextField(verbose_name="Info k interpretovi")

    role = (
        ("zpevak", "Zpevak"),
        ("kapela", "Kapela")
    )

    startYear=models.IntegerField(max_length=50, blank=True, null=True, verbose_name="Vznik kapely", help_text="Zadej rok")

    narodnost=models.CharField(max_length=50, verbose_name="Narodnost")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Zanr(models.Model):
    jzanr=models.CharField(max_length=50)

    class Meta:
        ordering = ['jzanr']

    def __str__(self):
        return self.jzanr


class Album(models.Model):
    a_name=models.CharField(max_length=50, verbose_name="Jmeno alba")

    a_rok=models.IntegerField(max_length=50)

    autor_a=models.ForeignKey(Interpret, on_delete=models.CASCADE, verbose_name="Interpret")

    zanr=models.ForeignKey(Zanr, on_delete=models.CASCADE, verbose_name="Zanr")

    class Meta:
        ordering = ['a_name']

    def __str__(self):
        return self.a_name

class Pisen(models.Model):
    p_name=models.CharField(max_length=50, verbose_name="Nazev pisne")
    p_writer=models.CharField(max_length=50, null=True, blank=True, verbose_name="Skladatel")
    p_lyrics=models.TextField(verbose_name="Text pisne", null=True, blank=True)
    p_album=models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Album")


    class Meta:
        ordering = ['p_name']

    def __str__(self):
        return self.p_name