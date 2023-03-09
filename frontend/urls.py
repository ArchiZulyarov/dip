from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('food/', views.index),
                  path('food/api/card/', views.card),
                  path('food/api/ingredientList/', views.ingredientList),
                  path('api/getdish/', views.getdish) ,
                  path('api/getIngredents/', views.getIngredients), 
                  path('api/getCategories/', views.getCategories) 
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
