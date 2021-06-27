from django.shortcuts import render, get_object_or_404
from .models import Blogg

def bloghome(request):
    #allblogs=Blogg.objects.all() #recent blog will be at last
    allblogs=Blogg.objects.order_by('-mydatetime')
    #allblogs=Blogg.objects.order_by('-mydatetime')[:2] #to limit the view till 0,1
    return render(request, 'blog/all_blogs.html',{'keyblogs':allblogs})

def details(request,blog_id):
    alldtls=get_object_or_404(Blogg,pk=blog_id) #pk is primary key
    return render(request,'blog/details.html',{'ids':alldtls})
