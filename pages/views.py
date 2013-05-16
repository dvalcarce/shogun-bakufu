# -*- encoding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from pages.models import Document
from pages.forms import DocumentForm

footer = "© 2013 Shogun Toolbox Foundation"


def home(request):
    """
    Renders homepage
    """
    c = {'title': "Homepage", 'footer': footer}

    return render_to_response('mainpage.html', c)


def upload(request):
    """
    File upload view
    """
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document.create(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('pages.views.upload'))
    else:
        form = DocumentForm()   # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    print documents

    # Render list page with the documents and the form
    return render_to_response(
        'upload.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
