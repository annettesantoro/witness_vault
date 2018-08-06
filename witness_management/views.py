from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Importing Of Models
from .models import Witness
from document_management.models import Document
from interaction_management.models import Interaction
# Importing of timezone
from django.utils import timezone
# Importing of forms
from .forms import WitnessForm
from document_management.forms import DocumentForm
from interaction_management.forms import InteractionForm
# Create your views here.

def witness_workbench(request):
    witnesses = Witness.objects.all()
    return render(
        request,
        'witness_management/witness_workbench.html',
        {'witnesses': 'witnesses',
        'witness': 'witness',
        'title': 'Witness Management Workbench'})

def new_witness(request):
    form = WitnessForm()
    if request.method == "POST":
        form = WitnessForm(request.POST)
        if form.is_valid():
            witness = form.save(commit=False)
            witness.created_by = request.user
            witness.created_date = timezone.now()
            witness.save()
            witness.witness_status = 'New'
            witness.witness_number = "W - " + str(witness.id)
            witness.save()
            messages.success(request, 'New Witness Has Been Created', extra_tags='modify modify_witness/' + str(witness.id))
            return redirect(witness_workbench)
        else:
            messages.error(request, 'Witness Has Not Been Created')
    else:
        form = WitnessForm()
    return render(request,
                  'witness_management/witness.html',
                  {'form': form,
                   'title': 'New Witness'})

def modify_witness(request, pk):
    # Query Sets
    witness = get_object_or_404(Witness, pk=pk)
    # Forms
    document_form = DocumentForm()
    interaction_form = InteractionForm()
    # Modify Witness
    if request.method == "POST" and 'master' in request.POST:     
        form = WitnessForm(request.POST, instance=witness)
        if form.is_valid():
            form = WitnessForm(request.POST, instance=witness)
            witness.modified_by = request.user
            witness.modified_date = timezone.now()
            if witness.parent_id == '':
                witness.parent_id = None
            witness.save()
            witness.witness_number = "WIT" + str(witness.id)
            witness.save()
            messages.success(request, 'Witness Has Been Modified')
            return redirect(witness_workbench)
        else:
            messages.error(request, 'Witness Has Not Been Modified')
    else:
        form = WitnessForm(instance=witness)
    # Create Relationship to Document
    if request.method == "POST" and 'witness_document' in request.POST:
        document_form = DocumentForm(request.POST, request.FILES)
        if document_form.is_valid():
            document = document_form.save(commit=False)
            document.created_by = request.user
            document.created_date = timezone.now()
            document.save()
            document.document_number = "DOC" + str(document.id)
            document.parent_id = witness.id
            document.document_number = "DOC" + str(document.id)
            document.parent_source = "Witness Management"
            document.save()
            witness.save()
            document_form = DocumentForm()
            messages.success(request, 'New Document Has Been Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Document Has Not Been Created')
    else:
        document_form = DocumentForm()
    # Create Relationship to Interaction
    if request.method == "POST" and 'witness_interaction' in request.POST:
        interaction_form = InteractionForm(request.POST, request.FILES)
        if interaction_form.is_valid():
            interaction = interaction_form.save(commit=False)
            interaction.created_by = request.user
            interaction.created_date = timezone.now()
            interaction.save()
            interaction.parent_id = witness.id
            interaction.interaction_number = "I - " + str(interaction.id)
            interaction.save()
            interaction_form = InteractionForm()
            messages.success(request, 'New Interaction Has Been Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Interaction Has Not Been Created')
    else:
        interaction_form = InteractionForm()
    return render(request,
                  'witness_management/witness.html',
                  {'form': form,
                   'document_form': document_form,
                   'interaction_form': interaction_form,
                   'witness': witness,
                   'modify': 'modify',
                   'title': 'Modify Witness:  ' + str(witness.witness_number)})