from django.contrib import admin
from .models import UploadDataset

admin.site.site_header = "mDrive Admin Panel"

admin.site.register(UploadDataset)
