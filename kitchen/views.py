from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType


def index(request):
    """View function for the home page of the site."""

    count_cooks = Cook.objects.count()
    count_dishes = Dish.objects.count()
    count_dichtipes = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "count_cooks": count_cooks,
        "count_dishes": count_dishes,
        "count_dichtipes": count_dichtipes,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)
