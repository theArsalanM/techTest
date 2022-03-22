from django.db import models


class Activity(models.Model):
    type = models.CharField(blank=True, null=True, max_length=250)
    units = models.CharField(blank=True, null=True, max_length=100)
    value = models.TextField(blank=True, null=True)  # This field type is a guess.
    relation = models.CharField(blank=True, null=True, max_length=2)
    target = models.ForeignKey('Target', models.DO_NOTHING, blank=True, null=True)
    molecule = models.ForeignKey('Molecule', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'

    def __str__(self):
        return f"Activity Instance - {self.type} - {self.target} - {self.molecule}"


class Molecule(models.Model):
    name = models.TextField(blank=True, null=True)
    max_phase = models.IntegerField(blank=True, null=True)
    structure = models.CharField(blank=True, null=True, max_length=4000)
    inchi_key = models.CharField(blank=True, null=True, max_length=27)

    class Meta:
        managed = False
        db_table = 'molecule'

    def __str__(self):
        return f"Molecule {self.name}"


class Target(models.Model):
    name = models.TextField(blank=True, null=True)
    organism = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'target'

    def __str__(self):
        return f"Target {self.name}"
