from django.shortcuts import render

# Create your views here.
def community_view(request):
    
    return render(request, 'community/home.html')

