from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def removePuncDef(text: str):
    punctuation = '''!"#$%&'()*+,z-./:;<=>?@[\]^_`{|}~'''
    returnText = ""
    for char in text:
        if char not in punctuation:
            returnText = returnText + char
    return returnText


def upperCaseDef(text: str):
    returnText = ""
    for char in text:
        returnText = returnText + char.upper()
    return returnText


def newLineRemoveDef(text: str):
    returnText = []
    for char in text:
        if char != '\n':
            if char == '\r':
                returnText.append(' ')
            else:
                returnText.append(char)
        else:
            pass

    return ''.join(returnText)


def extraSpaceRemoveDef(text: str):
    returnText = ""
    for ind, char in enumerate(text):
        if not (text[ind] == " " and text[ind + 1] == " "):
            returnText = returnText + char

    return returnText


def charCount(text: str):
    i = 0
    for char in text:
        i = i + 1
    return i


def analyzed(request, ):
    inputText = request.GET.get('text', 'default')
    removePunc = request.GET.get('removePunc', 'off')
    upperCase = request.GET.get('upperCase', 'off')
    newLineRemove = request.GET.get('newLineRemove', 'off')
    extraSpaceRemove = request.GET.get('extraSpaceRemove', 'off')

    purpose = []
    analyzedText = inputText

    if removePunc == "on":
        purpose.append("Remove Punctuation")
        result = removePuncDef(inputText)
        analyzedText = result
    if upperCase == "on":
        purpose.append("UPPER CASE")
        result = upperCaseDef(analyzedText)
        analyzedText = result
    if newLineRemove == "on":
        purpose.append("New Line Remover")
        result = newLineRemoveDef(analyzedText)
        analyzedText = result

    if extraSpaceRemove == "on":
        purpose.append("Extra Space Remove")
        result = extraSpaceRemoveDef(analyzedText)
        analyzedText = result

    if len(purpose) == 0:
        return HttpResponse("Please check any checkBoxes")

    count = charCount(analyzedText)

    strPurpose = ", ".join(purpose)

    params = {
        "purpose": strPurpose,
        "analyzedText": analyzedText,
        "count": count
    }

    return render(request, 'analyzed.html', params)
