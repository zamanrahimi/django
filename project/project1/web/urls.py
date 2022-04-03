from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# route section of CRUD, then go to the view 
urlpatterns = [
    path('list', views.index),
    path('insert', views.insert),
    path('delete_item/<int:myid>/', views.delete_item),
    path('update_item/<int:myid>/', views.update_item, name='update_item'),
    path('update_item1/<int:myid>/', views.update_item1, name='update_item1'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)