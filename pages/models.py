from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='csv')

    def __unicode__(self):
        return u"document"
