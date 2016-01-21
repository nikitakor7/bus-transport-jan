from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    BusNo = models.CharField(max_length=100, blank=True, default='KA')
    BusRoute = models.TextField()
    latitude = models.CharField(max_length=100, blank=True, default='32')
    longitude = models.CharField(max_length=100, blank=True, default='24')
    time = models.CharField(max_length=100, blank=True, default='12.20')

    class Meta:
        ordering = ('created',)
        
"""def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        BusNo = self.BusNo and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)"""


    
