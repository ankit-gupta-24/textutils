from django.shortcuts import render
import string
from django.shortcuts import HttpResponse
from collections import Counter
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

context = {
    "requestedService": '',
    "originalText": '',
    "outputText":''
}
def removePunc(text):
    context['requestedService'] = 'Remove Puctuations'
    allpuncs = string.punctuation
    optext=''
    for char in text:
        if not (char in allpuncs):
            optext +=char
    context['outputText'] = optext

def removeSpaces(text):
    context['requestedService'] = 'Remove Extra Spaces'
    optext = ''
    for i,char in enumerate(text):
        if(i<len(text)-1):
            if not (text[i] == ' ' and text[i+1] == ' '):
                optext += char
        else:
            optext += char
    context['outputText'] = optext

def capitalize(text):
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



def analyze(request):
    service = request.POST.get('services')
    text = request.POST.get('texttoutil')
    
    context['originalText'] = text

    if service == 'removePunc':
        removePunc(text)
    elif service == 'removeSpaces':
        removeSpaces(text)
    elif service == 'capitalize':
        capitalize(text)
    elif service == 'newLineRemover':
        context['requestedService'] = 'New Line Remover'
        context['outputText'] = text.replace("\r\n","")
    elif service == 'uppercase':
        context['requestedService'] = 'Uppercase'
        context['outputText'] = text.upper()
    elif service == 'lowercase':
        context['requestedService'] = 'Lowercase'
        context['outputText'] = text.lower()
    elif service == 'wordCountWP':
        removePunc(text)
        context['requestedService'] = 'word count without punctuations'
        context['outputText'] = len(context['outputText'].split())
    elif service == 'uniqueWC':
        removePunc(text)
        context['requestedService'] = 'unique word count'
        context['outputText'] = len(set(context['outputText'].split()))
    elif service == 'uniqueWord':
        removePunc(text)
        context['requestedService'] = 'unique word'
        context['outputText'] = " ".join(set(context['outputText'].split()))
    elif service == 'freqCount':
        removePunc(text)
        context['requestedService'] = 'frequency of each word'
        context['outputText'] = dict(Counter(context['outputText'].split()))
    elif service == 'letterCount':
        text = text.replace("\r\n","")
        text = text.replace(" ","")
        text = text.replace("\t","")
        removePunc(text)
        context['requestedService'] = 'unique letter count'
        context['outputText'] = len(set(list(context['outputText'])))
    elif service == 'uniqueLetter':
        text = text.replace("\r\n","")
        text = text.replace(" ","")
        text = text.replace("\t","")
        removePunc(text)
        context['requestedService'] = 'unique letter'
        context['outputText'] = "".join(set(list(context['outputText'])))
    else:
        context['requestedService'] = 'Please choose a valid Service'

    return render(request,'output.html',context)
