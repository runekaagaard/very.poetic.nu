from django.db import models as m
from django.contrib.auth.models import User

class Poem(m.Model):
    user = m.ForeignKey(User, editable=False)
    title = m.CharField(max_length=80)
    date = m.DateField(help_text="On the format YYYY-MM-DD, e.g. 2011-01-20.")
    content = m.TextField()
