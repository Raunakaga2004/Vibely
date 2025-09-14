from django.shortcuts import render, redirect, get_object_or_404   # ✅ redirect was missing

from .models import Vibe, VibeMedia

from django.contrib.auth.decorators import login_required  # optional but recommended
from .forms import VibeForm, VibeMediaForm, VibeMediaFormSet  # ✅ add the dot for relative import


# Create your views here.
def index(request) : 
  return render(request, 'index.html')

def vibe_list(request) :
  vibes = Vibe.objects.all().order_by('-created_at')
  return render(request, 'vibe_list.html', {'vibes' : vibes})

@login_required # only for logged in users
def create_vibe(request):
  if request.method == "POST":
    vibe_form = VibeForm(request.POST)
    formset = VibeMediaFormSet(request.POST, request.FILES)

    if vibe_form.is_valid() and formset.is_valid():
      vibe = vibe_form.save(commit=False)
      vibe.user = request.user
      vibe.save()

      formset.instance = vibe  # link media to vibe
      formset.save()
      return redirect("vibe_list")  # ✅ make sure you have a urlpattern named 'vibe_list'
  else:
    vibe_form = VibeForm()
    formset = VibeMediaFormSet()

  return render(request, "create_vibe.html", {
    "vibe_form": vibe_form,
    "formset": formset,
  })