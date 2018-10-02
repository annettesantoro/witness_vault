from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Importing Of Models
from .models import Witness, Activity, Document, Interaction
# Importing of timezone
from django.utils import timezone
# Importing of forms
from .forms import WitnessForm, ActivityForm, DocumentForm, InteractionForm
# Create your views here.

def witness_workbench(request):
    witnesses = Witness.objects.all()
    return render(request,
                  'witness_management/witness_workbench.html',
                  {'witnesses': witnesses,
                   'title': 'Witness Workbench'})

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
    documents = Document.objects.filter(parent_id=witness.id)
    interactions = Interaction.objects.filter(parent_id=witness.id)
    activities = Activity.objects.filter(parent_id=witness.id)
    # Forms
    document_form = DocumentForm()
    interaction_form = InteractionForm()
    #activity_form = ActivityForm()
    # Modify Witness
    if request.method == "POST" and 'master' in request.POST:     
        form = WitnessForm(request.POST, instance=witness)
        if form.is_valid():
            form = WitnessForm(request.POST, instance=witness)
            witness.modified_by = request.user
            witness.modified_date = timezone.now()
            witness.save()
            witness.witness_number = "W - " + str(witness.id)
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
            document.parent_id = witness.id    
            document.save()
            document.document_number = "D - " + str(document.id)
            document.save()
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
            interaction.interaction_number = "I - " + str(interaction.id)
            interaction.parent_id = witness.id
            interaction.save()
            interaction_form = InteractionForm()
            messages.success(request, 'New Interaction Has Been Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Interaction Has Not Been Created')
    else:
        interaction_form = InteractionForm()
    # Create Relationship to Activity
    if request.method == "POST" and 'witness_activity' in request.POST:
        activity_form = ActivityForm(request.POST)
        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.created_by = request.user
            activity.created_date = timezone.now()
            activity.save()
            activity.parent_id = witness.id
            activity.activity_status = "New"            
            activity.activity_number = "A-" + str(activity.id)
            activity.save()
            activity_form = ActivityForm()
            messages.success(request, 'New Activity Related to Witness Has Been Created', extra_tags='modify /witness_management/modify_activity/' + str(activity.id))
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Activity Related to Witness Has Not Been Created')
    else:
        activity_form = ActivityForm()
    return render(request,
                  'witness_management/witness.html',
                  {'form': form,
                   'document_form': document_form,
                   'interaction_form': interaction_form,
                   'activity_form': activity_form,
                   'witness': witness,
                   'documents': documents,
                   'interactions': interactions,
                   'activities': activities,
                   'modify': 'modify',
                   'title': 'Modify Witness:  ' + str(witness.witness_number)})

def activity_workbench(request):
    activities = Activity.objects.all()
    return render(request,
                  'witness_management/activity_workbench.html',
                  {'activities': activities,
                  'title': 'Activity Workbench'})

def new_activity(request):
    # Query Sets
    form = ActivityForm()
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.created_by = request.user
            activity.created_date = timezone.now()
            activity.save()
            activity.activity_number = "A" + str(activity.id)
            activity.save()
            messages.success(request, 'New Activity Has Been Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Activity Has Not Been Created')
    else:
        form = InteractionForm()
    return render(request,
                  'interaction_management/activity.html',
                  {'form': form,
                   'title': 'New Activity'})

def modify_activity(request, pk):
    # Query Sets
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST" and "master":
        form = ActivityForm(request.POST, request.FILES,
                               instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.modified_by = request.user
            activity.modified_date = timezone.now()
            if activity.parent_id == '':
                activity.parent_id = None
            activity.save()
            activity.activity_number = "A" + str(activity.id)
            activity.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ActivityForm(instance=activity)
    return render(request,
                  'witness_management/activity.html',
                  {'form': form,
                   'activity': activity,
                   'title': 'Activity ' + str(activity.activity_number)})

def document_repository(request):
    documents = Document.objects.all()
    return render(request,
                  'witness_management/document_repository.html',
                  {'documents': documents,
                   'title': 'Document Repository'})

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
            document.document_number = "D-" + str(document.id)
            document.save()
            messages.success(request, 'Document Has Been Modified')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Document Has Not Been Modified')
    else:
        form = DocumentForm(instance=document)
    return render(request,
                  'witness_management/document.html',
                  {'form': form,
                   'document': document,
                   'title': 'Document '})


def interaction_repository(request):
    interactions = Interaction.objects.all()
    return render(request,
                  'witness_management/interaction_repository.html',
                  {'interactions': interactions,
                  'title': 'Interactions Repository'})

def modify_interaction(request, pk):
    # Query Sets
    interaction = get_object_or_404(Interaction, pk=pk)
    if request.method == "POST" and "master":
        form = InteractionForm(request.POST, request.FILES,
                               instance=interaction)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.modified_by = request.user
            interaction.modified_date = timezone.now()
            interaction.save()
            if interaction.parent_id == '':
                interaction.parent_id = None
            interaction.save()
            interaction.interaction_number = "I-" + str(interaction.id)
            interaction.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = InteractionForm(instance=interaction)
    return render(request,
                  'witness_management/interaction.html',
                  {'form': form,
                   'interaction': interaction,
                   'modify': 'modify',
                   'title': ' Modify Interaction: ' + str(interaction.interaction_number)})