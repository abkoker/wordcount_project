#from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    countword = fulltext.split()

    worddictionary = {} # create empty dictionary

    for word in countword:      # for loop for the disctinary
        if word in worddictionary:
            worddictionary[word] += 1 #if there is anythin inside, then increase it value
        else:
            worddictionary[word] = 1 #add to it value

    wordsorted = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
# return render values
    return render(request, 'count.html',
    {'fulltext': fulltext,
    'count': len(countword),
    'wordsorted': wordsorted})

def about(request):
    return render(request, 'about.html')
