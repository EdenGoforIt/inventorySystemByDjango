# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alert(models.Model):
    alertid = models.AutoField(db_column='AlertId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    alerttype = models.CharField(db_column='AlertType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alertdate = models.DateTimeField(db_column='AlertDate', blank=True, null=True)  # Field name made lowercase.
    alertdescription = models.CharField(db_column='AlertDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alert'
        app_label = 'inventory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = 'inventory'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        app_label = 'inventory'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        app_label = 'inventory'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        app_label = 'inventory'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        app_label = 'inventory'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        app_label = 'inventory'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        app_label = 'inventory'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        app_label = 'inventory'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'inventory'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        app_label = 'inventory'


class Order(models.Model):
    orderid = models.AutoField(db_column='OrderId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    first = models.CharField(db_column='First', max_length=255)  # Field name made lowercase.
    middle = models.CharField(db_column='Middle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last = models.CharField(db_column='Last', max_length=255)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductId')  # Field name made lowercase.
    numbershipped = models.IntegerField(db_column='NumberShipped')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'
        app_label = 'inventory'


class Product(models.Model):
    productid = models.AutoField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=255)  # Field name made lowercase.
    productlabel = models.CharField(db_column='ProductLabel', max_length=255)  # Field name made lowercase.
    startinginventory = models.IntegerField(db_column='StartingInventory')  # Field name made lowercase.
    inventoryreceived = models.IntegerField(db_column='InventoryReceived')  # Field name made lowercase.
    inventoryshipped = models.IntegerField(db_column='InventoryShipped')  # Field name made lowercase.
    inventoryonhand = models.IntegerField(db_column='InventoryOnHand')  # Field name made lowercase.
    minimumrequired = models.IntegerField(db_column='MinimumRequired')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
        app_label = 'inventory'


class Purchase(models.Model):
    purchaseid = models.AutoField(db_column='PurchaseId', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductId')  # Field name made lowercase.
    numberreceived = models.IntegerField(db_column='NumberReceived')  # Field name made lowercase.
    purchasedate = models.DateField(db_column='PurchaseDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase'
        app_label = 'inventory'


class Supplier(models.Model):
    supplierid = models.AutoField(db_column='SupplierId', primary_key=True)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'
        app_label = 'inventory'
