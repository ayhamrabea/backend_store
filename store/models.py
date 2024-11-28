from django.db import models
from django.utils.translation import gettext as _
from django.contrib.sessions.models import Session
from project import settings
from checkout.models import Transaction

# Create your models here.

class Category(models.Model):

    name = models.CharField(_("name"), max_length=50)
    featured = models.BooleanField(_("featured") , default=False)
    order = models.IntegerField(_("order") , default=1)
    created_at = models.DateField(_(""), auto_now_add=True)
    updated = models.DateField(_(""), auto_now=True)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name


class Auther(models.Model):

    name = models.CharField(_("name"), max_length=50)
    bio = models.TextField(_("bio"))
    created_at = models.DateField(_(""), auto_now_add=True)
    updated = models.DateField(_(""), auto_now=True)
    

    class Meta:
        verbose_name = _("Auther")
        verbose_name_plural = _("Authers")

    def __str__(self):
        return self.name
    

class Product(models.Model):

    name = models.CharField(_("name"), max_length=50)
    short_description = models.TextField(_("short_description") , null=True)
    description = models.TextField(_("description") , null=True)
    image = models.ImageField(_("image"))
    pdf_file = models.FileField(_("pdf_file"),null=True)
    price = models.FloatField(_("price"))
    featured = models.BooleanField(_("featured") , default=False)
    created_at = models.DateField(_(""), auto_now_add=True)
    updated = models.DateField(_(""), auto_now=True)
    category = models.ForeignKey(Category, verbose_name=_(""), on_delete=models.PROTECT)
    auther = models.ForeignKey(Auther, verbose_name=_(""), on_delete=models.SET_NULL , null=True)    # سيتم تحديد null أذا قمنا بحذف الكاتب

    @property
    def pdf_file_url(self):
        return  settings.SITE_URL + self.pdf_file.url


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Order(models.Model):

    # transaction = models.OneToOneField(Transaction, verbose_name=_(""), on_delete=models.ProtectedError , null=True)
    customer = models.JSONField(_("customer"), default=dict)
    total = models.JSONField(_("total"), default=dict)
    created_at = models.DateField(_(""), auto_now_add=True)
    updated = models.DateField(_(""), auto_now=True)
    

    @property
    def customer_name(self):
        return self.customer['first_name'] + ' ' + self.customer['last_name']

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.id)
    


class OrderProduct(models.Model):

    prder = models.ForeignKey(Order, verbose_name=_(""), on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)
    price = models.FloatField(_("price"))
    created_at = models.DateField(_(""), auto_now_add=True)
    


class Cart(models.Model):

    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

class Slider(models.Model):

    title = models.CharField(_("title"), max_length=50)
    subtitle = models.TextField(_("subtitle") , null=True)
    image = models.ImageField(_("image") , null=True)
    order = models.IntegerField(_("order") , default=1)
    created_at = models.DateField(_(""), auto_now_add=True)
    updated = models.DateField(_(""), auto_now=True)

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")

    def __str__(self):
        return str(self.id)
