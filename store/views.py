from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product , Slider , Category , Cart
from django.http import JsonResponse
from django.utils.translation import gettext as _


# Create your views here.

def index(request):

    products = Product.objects.select_related('auther').filter(featured=True)
    sliders = Slider.objects.order_by('order')

    context = {
        'products' : products,
        'sliders' : sliders
    }
    return render(request,'index.html' , context)


def product(request , id):

    product = Product.objects.get(pk=id)

    context={
        'product':product
    }
    return render(request,'product.html',context)


def category(request , cid=None):

    query = request.GET.get('query')    # SEARCH INPUT 1
    cid = request.GET.get( 'category',cid)  # SEARCH INPUT 1

    cat = None
    where = {}
    if cid:
        cat = Category.objects.get(pk=cid)
        where['category_id'] = cid


    if query:
        where['name__icontains'] = query

    products = Product.objects.filter(**where)
    paginator = Paginator(products,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'category' :cat
    }
    return render(request,'category.html' , context)


def cart(request):
    return render(request,'cart.html')

def cart_ubdate(request , pid):
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key
    cart_model = Cart.objects.filter(session=session_id).last()
    if cart_model is None:
        cart_model = Cart.objects.create(session_id=session_id,items=[pid])
    elif pid not in cart_model.items:
        cart_model.items.append(pid)
        cart_model.save()

    return JsonResponse({
        'massage' : _('the product has been added to your cart'),
        'intms_count' : len(cart_model.items)
    })


def cart_remove(request , pid):
    session_id = request.session.session_key

    if not session_id:
        return JsonResponse({})

    cart_model = Cart.objects.filter(session=session_id).last()

    if cart_model is None:
        return JsonResponse({})
    elif pid in cart_model.items:
        cart_model.items.remove(pid)
        cart_model.save()

    return JsonResponse({
        'massage' : _('the product has been reomved from your cart'),
        'intms_count' : len(cart_model.items)
    })


def checkout(request):
    return render(request,'checkout.html')


def checkout_complete(request):
    return render(request,'checkout_complete.html')



