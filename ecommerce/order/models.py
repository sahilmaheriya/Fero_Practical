from django.db import models
from customer.models import Customer
from product.models import Product



class Order(models.Model):
    order_number = models.CharField(max_length=6, null=True, blank=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.all()
            if last_order and last_order.latest('id'):
                last_order_number = int(last_order.latest('id').order_number)
                self.order_number = f'{last_order_number + 1:05d}'
            else:
                self.order_number = '00001'
        super(Order, self).save(*args, **kwargs)
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()