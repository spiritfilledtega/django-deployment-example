from django.shortcuts import render
from appTwo.models import AccessRecord, User
from appTwo import forms
# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')

def user(request):
    usus = User.objects.order_by('first_name')
    return render(request, 'appTwo/user.html', {'user_page':usus})

def access(request):
    anc = AccessRecord.objects.order_by('date')
    return render(request, 'appTwo/access.html', {'acc_rec':anc})

def formed(request):
    fom = forms.FormName()

    if request.method == 'POST':
        fom = forms.FormName(request.POST)

        if fom.is_valid():
            fom.save(commit = True)
            return index(request)

        else:
            print('form is not valid')




    return render(request, 'appTwo/forms.html', {'form_page': fom})
