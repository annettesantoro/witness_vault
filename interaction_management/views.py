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
                  'title': 'Interactions Repository'})

def new_interaction(request):
    # Query Sets
    form = InteractionForm()
    if request.method == "POST":
        form = InteractionForm(request.POST, request.FILES)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.created_by = request.user
            interaction.parent_id = interaction.id            
            interaction.created_date = timezone.now()
            interaction.save()
            interaction.interaction_number = "I" + str(interaction.id)
            interaction.save()
            messages.success(request, 'New Interaction Has Been Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'New Interaction Has Not Been Created')
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
            interaction.modified_by = request.user
            interaction.modified_date = timezone.now()
            if interaction.parent_id == '':
                interaction.parent_id = None
            interaction.save()
            interaction.interaction_number = "I" + str(interaction.id)
            interaction.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = InteractionForm(instance=interaction)
    return render(request,
                  'interaction_management/interaction.html',
                  {'form': form,
                   'interaction': interaction,
                   'title': ' Modify Interaction ' })