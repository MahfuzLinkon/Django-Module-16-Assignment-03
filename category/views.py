from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def add_category(request):
    categoryForm = CategoryForm()
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('add_category')
    else:
        categoryForm = CategoryForm()
    return render(request, 'category_form.html', {'categoryForm': categoryForm})