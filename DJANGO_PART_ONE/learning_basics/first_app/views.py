from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse("<h4>Index menu:<h4><p></p><a href='/firstway'>First way</a><p></p><a href='/secondway'>Second way</a>")

# def first_way_url(request):
#     text1 = 'Jestem First_Way'
#     text2 = 'zostałem wstrzyknięty do szablonu pliku html'
#     contextDict = {
#         'textList':[text1,text2],
#         }
#     return render(request, 'first_app/way.html', contextDict)
#
# def second_way_url(request):
#     text1 = 'Jestem Second_Way'
#     text2 = 'zostałem wstrzyknięty do szablonu pliku html'
#     contextDict = {
#         'textList':[text1,text2],
#         }
#     return render(request, 'first_app/way.html', contextDict)

def one_way_url(request, way):
    if way == "firstway":
        text1 = 'Jestem First_Way'
    elif way == "secondway":
        text1 = 'Jestem Second_Way'
    text2 = 'zostałem wstrzyknięty do szablonu pliku html'
    contextDict = {
        'textList':[text1,text2],
        }
    return render(request, 'first_app/way.html', contextDict)
