import csv

from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='csv')
    rows = models.IntegerField(null=True)
    cols = models.IntegerField(null=True)

    def __unicode__(self):
        return u"document"

    @classmethod
    def create(self, docfile):
        """
        Factory method.
        Use this method for Document instantiation instead of __init__.
        """
        document = Document(docfile=docfile)
        try:
            csvfile = csv.reader(docfile, delimiter=',', quotechar='|')
            data = list(csvfile)
            document.rows = len(data)
            document.cols = len(data[0])
        except csv.Error:
            document.rows = 0
            document.cols = 0

        return document
