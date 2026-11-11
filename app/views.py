from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



#def insert_topic(request):
   # tn=input('Enter Topic')
    #TTO=Topic.objects.get_or_create(topic_name=tn)
    #if TTO[1]:
     #   return HttpResponse(f'{tn} is created')
    #else:
     #   return HttpResponse(f'{tn} is already exits')

#def insert_webpage(request):
 #   tn=input('Enter topic Name')
  #  LTO=Topic.objects.filter(topic_name=tn)
   #    TO=LTO[0]
    #   url=input('enter url')
     #   email=input('enter email')
      #  TWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
       # if TWO[1]:
        #    return HttpResponse(f'{tn} created')
        #else:
         #    return HttpResponse(f'{tn} present')

    #else:
     #   return HttpResponse('Topic is Not Present')  


#def insert_access(request):


   # tn=input('enter tn')
    #TO=Topic.objects.get_or_create(topic_name=tn)[0]
    #TO.save()

#    n=input('enter name')  
 #  e=input('enter email') 
   #WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    #WO.save()   
    #d=input('enter date')
    #a=input('enter author')

    #AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    #AO.save()

    #return HttpResponse('Access Is Created')  


def display_topics(request):
    QSLTO=Topic.objects.all()
    d= { 'QSLTO': QSLTO}
    return render(request,'display_topics.html',d)















