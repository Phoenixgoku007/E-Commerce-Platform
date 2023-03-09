from django.db import models

# Create your models here.
'''
collection can have many products

customers can have many orders

order can have many items

cart can have many items

-------------------------------------------------------

For creating onetoone relationship use onetoone attribute

For creating one to many relation use Foreignkey attribute

If I use cascade for on delete all the relevant data get deleted

If I use protect then it will be preserved 



'''

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

#In the above code featured product refers to the product class but it is defined after the collections so have to give a single quotation to the Product ...In case if I change the name from product to something else that won't have any impact here
'''
Since the collection class and product class refer each other one after another reverse relationship can not be done by python so i have disable it by using related name attribute in the above line

'''
class Product(models.Model):
    title=models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True) #it will automatically store the time in which the last change has been made
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)# here protect is used for ondelete so that when a collection got deleted the products will be preserved
    promotions = models.ManyToManyField(Promotion) # manytomany relationship 

class Customer(models.Model):
    MEMBERSHIP_BRONZE= 'B'
    MEMBERSHIP_SILVER= 'S' # instead of changing the letters from inside the array of tuples below we can edit here
    MEMBERSHIP_GOLD= 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ] # created the name in capital to denote that it is a fixed field 

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    

    ''' class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name','first_name']) #for making the db operations more efficient
        ]'''

class Order(models.Model):
    
    PAYMENT_PENDING = 'P' # I am using these variables separately so that if i want to change the notation it is simple 
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True) # Auto populated feature
    payment = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)# protect is used since if customer got deleted orders will be preserved because our sales data requires this to calculate profits


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT) #if order got deleted accidentally order item won't get deleted since we are using protect
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)



class Address(models.Model):# it is the child class which refers to the parent class customer
    street = models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    zip =models.CharField(max_length=255)
    # below i have set the customer as primary key so that there won't be more than one field for the same customer or any kind of duplication
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)# here cascade means if i delete the data of a customer the associated address will also get deleted
    # for one to many relationship
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE) here Foreignkey keyword is used for making this relation


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)# if the cart got deleted all the cartitems also get deleted
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #if the product got deleted the cartitem will also get deleted
    quantity = models.PositiveSmallIntegerField()