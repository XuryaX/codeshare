from django.db import models
from pygments import highlight,lexers
from pygments.formatters.html import HtmlFormatter
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown
import datetime

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    lang = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.lang)


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    high_code = models.TextField(editable=False)
    tags = TagField()
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.high_code = self.highlight()
        super(Snippet,self).save(force_insert,force_update)

    def highlight(self):
        return highlight(self.code,self.language.get_lexer(),HtmlFormatter(linenos=True))