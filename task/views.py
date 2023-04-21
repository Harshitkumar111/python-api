import json
from django.shortcuts import render,redirect
from task.models import Users
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):  
    newsdata = Users.objects.all()
    per_page = 4
    obj_paginator = Paginator(newsdata,per_page)  
    first_page = obj_paginator.page(1).object_list    
    page_range = obj_paginator.page_range
    context = {
    'obj_paginator':obj_paginator,
    'first_page':first_page,
    'page_range':page_range
    }
    if request.method == 'POST':
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values('id', 'Username','First_name','Last_name','email'))
        return JsonResponse({"results":results})
    return render(request, 'index.html',context)
def save(request):
    Uname=request.POST['name']
    First_name=request.POST['fname']
    Last_name=request.POST['lname']
    email=request.POST['email']
    data =  Users.objects.create(Username=Uname,First_name=First_name,Last_name=Last_name,email=email)
    LastInsertId = (Users.objects.last()).id
    mydata = list(Users.objects.filter(id=LastInsertId).values())
    if data:
        return HttpResponse(json.dumps(mydata),content_type="application/json")
    else:
        return JsonResponse({'status':0,'msg':"fail"}) 
def api(request,id):   
    mydata = list(Users.objects.filter(id=id).values())    
    return HttpResponse(json.dumps(mydata),content_type="application/json")
def update(request,id):
    ids=request.POST['id']
    Uname=request.POST['name']
    First_name=request.POST['fname']
    Last_name=request.POST['lname']
    email=request.POST['email']
    mydata = Users.objects.filter(id=ids).update(Username=Uname,First_name=First_name,Last_name=Last_name,email=email)   
    mydata = list(Users.objects.filter(id=ids).values())
    if mydata:
        return HttpResponse(json.dumps(mydata),content_type="application/json")
    else:
        return JsonResponse({'status':0,'msg':"fail"})
def destroy(request,id):
    deleteid=request.POST['deleteuser']
    delete = list(Users.objects.get(id=deleteid).delete()) 
    return JsonResponse({'id':deleteid,'status':"1",'msg':"Delete Success"})