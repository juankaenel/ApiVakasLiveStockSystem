from django.db import models

class Timestamps(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True #esto agrego sino, las apps que heredan toman como id timestamps