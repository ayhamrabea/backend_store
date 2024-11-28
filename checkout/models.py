from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class TransactionStatus(models.IntegerChoices):
    Pending = 0 , _('Pending')
    Comleted = 1 , _('Comleted')


class PaymentMethod(models.IntegerChoices):
    Stripe = 0 , _('Stripe')
    Paypal = 1 , _('Paypal')




class Transaction(models.Model):

    session = models.CharField(_("session"), max_length=50)
    amount = models.FloatField(_("amount"))
    items = models.JSONField(_("items"), default=dict)
    customer = models.JSONField(_("customer"), default=dict)
    status = models.IntegerField(_("status") ,choices=TransactionStatus.choices , default=TransactionStatus.Pending)
    payment_method = models.IntegerField(_("paymentmethod") ,choices=PaymentMethod.choices , default=None)
    created_at = models.DateField(_(""), auto_now_add=True) 
    updated = models.DateField(_(""), auto_now=True)


    @property
    def customer_name(self):
        return self.customer['first_name'] + ' ' + self.customer['last_name']
    @property
    def customer_email(self):
        return self.customer['email'] 

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    # def __str__(self):
    #     return self.name

