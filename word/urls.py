from django.urls import path,include
from .views import  HomePage,WordPage,AddWord,UpdateWord,DeleteWord,SignUp
urlpatterns = [
    path('',HomePage.as_view(),name='HOME'),
    path('word/<int:pk>/',WordPage.as_view(),name='Detail'),
    path('word/create',AddWord.as_view(),name='NEW'),
    path('word/update/<int:pk>',UpdateWord.as_view(),name='Update'),
    path('word/delete/<int:pk>',DeleteWord.as_view(),name='Delete'),
    path('signup',SignUp.as_view(),name='signup')
]
