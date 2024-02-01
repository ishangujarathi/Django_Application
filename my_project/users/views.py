from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()   #creating the user, if the form is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You should now be able to Log In!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})  #directly rendering a template (users/register.html) and as a context, we are passing the instance of usercreation form as a dictionary with key = form and value = form(instance of the usercreationform, which is provided by django)

@login_required
def profile(request):
    return render(request, 'users/profile.html')
