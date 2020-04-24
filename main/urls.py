from django.urls import path
from .views import Home, Dashboard, DataUpload, DataDelete, Download, Share, OffShare

urlpatterns = [
    path('', Home, name='home'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dataUpload/', DataUpload, name='dataUpload'),
    path('dataDelete/<str:path>', DataDelete, name='dataDelete'),
    path('download/<int:id>/', Download, name='download'),
    path('share/<int:id>/', Share, name='share'),
    path('offshare/<int:id>/', OffShare, name='offshare'),
]