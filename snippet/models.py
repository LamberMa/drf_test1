from django.db import models


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# 下面的几行代码是处理代码高亮的，不好理解，但是没有关系，它并不重要
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0])for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    linenos = models.BooleanField(default=False, verbose_name='是否显示行号')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created', )