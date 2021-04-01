from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
import datetime
import pytz
from django import forms

TIME = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.plated_end_at = datetime.datetime.now() + datetime.timedelta(days=15)
            post.save()
        return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})


def order_delete(request, a_id):
    try:
        author = Order.objects.get(id=a_id)
        author.delete()
    except Order.DoesNotExist:
        # LOGGER.error("User does not exist")
        pass
    return redirect('order_list')


def order_update(request, a_id):
    if request.method == "POST":
        author = Order.objects.get(id=a_id)
        form = OrderForm(request.POST, instance=author)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('order_list')
    else:
        author = Order.objects.get(id=a_id)
        form = OrderForm(instance=author)
    return render(request, 'order/create_order.html', {'form': form})
