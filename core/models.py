from django.db import models


# About Me Model
class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return "About Me"


# Skills Model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill Name")
    description = models.TextField()
    image = models.ImageField(upload_to="skills")

    def __str__(self):
        return self.name


# Services Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service Name")
    description = models.TextField()
    image = models.ImageField(upload_to="service")

    def __str__(self):
        return self.name


# Projects Model
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project title")
    image = models.ImageField(upload_to="project")

    def __str__(self):
        return self.title
