from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True, verbose_name='Текст поста')
    rate = models.IntegerField(default=0, verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    def __str__(self):
        return self.title

