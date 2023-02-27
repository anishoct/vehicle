from django.conf.urls.static import static
from django.urls import path, include

from vehicles import settings
from .import views
from .views import add_car

app_name='tatacars'
urlpatterns = [

    path('',views.car,name='car'),
    path('car/<int:car_id>/',views.detail,name='detail'),
    path('add_car',views.add_car,name='add_car'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete<int:id>/hel',views.delete,name='delete')
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
