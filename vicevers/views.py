from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def reverse(request):
    user_text = request.GET['usertext']
    rev_text = user_text[::-1]
    return render(request,'reverse.html',{'usertext': user_text, 'reversedtext': rev_text})
