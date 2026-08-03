from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# ==========================
# HARFLAR
# ==========================
class Letter(models.Model):
    char = models.CharField(max_length=5, verbose_name="Harf", help_text="Masalan: A, B, D...")
    name = models.CharField(max_length=100, verbose_name="Harf nomi", help_text="Masalan: A harfi")
    image = models.ImageField(upload_to='letters/images/', verbose_name="Harf rasmi", blank=True, null=True)
    audio = models.FileField(upload_to='letters/audios/', verbose_name="Harf talaffuzi (ovoz)", blank=True, null=True, help_text="MP3, WAV")
    
    example_word = models.CharField(max_length=100, verbose_name="Misoldagi so'z", help_text="Masalan: Olma", blank=True)
    example_image = models.ImageField(upload_to='letters/examples/', verbose_name="Misol rasmi", blank=True, null=True)
    example_audio = models.FileField(upload_to='letters/examples/audio/', verbose_name="Misol so'z ovozi", blank=True, null=True)
    
    description = models.TextField(verbose_name="Qisqacha tavsif", blank=True, help_text="Bolalar uchun harf haqida")
    
    color = models.CharField(max_length=20, default="#FF6B6B", verbose_name="Fon rangi (HEX)", help_text="Masalan: #FF6B6B")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Harf"
        verbose_name_plural = "Harflar"
        ordering = ['order', 'char']

    def __str__(self):
        return f"{self.char} - {self.name}"

