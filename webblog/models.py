from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about_me  = models.TextField(max_length= 200, null=True)
    author_image = models.ImageField(upload_to="author_image/", null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name']

class Blog(models.Model):
    blog_title = models.CharField(max_length = 200, help_text = "Enter a Blog Title")
    pub_date = models.DateField()
    blog_description = models.TextField(max_length = 1000, help_text="Enter blog description")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    blog_image = models.ImageField(upload_to='blog_image/', null=True)

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering = ['pub_date']

