from django.shortcuts import render, get_object_or_404, redirect

from .models import Item

# Create your views here.
#CRUD operations
#Create
def create_item(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')

        Item.objects.create(name=name, description=description, price=price)

        return redirect('item_list')
    
    return render(request, template_name='crudApp/item_form.html')

#Read
def item_list(request):
    items=Item.objects.all()
    return render(request, template_name='crudApp/item_list.html', context={'items':items})

#Update
def update_item(request, pk):
    item=get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')

        item.name=name
        item.description=description
        item.price=price
        item.save()

        return redirect('item_list')
    
    return render(request, template_name='crudApp/item_form.html', context={'item':item})

#Delete

def delete_item(request, pk):
    item=get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    
    return render(request, template_name='crudApp/item_confirm_delete.html', context={'item':item})