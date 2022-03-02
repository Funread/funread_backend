from django.db import models

class WhatTheFuck(models.Model):
    name = models.CharField(max_length=20)