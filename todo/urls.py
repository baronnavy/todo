from django.urls import path
from .views import TodoList, TodoList2, TodoDetail, TodoCreate, TodoDelete, TodoUpdate,Reservation,ResevationUpdate,ResevationCreate
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('list2/', TodoList2.as_view(), name='list2'),
    path('reservation/', Reservation.as_view(), name='reservation'),
    path('reservation_update/<int:pk>', ResevationUpdate.as_view(), name='reservation_update'),
    path('reservation_create/<int:year>', ResevationCreate.as_view(), name='reservation_create'),
    path('list/plot/', views.get_svg, name='plot'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    ]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
