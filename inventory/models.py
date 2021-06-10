# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contacts(models.Model):
    contact_id = models.TextField()  # This field type is a guess.
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone = models.TextField(blank=True, null=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Countries(models.Model):
    country_id = models.TextField()
    country_name = models.TextField()
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Customers(models.Model):
    customer_id = models.TextField()  # This field type is a guess.
    name = models.TextField()
    address = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    credit_limit = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    employee_id = models.TextField()  # This field type is a guess.
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    hire_date = models.TextField()
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    job_title = models.TextField()

    class Meta:
        managed = False
        db_table = 'employees'


class Inventories(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    warehouse = models.ForeignKey('Warehouses', models.DO_NOTHING)
    quantity = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventories'


class Locations(models.Model):
    location_id = models.TextField()  # This field type is a guess.
    address = models.TextField()
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    item_id = models.TextField()  # This field type is a guess.
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.TextField()  # This field type is a guess.
    unit_price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    order_id = models.TextField()  # This field type is a guess.
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    status = models.TextField()
    salesman = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    order_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'orders'


class ProductCategories(models.Model):
    category_id = models.TextField()  # This field type is a guess.
    category_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_categories'


class Products(models.Model):
    product_id = models.TextField()  # This field type is a guess.
    product_name = models.TextField()
    description = models.TextField(blank=True, null=True)
    standard_cost = models.TextField(blank=True, null=True)  # This field type is a guess.
    list_price = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.ForeignKey(ProductCategories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products'


class Regions(models.Model):
    region_id = models.TextField()  # This field type is a guess.
    region_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'regions'


class Warehouses(models.Model):
    warehouse_id = models.TextField()  # This field type is a guess.
    warehouse_name = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouses'
