from django.shortcuts import render,redirect
from base.models import Task,History

# Create your views here.
def home(request):
  all_data= Task.objects.all()
  if not all_data.exists():
    return render(request,'notask.html',{'hist':all_data})
  return render(request,'home.html',{'data':all_data})

def add(request):
  if request.method=='POST':
    title_data=request.POST['title']
    desc_data=request.POST['desc']

    Task.objects.create(title=title_data,desc=desc_data)
  return render(request,'add.html')


def edit(request,pk):

  task = Task.objects.get(id=pk)

  print(task.title) 
  if request.method=='POST':
    title_data=request.POST['title']
    desc_data=request.POST['desc']

    print(title_data,desc_data) 

    task.title=title_data 
    task.desc=desc_data 

    task.save()

    return redirect('home')

  return render(request,'edit.html',{'data':task})

def delete_(request,pk):
  task = Task.objects.get(id=pk)
  History.objects.create(title=task.title,desc=task.desc)
  task.delete()
  return redirect('home')

def history(request):
  hist = History.objects.all()
  if not hist.exists():
    return render(request,'nohis.html',{'hist':hist})
  return render(request,'history.html',{'hist':hist})



def his_del(request,pk):
  his_ = History.objects.get(id=pk)
  his_.delete()
  return redirect('home')

def restore(request,pk):
  restore=History.objects.get(id=pk)
  Task.objects.create(title=restore.title,desc=restore.desc)
  restore.delete()
  return redirect('home')

def del_all(request):
  del_=History.objects.all()
  del_.delete()
  return redirect('history')

def restore_all(request):
  res_=History.objects.all()
  for i in res_:
    Task.objects.create(title=i.title,desc=i.desc)
    i.delete()
  return redirect('history')

