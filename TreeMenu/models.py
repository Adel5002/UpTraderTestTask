from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItemChild(models.Model):
    text = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, db_index=True)
    item_child = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
