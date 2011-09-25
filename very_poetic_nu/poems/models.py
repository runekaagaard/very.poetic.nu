from django.db import models as m
from django.contrib.auth.models import User

class Poem(m.Model):
    author = m.ForeignKey(User)
    title = m.CharField(max_length=80)
    date = m.DateField()
    content = m.TextField()
