from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Document
from .forms import DocumentForm

# Create your views here.

def document_workbench(request):
    return render(
        request,
        'document_management/document_workbench.html',
        {'title': 'Document Management Workbench'})

def new_document(request):
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.created_date = timezone.now()
            if document.parent_id == '':
                document.parent_id = None
            document.save()
            document.document_number = "W - " + str(document.id)
            document.save()
            messages.success(request, 'New Document Has Been Created', extra_tags='modify modify_document/' + str(document.id))
            return redirect(document_workbench)
        else:
            messages.error(request, 'Document Has Not Been Created')
    else:
        form = DocumentForm()
    return render(request,
                  'document_management/document.html',
                  {'form': form,
                   'title': 'New Document'})
   


def modify_document(request, pk):
    # Query Sets
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST" and "master" in request.POST:
        form = DocumentForm(request.POST, request.FILES,
                            instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            document.modified_by = request.user
            document.modified_date = timezone.now()
            if document.parent_id == "": document.parent_id = None
            document.save()
            document.document_number = "D" + str(document.id)
            document.save()
            messages.success(request, 'Document Has Been Modified')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Document Has Not Been Modified')
    else:
        form = DocumentForm(instance=document)
    return render(request,
                  'document.html',
                  {'form': form,
                   'document': document,
                   'title': 'Document ' + str(document.document_number)})        