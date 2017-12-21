from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from .forms import EventForm, UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Event

# Create your views here.
def login_page(request):
    return render(request, 'planner/login_page.html')

def event_overview(request):
    events = Event.objects.filter(author = request.user)
    return render(request, 'planner/event_overview.html', {'events': events})

def event_detail(request, pk):
    detail = get_object_or_404(Event, pk=pk)
    return render(request, 'planner/event_detail.html', {'detail': detail})

def event_delete(request, pk):
    instance = Event.objects.get(id=pk)
    instance.delete()
    return redirect('event_list')
    return render(request, 'planner/event_list.html', {'instance': instance})

def event_edit(request, pk):
    edit = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=edit)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', pk=edit.pk)
    else:
        form = EventForm(instance=edit)
    return render(request, 'planner/event_edit.html', {'form': form})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'planner/event_edit.html', {'form': form})

def event_list(request):
    events = Event.objects.filter(author = request.user)
    return render(request, 'planner/event_list.html', {'events': events})

def login_view(request):
    print(request.user.is_authenticated())

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('event_overview')

    return render(request, "planner/login_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "planner/logout_form.html", {})

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect('login_view')

    return render(request, "planner/register_form.html", {"form": form})
