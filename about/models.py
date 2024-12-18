from django.db import models
from django.forms import ValidationError


class NewsModel(models.Model):
    title = models.CharField(max_length=100, help_text='Yangilik mavzusini kiriting')
    news = models.TextField(max_length=2000, help_text='Yangigilikni kiriting')
    news_img = models.ImageField(upload_to='news/')

    def __str__(self):
        return f"Yangiliklar: {self.title}"
    class Meta:
        db_table= "news"
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class AboutModel(models.Model):
    description = models.TextField( help_text="Maktab haqida malumot yozing.")

    def save(self, *args, **kwargs):
        if AboutModel.objects.exists() and not self.pk:
            raise ValidationError("Faqat bitta AboutModel yozuviga ruxsat beriladi.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description}" 
    class Meta:
        db_table= "description"
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"


class DocumentModel(models.Model):
    document = models.FileField(upload_to='documents/', null=True, blank=True, help_text="Faylni yuklang")
    document_img = models.ImageField(upload_to='document_img/', null=True, blank=True, help_text="Dokument uchun rasm yuklang")
    def __str__(self):
        return f"{self.document}" 
    class Meta:
        db_table= "document"
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumentlar"


class GalleryModel(models.Model):
    gallery = models.ImageField(upload_to='school_img/', help_text="Maktab rasmini yuklang") 

    def __str__(self):
        return f"{self.gallery}" 
    class Meta:
        db_table= "galereya"
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"


class TeachersModal(models.Model):
    teacher_img = models.ImageField(upload_to="teacher_img/", help_text="O'qituvchining rasmini yuklang")
    first_name = models.CharField(max_length=100, help_text="O'qituvchinig ismini kiriting")
    last_name = models.CharField(max_length=100, help_text="O'qituvchinig familiyasini kiriting")
    bio = models.CharField(max_length=30, help_text="Qaysi fandan dars berishini kiriting")

    def __str__(self):
        return f" O'qituvchilar: {self.first_name} {self.last_name}"
    class Meta:
        db_table = "oqituvchilar"
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"



class ContactModel(models.Model):
    phone_number = models.CharField(max_length=100, help_text="Telefon raqamini kiriting.") 
    email = models.EmailField(help_text="Email manzilini kiriting.")
    address = models.TextField(max_length=100, help_text="Manzilni kiriting.")
    location = models.TextField(help_text="Manzilingizni xaritada ko'rsatish uchun joylashuvni kiriting.")
    instagram = models.URLField(null=True, blank=True, help_text="Instagram profilining URL manzilini kiriting.")
    telegram = models.URLField(null=True, blank=True, help_text="Telegram kanal yoki profil URL manzilini kiriting.")
    youtube = models.URLField(null=True, blank=True, help_text="YouTube kanalining URL manzilini kiriting.")

    def __str__(self):
        return f"Kontakt ma'lumotlari: {self.phone_number}, {self.email}"

    class Meta:
        db_table = 'kontakt'
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'
