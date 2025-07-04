from django.shortcuts import render

def grocery_view(request):
    grocery_items = {'milk': 10, 'bread': 20, 'egg': 15}
    if request.method == "POST":
        selected = request.POST.getlist('items')
        selected_item = {item: grocery_items[item] for item in selected}
        total = sum(selected_item.values())
        return render(request, 'selected.html', {
            'selected_item': selected_item,
            'total': total
        })
    return render(request, 'grocery.html', {'items': grocery_items})


