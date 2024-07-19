from django.shortcuts import render,HttpResponse
#19

def index(request):
    return render(request,'index.html')

def analyze(request):
    if request.method == "GET":
        #get the text
        text = request.GET.get('text',"default")

        #check the checkbox values
        rp = request.GET.get('rp','off')
        fc = request.GET.get('fc','off')
        lc = request.GET.get('lc','off')
        nlr = request.GET.get('nlr','off')
        sr = request.GET.get('sr','off')
        cc = request.GET.get('cc','off')

        if rp == 'on':
            eg='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            analyzed=""
            for s in text:
                if s not in eg:
                    analyzed+=s
                
            param ={'purpose':'Remove Punctuations','ans':analyzed}
            text = analyzed
        
        if fc == 'on':
            analyzed = ""
            for char in text:
                analyzed = analyzed + char.upper()
            
            param ={'purpose':'Change To Uppercase','ans':analyzed}
            text = analyzed

        if lc == 'on':
            analyzed = ""
            for char in text:
                analyzed = analyzed + char.lower()
            
            param ={'purpose':'Change To Uppercase','ans':analyzed}
            text = analyzed
        
        if nlr == 'on':
            analyzed = ""
            for char in text:
                if char!="\n" and char!="\r":
                    analyzed = analyzed + char
            
            param ={'purpose':'Remove New Line','ans':analyzed}
            text = analyzed

        if sr == 'on':
            analyzed = " ".join(text.split())

            
            param ={'purpose':'ExtraSpace Remover','ans':analyzed}
            text = analyzed

        if cc == 'on':
            countt=0
            for i in text:
                if not (i == ' '):
                    countt+=1
            analyzed = f"The Number of Characters in '{text}' are--{countt}"

            param ={'purpose':'Character Counter','ans':analyzed}


        if(rp != 'on' and fc != 'on' and lc != 'on' and nlr != 'on' and sr != 'on' and cc != 'on'):
            return render(request, 'error.html')
    
        return render(request,'analyze.html',param)

        


    return render(request,'analyze.html')