from django.shortcuts import render
from .models import AboutModel, ContactModel, GalleryModel, TeachersModal, DocumentModel, NewsModel
from itertools import zip_longest

def home_view(request):
    about = AboutModel.objects.first()
    documents = DocumentModel.objects.all()[:3]
    reversed_gallery = GalleryModel.objects.all()
    contacts = ContactModel.objects.first()
    teachers = TeachersModal.objects.all()
    news = NewsModel.objects.all()

    
    return render(request, 'home.html', context={
        'about' : about, 
        'documents' : documents,
        'reversed_gallery':reversed_gallery,
        'contact_info' :contacts,
        'teachers' : teachers,
        'news' : news
    })
