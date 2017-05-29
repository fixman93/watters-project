from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from apps.catalogue.models import Dress


class Basket(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def add_product(self, product):
        pass


class Line(models.Model):
    """
    A line of a basket
    """
    basket = models.ForeignKey(Basket, related_name='lines',
                               verbose_name=_("Basket"))
    dress = models.ForeignKey(Dress, related_name='basket_lines',
                              verbose_name=_("Dress"))
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
