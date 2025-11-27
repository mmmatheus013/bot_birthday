from django.shortcuts import render, redirect
from .forms import BirthdaysForm
from .models import Birthdays


def birthday_create(request):
    if request.method == "POST":
        form = BirthdaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("birthday_list")
    else:
        form = BirthdaysForm()
    return render(request, "birthday/forms.html", {"form": form})


def birthday_list(request):
    items = Birthdays.objects.order_by("name")
    return render(request, "birthday/list.html", {"items": items})
