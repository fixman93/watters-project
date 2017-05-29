from django.db import models
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from .validators import color_hex


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=25)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(_("Name"), max_length=25)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Dress(models.Model):
    # Price Choices
    HIGH_PRICE = 3
    AVERAGE_PRICE = 2
    SMALL_PRICE = 1
    PRICE_CHOICES = [(HIGH_PRICE, "$$$"),
                     (AVERAGE_PRICE, "$$"),
                     (SMALL_PRICE, "$")
                     ]

    name = models.CharField(_("Name"), max_length=50, unique=True, db_index=True)
    description = models.TextField(_("Description"))
    sku = models.CharField(_("SKU"), max_length=20, unique=True, db_index=True)
    style = models.CharField(_("Style"), max_length=20, unique=True, db_index=True)
    collection = models.ForeignKey("Collection")
    price = models.PositiveSmallIntegerField(_("Price"), choices=PRICE_CHOICES,
                                             default=SMALL_PRICE)
    size = models.ForeignKey("Size")
    colors = models.ManyToManyField("Color")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dresses"


class Part(models.Model):
    dress = models.ForeignKey("Dress", related_name='parts', verbose_name=_("Dress"))
    name = models.CharField(_("Name"), max_length=20)
    colors = models.ManyToManyField("Color")
    position = models.PositiveIntegerField(_("Position"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["position"]


class Size(models.Model):   #Drop?
    name = models.CharField(_("Name"), max_length=50, unique=True)
    size_from = models.PositiveSmallIntegerField(default=0)
    size_to = models.PositiveSmallIntegerField(default=24)

    def __str__(self):
        return "{0}, {1} - {2}w".format(self.name, self.size_from, self.size_to)


class DressImage(models.Model):
    dress = models.ForeignKey("Dress", related_name='images', verbose_name=_("Dress"))
    original = ImageField(_("Original"), upload_to="photos")
    caption = models.CharField(_("Caption"), max_length=200, blank=True)
    color = models.ForeignKey("Color")
    position = models.PositiveIntegerField(_("Position"),
        help_text=_("An image with a first position will be the primary"
                    " image for a product"))

    class Meta:
        ordering = ["position"]
        unique_together = ("dress", "position")
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")

    def __str__(self):
        return "Image of '%s'" % self.dress.name


class Fabric(models.Model):
    dress = models.ForeignKey("Dress", related_name='fabrics', verbose_name=_("Dress"))
    name = models.CharField(_("Name"), max_length=25)
    colors = models.ManyToManyField("Color")
    position = models.PositiveIntegerField(_("Position"))

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("dress", "name")
        ordering = ["position"]

class Color(models.Model):
    name = models.CharField(_("Name"), max_length=25, unique=True)
    hex_code = models.CharField(_("Color"),
                             max_length=7,
                             validators=[color_hex],
                             help_text=_('HEX code like #000000'))

    def __str__(self):
        return self.name
