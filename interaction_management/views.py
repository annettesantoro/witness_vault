from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Interaction
from django.utils import timezone
from .forms import InteractionForm
# Create your views here.


def interaction_workbench(request):
    interactions = Interaction.objects.all()
    return render(request,
                  'interaction_management/interaction_workbench.html',
                  {'interactions': interactions,
                   'title': 'Interaction Management Workbench'})

def new_interaction(request):
    form = InteractionForm()
    if request.method == "POST":
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.created_by = request.user
            interaction.created_date = timezone.now()
            interaction.save()
            interaction.interaction_number = "W - " + str(interaction.id)
            interaction.save()
            messages.success(request, 'New Interaction Has Been Created', extra_tags='modify modify_interaction/' + str(interaction.id))
            return redirect(interaction_workbench)
        else:
            messages.error(request, 'Interaction Has Not Been Created')
    else:
        form = InteractionForm()
    return render(request,
                  'interaction_management/interaction.html',
                  {'form': form,
                   'title': 'New Interaction'})
                   
def modify_interaction(request, pk):
    # Query Sets
    interaction = get_object_or_404(Interaction, pk=pk)
    if request.method == "POST":
        form = InteractionForm(request.POST, request.FILES,
                               instance=interaction)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.created_by = request.user
            interaction.modified_date = timezone.now()
            interaction.save()
            interaction.interaction_number = "I-" + str(interaction.id)
            interaction.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = InteractionForm(instance=interaction)
    return render(request,
    'interaction_management/interaction.html',
    {'interaction': interaction, 
    'title': 'Modify Interaction: '})

def modify_incident(request, pk):
    # Query Sets
    # Main Interaction Queries
    interaction = get_object_or_404(Interaction, pk=pk)
    # Modify Interaction
    if request.method == "POST" and 'master' in request.POST:
        form = InteractionForm(request.POST, instance=interaction)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.created_by = request.user
            interaction.modified_date = timezone.now()
            interaction.save()
            oldInteraction = Interaction.objects.filter(id = interaction.id)[0]
            interaction.interaction_number = "I-" + str(interaction.id)
            interaction.save()
            messages.success(request, 'Interaction No.' + ' ' + str(interaction.interaction_number) + ' ' + 'Has Been Modified')
            return redirect(request.META['HTTP_REFERER'])            
        else:
            messages.error(request, 'Interaction Record Has Not Been Modified')
    else:
        form = InteractionForm(instance=interaction)
    return render (request,'interaction_management/interaction.html',
    {'form': form,
    'modify': 'modify',
    'title': 'Modify Interaction:  ' + str(interaction.interaction_number)})