# ==========================
# RAQAMLAR
# ==========================
class Number(models.Model):
    value = models.PositiveIntegerField(verbose_name="Raqam qiymati", unique=True, help_text="Masalan: 1, 2, 3...")
    word = models.CharField(max_length=100, verbose_name="So'z bilan", help_text="Masalan: bir, ikki")
    
    image = models.ImageField(upload_to='numbers/images/', verbose_name="Raqam rasmi", blank=True, null=True)
    audio = models.FileField(upload_to='numbers/audios/', verbose_name="Raqam talaffuzi", blank=True, null=True)
    
    count_image = models.ImageField(upload_to='numbers/count/', verbose_name="Miqdor rasmi (masalan 3 ta olma)", blank=True, null=True)
    description = models.TextField(verbose_name="Tavsif", blank=True)
    
    color = models.CharField(max_length=20, default="#4ECDC4", verbose_name="Fon rangi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Raqam"
        verbose_name_plural = "Raqamlar"
        ordering = ['order', 'value']

    def __str__(self):
        return f"{self.value} - {self.word}"

# ==========================
# HAYVONLAR
# ==========================
class AnimalCategory(models.Model):
    CATEGORY_CHOICES = [
        ('uy', 'Uy hayvonlari'),
        ('yovvoyi', 'Yovvoyi hayvonlar'),
        ('qushlar', 'Qushlar'),
        ('suv', 'Suv hayvonlari'),
        ('hasharot', 'Hasharotlar'),
    ]
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", blank=True)
    type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='uy', verbose_name="Turi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='animals/categories/', verbose_name="Kategoriya rasmi", blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, verbose_name="Emoji/Icon", help_text="Masalan: 🐶, 🦁")
    color = models.CharField(max_length=20, default="#FFE66D", verbose_name="Fon rangi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Hayvon kategoriyasi"
        verbose_name_plural = "Hayvon kategoriyalari"
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Animal(models.Model):
    category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE, related_name='animals', verbose_name="Kategoriya")
    name = models.CharField(max_length=100, verbose_name="Hayvon nomi", help_text="Masalan: Mushuk")
    name_en = models.CharField(max_length=100, blank=True, verbose_name="Inglizcha nomi", help_text="Masalan: Cat")
    
    image = models.ImageField(upload_to='animals/images/', verbose_name="Hayvon rasmi")
    audio_sound = models.FileField(upload_to='animals/sounds/', verbose_name="Hayvon ovozi (miyov, vov...) ", blank=True, null=True)
    audio_name = models.FileField(upload_to='animals/names/', verbose_name="Nom talaffuzi ovozi", blank=True, null=True)
    
    description = models.TextField(verbose_name="Hayvon haqida (bolalar uchun)", blank=True)
    where_lives = models.CharField(max_length=200, blank=True, verbose_name="Qayerda yashaydi?")
    what_eats = models.CharField(max_length=200, blank=True, verbose_name="Nima yeydi?")
    interesting_fact = models.TextField(blank=True, verbose_name="Qiziqarli fakt")
    
    color = models.CharField(max_length=20, default="#FF9F1C", verbose_name="Fon rangi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Hayvon"
        verbose_name_plural = "Hayvonlar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

# ==========================
# RANGLAR
# ==========================
class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name="Rang nomi", help_text="Masalan: Qizil")
    name_en = models.CharField(max_length=50, blank=True, verbose_name="Inglizcha nomi")
    hex_code = models.CharField(max_length=20, default="#FF0000", verbose_name="HEX kodi", help_text="#FF0000")
    image = models.ImageField(upload_to='colors/', verbose_name="Rang rasmi (obyekt)", blank=True, null=True)
    audio = models.FileField(upload_to='colors/audios/', verbose_name="Rang talaffuzi", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"
        ordering = ['order']

    def __str__(self):
        return self.name

# ==========================
# SO'ZLASHUV / NUTQ RIVOJLANTIRISH
# ==========================
class ConversationTopic(models.Model):
    title = models.CharField(max_length=150, verbose_name="Mavzu nomi", help_text="Masalan: Salomlashish")
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Mavzu tavsifi")
    image = models.ImageField(upload_to='conversation/topics/', verbose_name="Mavzu rasmi", blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icon/Emoji", help_text="Masalan: 👋")
    color = models.CharField(max_length=20, default="#A8E6CF", verbose_name="Fon rangi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "So'zlashuv mavzusi"
        verbose_name_plural = "So'zlashuv mavzulari"
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Phrase(models.Model):
    DIFFICULTY_CHOICES = [
        ('oson', 'Oson'),
        ('orta', "O'rtacha"),
        ('qiyin', 'Qiyin'),
    ]
    topic = models.ForeignKey(ConversationTopic, on_delete=models.CASCADE, related_name='phrases', verbose_name="Mavzu")
    text = models.CharField(max_length=300, verbose_name="Ibora / So'z", help_text="Masalan: Salom, qanday ahvoldasan?")
    translation = models.CharField(max_length=300, blank=True, verbose_name="Tarjimasi / Izohi", help_text="Bolalar uchun tushuntirish")
    
    image = models.ImageField(upload_to='conversation/phrases/', verbose_name="Rasm", blank=True, null=True)
    audio = models.FileField(upload_to='conversation/audios/', verbose_name="Ovozli talaffuz", blank=True, null=True)
    
    example = models.TextField(blank=True, verbose_name="Misol gap")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='oson', verbose_name="Qiyinlik darajasi")
    
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "So'zlashuv iborasi"
        verbose_name_plural = "So'zlashuv iboralari"
        ordering = ['order']

    def __str__(self):
        return self.text

# ==========================
# O'YINLAR / TOPSHIRIQLAR (Nutqni rivojlantirish)
# ==========================
class Exercise(models.Model):
    TYPE_CHOICES = [
        ('match', 'Moslashtirish (rasm-soz)'),
        ('listen', 'Eshit va top'),
        ('speak', 'Qaytarib ayt'),
        ('puzzle', 'Jumboq'),
    ]
    title = models.CharField(max_length=150, verbose_name="Mashq nomi")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='listen', verbose_name="Mashq turi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='exercises/', blank=True, null=True, verbose_name="Rasm")
    audio = models.FileField(upload_to='exercises/audios/', blank=True, null=True, verbose_name="Ovoz")
    related_letter = models.ForeignKey(Letter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Bog'liq harf")
    related_number = models.ForeignKey(Number, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Bog'liq raqam")
    related_animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Bog'liq hayvon")
    
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mashq / O'yin"
        verbose_name_plural = "Mashqlar / O'yinlar"
        ordering = ['order']

    def __str__(self):
        return self.title
