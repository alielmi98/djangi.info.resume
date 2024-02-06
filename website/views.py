from django.shortcuts import render

info={"name":"Ali Elmi", "email":"ali.elmi77@yahoo.com","phone":"+989146882659"}
def index_view(request):
    return render(request,'index.html', info)
# Create your views here.
