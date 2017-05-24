from django.shortcuts import render

def post_list(request):
    return render(request, 'mysystem/post_list.html', {})
