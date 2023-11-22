from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from menu.models import Menu


# Create your views here.


class MenuDetailView(DetailView):
    model = Menu

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return get_object_or_404(Menu, name=name)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        current_menu = context['object']

        ancestors = self.get_ancestors(current_menu)
        context['ancestors'] = ancestors

        descendants = self.get_descendants(current_menu)
        context['descendants'] = descendants

        return context

    @staticmethod
    def get_ancestors(menu):
        ancestors = []

        while menu.previous_tab:
            ancestors.insert(0, menu.previous_tab)
            menu = menu.previous_tab

        return ancestors

    @staticmethod
    def get_descendants(menu):
        return list(Menu.objects.filter(previous_tab=menu))
