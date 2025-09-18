from django.shortcuts import render, redirect, get_object_or_404  

from .models import Vibe

from django.contrib.auth.decorators import login_required 
from .forms import VibeForm

from .forms import UserRegistrationForm

from django.contrib.auth import login

# Create your views here.
def index(request) : 
  return render(request, 'index.html')

def vibe_list(request) :
  vibes = Vibe.objects.all().order_by('-created_at')
  return render(request, 'vibe_list.html', {'vibes' : vibes})

@login_required # only for logged in users
def vibe_create(request):
  if request.method == "POST":
    vibe_form = VibeForm(request.POST, request.FILES)

    if vibe_form.is_valid() : # check if it is valid
      vibe = vibe_form.save(commit=False) # save it but don't commit
      vibe.user = request.user # add user to the vibe
      vibe.save() # this will save vibe to database

      # formset.instance = vibe  # link media to vibe
      # formset.save()
      return redirect("vibe_list")  #redirect to other endpoint
    
  else: # empty Form 
    vibe_form = VibeForm()
    # formset = VibeMediaFormSet()

  return render(request, "vibe_form.html", {
    "vibe_form": vibe_form,
    # "formset": formset,
  })
  
@login_required
def vibe_edit(request, vibe_id) :
  vibe = get_object_or_404(Vibe, pk=vibe_id, user=request.user)
  
  if request.method == 'POST': 
    vibe_form = VibeForm(request.POST, request.FILES, instance = vibe)
    # formset = VibeMediaForm(request.POST, request.FILES, instance = vibe)
    # instance is used to update the already having entry in database
    
    if(vibe_form.is_valid()) : 
      vibe_form.save()
      return redirect("vibe_list") # redirect to your vibe list page
  else :
    vibe_form = VibeForm(instance=vibe)
    # formset = VibeMediaFormSet(instance=vibe)
  return render(request, "vibe_form.html", {
    "vibe_form": vibe_form,
    # "formset": formset,
  })
  
@login_required
def vibe_delete(request, vibe_id) : 
  vibe = get_object_or_404(Vibe, pk = vibe_id, user = request.user)
  
  if request.method == "POST" : 
    vibe.delete()
    return redirect("vibe_list")
  return render(request, "vibe_confirm_delete.html", {"vibe" : vibe})

# user views

def register(request) :
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)

    if form.is_valid() :
      user = form.save(commit=False) 
      user.set_password(form.cleaned_data['password1'])
      user.save()
      
      login(request, user)
      return redirect("vibe_list")
    
  else: 
    form = UserRegistrationForm()

  return render(request, "registration/register.html", {
    'form' : form
  })


# general creating entry

# def vibe_create(request) : 
#   if request.method == 'POST': 
#     pass
#   else :
#     form = VibeForm()
    
#   return render(request, 'vibe_form.html', {'form' : form})