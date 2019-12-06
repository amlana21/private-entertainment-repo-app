from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import ItemTypes,Items,SourceType,ListTypes
import json
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse("Project 3: TODO")

def logout_view(request):
    logout(request)
    return redirect('homepage')

def additems(request):
    print('price')
    # print(request.POST.getlist('lstnme'))
    itmnme=request.POST.get('itmnme')
    srcnme=request.POST.getlist('srcnme')
    lstnme=request.POST.getlist('lstnme')
    print(lstnme)
    Category=request.POST.get('Category')
    prce=request.POST.get('prce')
    rsllprce=request.POST.get('rsllprce')
    itmprrty=request.POST.get('itmprrty')


    itmcreated=Items.objects.create(itemname=itmnme,typeofoitem_id=Category,price=prce,resellprice=rsllprce,priority=itmprrty)

    for v in srcnme:
        val=SourceType.objects.get(pk=v)
        itmcreated.source.add(val)

    for v in lstnme:
        val=ListTypes.objects.get(pk=v)
        itmcreated.listadded.add(val)

    context={
        'itemtypesqry':datatodict(ItemTypes.objects.all().values()),
        'itemsqry':multitodict(Items.objects.all()),
        'itemsorig':getprtydict(),
        'srctype':datatodict(SourceType.objects.all()),
        'listsqry':datatodict(ListTypes.objects.all())
    }

    # return render(request,'index.html',context)
    return redirect('homepage')
    
@login_required
def homepage(request):

    context={
        'itemtypesqry':datatodict(ItemTypes.objects.all().values()),
        'itemsqry':multitodict(Items.objects.all()),
        'itemsorig':getprtydict(),
        'srctype':datatodict(SourceType.objects.all()),
        'listsqry':datatodict(ListTypes.objects.all())
    }

    return render(request,'index.html',context)
    # return redirect('index')



def searchitems(request):
    if request.method == 'POST':
        print(request.POST.get('srchTxt'))
        srchTxt=request.POST.get('srchTxt').lower()
        itmdata=multitodict(Items.objects.all())
        itmresp=[]
        for itm in itmdata:
            added={}
            if srchTxt in itm['itemname'].lower():
                itmresp.append(itm)
        context={
        'itemtypesqry':datatodict(ItemTypes.objects.all().values()),
        'itemsqry':itmresp,
        'itemsorig':getprtydict(),
        'srchvlues':str(srchTxt),
        'srctype':datatodict(SourceType.objects.all()),
        'listsqry':datatodict(ListTypes.objects.all())
        # 'srchrslts':itmresp
         }
        # return redirect('index',context)
        return render(request, 'index.html', context)
   

def multitodict(inptqry):
    otpt=[]
    
    for itm in inptqry:
        added={}
        added['id']=itm.id
        added['itemname']=itm.itemname
        added['source']=itm.source.all()
        added['listadded']=itm.listadded.all()
        added['typeofoitem']=itm.typeofoitem
        added['price']=itm.price
        added['resellprice']=itm.resellprice
        added['priority']=itm.getpriority()
        otpt.append(added)
    return otpt

def datatodict(inptqry):
    otpt=[]
    for itm in inptqry:

        # print(itm)
        otpt.append(itm)
    return otpt

def getprty():
    itemobj=Items()
    return list(itemobj.getpriorityval())

def getprtydict():
    itemobj=Items()
    return list(itemobj.getprioritydict())