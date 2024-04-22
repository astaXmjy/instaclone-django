from django.urls import path
from  directs import views
urlpatterns = [
    path('inbox/',views.inbox,name='message'),
    path('directs/<username>/',views.Directs,name='directs'),
    path('send/',views.SendMessage,name="send-message"),
]
