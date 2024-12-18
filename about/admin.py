from django.contrib import admin
from .models import AboutModel, DocumentModel, GalleryModel, ContactModel,TeachersModal, NewsModel
 


admin.site.register(AboutModel)
admin.site.register(DocumentModel)
admin.site.register(GalleryModel)
admin.site.register(TeachersModal)
admin.site.register(ContactModel)
admin.site.register(NewsModel)

