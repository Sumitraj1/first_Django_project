from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html') 

def analyse(request):
   #get the text
   djtext=(request.POST.get('text','default'))

   #check checkbox values
   removepunc=request.POST.get('removepunc','off')
   fullcaps=request.POST.get('fullcaps','off')   
   newlineremover=request.POST.get('newlineremover','off') 
   extraspaceremover=request.POST.get('extraspaceremover','off')
   charactercount=request.POST.get('charactercount','off')
   #check which checkbox is on  

   ##remove punctuation in strings
   if removepunc=="on":
      punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_`'''
      analysed= ""
      for char in djtext:
          if char not in punctuations:
              analysed = analysed + char 
      params={'purpose':'Removed Punctuation','analyzed_text':analysed}
      djtext = analysed
    #   return render(request,'analyze.html',params)
   
   #convert String in Uppercse
   if(fullcaps=="on"):
       analysed=""
       for char in djtext:
           analysed=analysed+char.upper()
       params={'purpose':'Changed to Uppercase','analyzed_text':analysed}
       djtext = analysed
    #    return render(request,'analyze.html',params)
   
   #remove newline from String
   if(newlineremover=="on"):
        analysed=""
        for char in djtext:
           if char!="\n" and char!="\r":
            analysed=analysed+char
        params={'purpose':'New Line Remover','analyzed_text':analysed}
        djtext = analysed
        # return render(request,'analyze.html',params)
   
   #Remove extraSpace From Strings
   if(extraspaceremover=="on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analysed}
        # Analyze the text
        djtext = analysed
        # return render(request, 'analyze.html', params)

        

   #count the charcters in Strings
   if(charactercount=="on"):
       analysed=len(djtext)
       params={'purpose':'Character Count','analyzed_text':analysed}
       djtext = analysed
    #    return render(request,'analyze.html',params)


   if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")         
   
   
   return render(request, 'analyze.html', params)
