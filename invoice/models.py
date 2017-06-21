from django.db import models
import datetime


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    abn = models.BigIntegerField(unique=True)
    pricepersticker = models.DecimalField(max_digits=3, decimal_places=2)
    contactname = models.CharField(blank=True, max_length=100)
    contactphone = models.CharField(max_length=10, blank=True)
    billingaddress = models.TextField(blank=True)
    billingemail = models.EmailField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"%s" % (self.name)


class Suburb(models.Model):
    ACT = 'ACT'
    NSW = 'NSW'
    NT = 'NT'
    QLD = 'QLD'
    SA = 'SA'
    TAS = 'TAS'
    VIC = 'VIC'
    WA = 'WA'
    STATE_CHOICES = (
        (ACT, 'ACT'),
        (NSW, 'NSW'),
        (NT, 'NT'),
        (QLD, 'QLD'),
        (SA, 'SA'),
        (TAS, 'TAS'),
        (VIC, 'VIC'),
        (WA, 'WA'),
    )
    name = models.CharField(max_length=250, unique=True)
    postcode = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default=WA)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"%s (%s)" % (self.name, self.state)


class Location(models.Model):
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250, unique=True)
    suburb = models.ForeignKey('Suburb')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"%s - %s" % (self.name, self.suburb.name)


class Store(models.Model):
    company = models.ForeignKey('Company')
    location = models.ForeignKey('Location')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['company']

    def __str__(self):
        return u"%s:%s(%s)" % (self.company.name, self.location.name, self.location.suburb.name)


class StickerOrder(models.Model):
    TWENTYFIVE = 25
    FIFTY = 50
    HUNDRED = 100
    QTY_CHOICE = (
        (TWENTYFIVE, '25'),
        (FIFTY, '50'),
        (HUNDRED, '100'),
    )
    store = models.ForeignKey('Store')
    date = models.DateField(default=datetime.datetime.today)
    qty = models.PositiveSmallIntegerField(choices=QTY_CHOICE, default=FIFTY)
    stickerstart = models.BigIntegerField()
    stickerend = models.BigIntegerField()
    signed = models.NullBooleanField(null=True)
    printed = models.BooleanField(default=False)

    class Meta:
        unique_together = (("store", "stickerstart"), ("store", "stickerend"),)

    def __str__(self):
        return u"%s:%s %s - %s (%s+%s)" % (
        self.id, self.store.company.name, self.store.location.name, self.date, self.stickerstart, self.qty)
