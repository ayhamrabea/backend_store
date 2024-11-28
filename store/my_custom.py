from .models import Category , Cart , Product

def custom(request):
    caterories = Category.objects.order_by('order')
    cart = Cart.objects.filter(session=request.session.session_key).last()

    cart_total = 0
    cart_products = []

    if cart:
        cart_products = Product.objects.filter(pk__in=cart.items)
        for item in cart_products:
            cart_total += item.price

    context = {
        'caterories':caterories,
        'cart_products':cart_products,
        'cart_total': cart_total
    }
    return context


