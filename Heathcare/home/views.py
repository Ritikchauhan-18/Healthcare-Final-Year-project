from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        return render(request, 'home/result.html')
    return render(request, 'home/index.html')  # This renders home/index.html

# def result(request):
    # return render(request, 'home/ml.html')  # This renders home/index.html
