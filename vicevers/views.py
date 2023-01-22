from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    number_words = len(words)
    rev_text = user_text[::-1]
    print(request.GET['usertext'])
    return render(request,'reverse.html',{'usertext': user_text, 'reversedtext': rev_text, "number_words": number_words})
