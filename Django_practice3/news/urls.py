from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('made-by-class/', ClassBasedIndex.as_view(), name='home_class'),
    path('category/<int:category_id>', get_category, name='category'),
    path('redirect/', Redirect.as_view(), name='redirect'),
    path('form_example/', SimpleForm.as_view(), name='form_example')
]
