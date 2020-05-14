from django.shortcuts import render
import string
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    
def analyze(request):
    service = request.POST.get('services')
    text = request.POST.get('texttoutil')
    context = {
        "requestedService": '',
        "originalText": '',
        "outputText":''
    }
    context['originalText'] = text

    if service == 'removePunc':
        context['requestedService'] = 'Remove Puctuations'
        allpuncs = string.punctuation
        optext=''
        for char in text:
            if not (char in allpuncs):
                optext +=char
        context['outputText'] = optext

    elif service == 'removeSpaces':
        context['requestedService'] = 'Remove Extra Spaces'
        optext = ''
        for i,char in enumerate(text):
            if(i<len(text)-1):
                if not (text[i] == ' ' and text[i+1] == ' '):
                    optext += char
            else:
                optext += char
        context['outputText'] = optext

    elif service == 'capitalize':
        context['requestedService'] = 'Cpitalize Each Word'
        flag=False
        optext = text[0].upper()
        for i in range(1,len(text)):
            if text[i] == ' ' or text[i] == '\n':
                flag = True
                optext += text[i]
            elif flag == True:
                optext +=text[i].upper()
                flag=False
            else:
                optext +=text[i].lower()
        context['outputText'] = optext

    elif service == 'newLineRemover':
        context['requestedService'] = 'New Line Remover'
        context['outputText'] = text.replace("\r\n","")

    elif service == 'uppercase':
        context['requestedService'] = 'Uppercase'
        context['outputText'] = text.upper()

    elif service == 'lowercase':
        context['requestedService'] = 'Lowercase'
        context['outputText'] = text.lower()
        
    else:
        context['requestedService'] = 'Please choose a valid Service'

    return render(request,'output.html',context)
