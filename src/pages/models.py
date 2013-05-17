import csv
import mimetypes
import os

from django.db import models


class Document(models.Model):
    """
    Document class.
    Saves an uploaded file and its data.
    """
    docfile = models.FileField(upload_to='csv')
    filetype = models.CharField(max_length=20, null=True, blank=True)
    rows = models.IntegerField(null=True)
    cols = models.IntegerField(null=True)

    def __unicode__(self):
        return u"document"

    def delete(self, *args, **kwargs):
        """
        Delete Document from DB and disk
        """
        # Delete from disk
        os.remove(self.docfile.path)
        # Delete from DB
        super(Document, self).delete(*args, **kwargs)

    @classmethod
    def create(cls, docfile):
        """
        Factory method.
        Use this method for Document instantiation instead of __init__.
        """
        # Save document
        document = Document(docfile=docfile)

        # Get MIME type from document name
        document.filetype = mimetypes.guess_type(docfile.name, strict=False)[0]

        # Get number of rows and columns of the uploaded file
        try:
            csvfile = csv.reader(docfile, delimiter=',', quotechar='|')
            data = list(csvfile)
            document.rows = len(data)
            document.cols = len(data[0])
        except csv.Error:
            document.rows = 0
            document.cols = 0

        return document
