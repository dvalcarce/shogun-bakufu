from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

    def __unicode__(self):
        return u"form"
