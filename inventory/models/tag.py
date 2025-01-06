from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, db_collation="numeric")
    description = models.CharField(max_length=4096, db_collation="numeric")
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'pk']
