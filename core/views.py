from django.shortcuts import render

from django.views.generic import TemplateView
from .models import About, Skill, Service, Project


class HomeTemplateView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["skills"] = Skill.objects.all()
        context["services"] = Service.objects.all()
        context["projects"] = Project.objects.all()
        return context

