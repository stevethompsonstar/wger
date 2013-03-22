from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from wger.nutrition.views import ingredient
from wger.nutrition.views import plan
from wger.nutrition.views import meal
from wger.nutrition.views import meal_item
from wger.nutrition.views import unit
from wger.nutrition.views import unit_ingredient

urlpatterns = patterns('wger.nutrition.views',
    url(r'^overview/$', 'plan.overview'),

    # Plans
    url(r'^add/$', 'plan.add'),
    url(r'^(?P<id>\d+)/view/$', 'plan.view'),
    url(r'^(?P<pk>\d+)/copy/$',
        'plan.copy',
        name='nutrition-copy'),
    url(r'^(?P<pk>\d+)/delete/$',
        login_required(plan.PlanDeleteView.as_view()),
        name='nutrition-delete'),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(plan.PlanEditView.as_view()),
        name='nutrition-edit'),
    url(r'^(?P<id>\d+)/pdf/$', 'plan.export_pdf'),

    # Meals
    url(r'^(?P<plan_pk>\d+)/meal/add/$',
        login_required(meal.MealCreateView.as_view()),
        name='meal-add'),
    url(r'^meal/(?P<pk>\d+)/edit/$',
        login_required(meal.MealEditView.as_view()),
        name='meal-edit'),
    url(r'^meal/(?P<id>\d+)/delete/$', 'meal.delete_meal'),

    # Meal items
    url(r'^meal/(?P<meal_id>\d+)/item/add/$',
        login_required(meal_item.MealItemCreateView.as_view()),
        name='mealitem-add'),
    url(r'^meal/item/(?P<pk>\d+)/edit/$',
        login_required(meal_item.MealItemEditView.as_view()),
        name='mealitem-edit'),
    url(r'^meal/item/(?P<item_id>\d+)/delete/$', 'meal_item.delete_meal_item'),

    # Ingredients
    url(r'^ingredient/(?P<pk>\d+)/delete/$',
        permission_required('exercises.change_exercise')(ingredient.IngredientDeleteView.as_view()),
        name='ingredient-delete'),
    url(r'^ingredient/(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(ingredient.IngredientEditView.as_view()),
        name='ingredient-edit'),
    url(r'^ingredient/add/$',
        permission_required('exercises.change_exercise')(ingredient.IngredientCreateView.as_view()),
        name='ingredient-add'),
    url(r'^ingredient/overview/$', 'ingredient.overview'),
    url(r'^ingredient/(?P<id>\d+)/view/$', 'ingredient.view'),
    url(r'^ingredient/(?P<id>\d+)/view/(?P<slug>[-\w]+)/$', 'ingredient.view'),
    url(r'^ingredient/search/$',
        'ingredient.search',
        name='ingredient-search'),
    url(r'^ingredient/(?P<pk>\d+)/get-units$',
        'ingredient.ajax_get_ingredient_units',
        name='ingredient-get-units'),
    url(r'^ingredient/(?P<pk>\d+)/get-nutritional-values$',
        'ingredient.ajax_get_ingredient_values',
        name='ingredient-get-values'),

    # Ingredient units
    url(r'^ingredient/unit/list/$',
        permission_required('exercises.change_exercise')(unit.WeightUnitListView.as_view()),
        name='weight-unit-list'),
    url(r'^ingredient/unit/add/$',
        permission_required('exercises.change_exercise')(unit.WeightUnitCreateView.as_view()),
        name='weight-unit-add'),
    url(r'^ingredient/unit/(?P<pk>\d+)/delete/$',
        permission_required('exercises.change_exercise')(unit.WeightUnitDeleteView.as_view()),
        name='weight-unit-delete'),
    url(r'^ingredient/unit/(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(unit.WeightUnitUpdateView.as_view()),
        name='weight-unit-edit'),
        

    # Ingredient to weight units cross table
    url(r'^ingredient/unit-to-ingredient/add/(?P<ingredient_pk>\d+)/$',
        permission_required('exercises.change_exercise')(unit_ingredient.WeightUnitIngredientCreateView.as_view()),
        name='weight-unit-ingredient-add'),
    url(r'^ingredient/unit-to-ingredient/(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(unit_ingredient.WeightUnitIngredientUpdateView.as_view()),
        name='weight-unit-ingredient-edit'),
    url(r'^ingredient/unit-to-ingredient/(?P<pk>\d+)/delete/$',
        permission_required('exercises.change_exercise')(unit_ingredient.WeightUnitIngredientDeleteView.as_view()),
        name='weight-unit-ingredient-delete'),
)
