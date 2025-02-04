from django.db import models

class MadLibResponse(models.Model):
    adjective1 = models.CharField(max_length=50)
    software_type = models.CharField(max_length=50)
    programming_language = models.CharField(max_length=50)
    number = models.IntegerField()
    bug_type = models.CharField(max_length=50)
    adjective2 = models.CharField(max_length=50)
    verb_ing = models.CharField(max_length=50)
    plural_noun = models.CharField(max_length=50)
    software_company = models.CharField(max_length=50)
    silly_word = models.CharField(max_length=50)
    verb_past = models.CharField(max_length=50)
    famous_person = models.CharField(max_length=50)
    adjective3 = models.CharField(max_length=50)
    noun1 = models.CharField(max_length=50)
    verb1 = models.CharField(max_length=50)
    verb2 = models.CharField(max_length=50)
    adjective4 = models.CharField(max_length=50)
    noun2 = models.CharField(max_length=50)

    def __str__(self):
        return f"MadLib Entry {self.id}"
