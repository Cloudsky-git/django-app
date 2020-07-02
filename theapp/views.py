from django.shortcuts import render

def post_list(request):
    return render(request, 'theapp/post_list.html', {})
