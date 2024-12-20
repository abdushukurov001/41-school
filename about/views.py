from django.shortcuts import render
from .models import AboutModel, ContactModel, GalleryModel, TeachersModal, DocumentModel, NewsModel
from itertools import zip_longest

def home_view(request):
    about = AboutModel.objects.first()
    documents = DocumentModel.objects.all()[:3]
    gallery = GalleryModel.objects.all()
    contacts = ContactModel.objects.first()
    teachers = TeachersModal.objects.all()
    teachers_chunks = [list(chunk) for chunk in zip_longest(*[iter(teachers)]* 3, fillvalue=None)]
    gallery_chunks = [list(chunk) for chunk in zip_longest(*[iter(gallery)]* 4, fillvalue=None)]
    news = NewsModel.objects.all()
    reversed_gallery = gallery_chunks[::-1] 
    
    return render(request, 'home.html', context={
        'about' : about, 
        'documents' : documents,
        'reversed_gallery':reversed_gallery,
        'contact_info' :contacts,
        'teachers_chunks' : teachers_chunks,
        'news' : news
    })
