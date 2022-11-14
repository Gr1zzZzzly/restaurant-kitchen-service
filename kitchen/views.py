from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, SearchForm, CookForm, IngredientForm, CookUpdateExperienceForm
from kitchen.models import Cook, Dish, DishType, Ingredient


def index(request):
    """View function for the home page of the site."""

    count_cooks = Cook.objects.count()
    count_dishes = Dish.objects.count()
    count_dichtipes = DishType.objects.count()
    count_ingredients = Ingredient.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "count_cooks": count_cooks,
        "count_dishes": count_dishes,
        "count_dichtipes": count_dichtipes,
        "count_ingredients": count_ingredients,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5
    queryset = DishType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={
                "title": name,
            }
        )

        return context

    def get_queryset(self):

        form_ = SearchForm(self.request.GET)
        if form_.is_valid():
            return self.queryset.filter(
                name__icontains=form_.cleaned_data["title"]
            )

        return self.queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={
                "title": name,
            }
        )

        return context

    def get_queryset(self):
        form_ = SearchForm(self.request.GET)
        if form_.is_valid():
            return self.queryset.filter(
                name__icontains=form_.cleaned_data["title"]
            )

        return self.queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={
                "title": username,
            }
        )

        return context

    def get_queryset(self):
        form_ = SearchForm(self.request.GET)
        if form_.is_valid():
            return self.queryset.filter(
                username__icontains=form_.cleaned_data["title"]
            )

        return self.queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateExperienceForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5
    queryset = Ingredient.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={
                "title": name,
            }
        )

        return context

    def get_queryset(self):
        form_ = SearchForm(self.request.GET)
        if form_.is_valid():
            return self.queryset.filter(
                name__icontains=form_.cleaned_data["title"]
            )

        return self.queryset


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


