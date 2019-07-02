from django.shortcuts import render
from registration.forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/board')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})
