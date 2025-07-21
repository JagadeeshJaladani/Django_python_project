from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'notes/home.html')


from .models import Note
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_important = 'is_important' in request.POST
        Note.objects.create(user=request.user, title=title, content=content, is_important=is_important)
        return redirect('note_list')
    return render(request, 'notes/note_form.html')

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.is_important = 'is_important' in request.POST
        note.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'note': note})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
