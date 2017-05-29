import re
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator


_regex_color_hex = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
color_hex = RegexValidator(regex=_regex_color_hex, message=_('HEX color code'))
