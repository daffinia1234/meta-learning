from django.shortcuts import render
from Test.forms import Addform
from Test.models import Addproperty

# Create your views here.
def viewform(request):
    property = []

    form=Addform(request.GET)
    if form.is_valid():
        location=form.cleaned_data.get('location')
        if location:
            property=Addproperty.objects.all()
            property=property.filter(location__icontains=location)
    return render(request,'filter.html',{'property':property,'form':form})
