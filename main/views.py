from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406347380',
        'name': 'Dery Andreas Tampubolon',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)