from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea, TextInput
from .models import Letter, Number, AnimalCategory, Animal, Color, ConversationTopic, Phrase, Exercise

# Umumiy yordamchi funksiyalar
def image_preview_tag(obj, field_name):
    """Rasm preview HTML"""
    file = getattr(obj, field_name, None)
    if file:
        try:
            return format_html('<img src="{}" style="width:100px; height:100px; object-fit:cover; border-radius:12px; border:2px solid #eee;" /><br><small>{}</small>', file.url, file.name.split('/')[-1])
        except:
            return "Rasm yoʻq"
    return format_html('<div style="width:100px; height:60px; background:#f5f5f5; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#999; font-size:12px;">Rasm yoʻq<br>Yuklang</div>')

def audio_player_tag(obj, field_name):
    """Audio player HTML"""
    file = getattr(obj, field_name, None)
    if file:
        try:
            return format_html(
                '<audio controls style="width:250px;"><source src="{}" type="audio/mpeg">Brauzeringiz audio qo\'llamaydi</audio><br><small style="color:#666;">{}</small><br>'
                '<a href="{}" target="_blank" style="font-size:11px; background:#2D3436; color:white; padding:2px 8px; border-radius:10px; text-decoration:none;">📥 Yuklab olish</a>',
                file.url, file.name.split('/')[-1], file.url
            )
        except:
            return "Ovoz yoʻq"
    return format_html('<div style="padding:10px; background:#fff3cd; border-radius:8px; font-size:12px; color:#856404;">🔇 Ovoz yo\'q - Fayl yuklang (MP3, WAV, M4A)</div>')

# ================= HARFLAR =================
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('char_badge', 'char', 'name', 'example_word', 'image_thumb', 'audio_icon', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('char', 'name', 'example_word')
    ordering = ('order',)
    list_per_page = 30
    save_on_top = True
    
    # Tahrirlash formasi
    readonly_fields = ('image_preview', 'audio_preview', 'example_image_preview', 'example_audio_preview')
    
    fieldsets = (
        ('📝 Asosiy ma\'lumot (Matnni tahrirlang)', {
            'fields': ('char', 'name', 'order', 'is_active', 'color', 'description'),
            'description': 'Bu yerda harf va tavsif matnini qo\'lda tahrirlay olasiz. Internet shart emas!'
        }),
        ('🖼️ Harf rasmi va ovozi (Mavjudini almashtirish yoki yangisini yuklash)', {
            'fields': ('image_preview', 'image', 'audio_preview', 'audio'),
            'description': 'Kompyuteringizdan fayl tanlang. Mavjud fayl avtomatik almashadi.'
        }),
        ('📚 Misol so\'z (Mavjudini tahrirlang)', {
            'fields': ('example_word', 'example_image_preview', 'example_image', 'example_audio_preview', 'example_audio'),
        }),
    )
    
    def char_badge(self, obj):
        return format_html('<div style="width:40px; height:40px; background:{}; color:white; border-radius:12px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:18px;">{}</div>', obj.color, obj.char)
    char_badge.short_description = "Harf"
    
    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:50px; height:50px; object-fit:cover; border-radius:8px;" />', obj.image.url)
        return format_html('<span style="color:#ccc;">-</span>')
    image_thumb.short_description = "Rasm"
    
    def audio_icon(self, obj):
        if obj.audio:
            return format_html('<span style="background:#D9F8F2; padding:4px 8px; border-radius:10px; font-size:11px;">🔊 Bor</span>')
        return format_html('<span style="background:#FFE5EC; padding:4px 8px; border-radius:10px; font-size:11px;">🔇 Yo\'q</span>')
    audio_icon.short_description = "Ovoz"
    
    def image_preview(self, obj):
        return image_preview_tag(obj, 'image')
    image_preview.short_description = "Hozirgi rasm (Ko'rish)"
    
    def audio_preview(self, obj):
        return audio_player_tag(obj, 'audio')
    audio_preview.short_description = "Hozirgi ovoz (Eshitish)"
    
    def example_image_preview(self, obj):
        return image_preview_tag(obj, 'example_image')
    example_image_preview.short_description = "Misol rasmi (Hozirgi)"
    
    def example_audio_preview(self, obj):
        return audio_player_tag(obj, 'example_audio')
    example_audio_preview.short_description = "Misol ovozi (Hozirgi)"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/letter/{}/change/" style="background:#FF6B6B; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px; font-weight:bold;">✏️ Tahrirlash</a>', obj.pk)
    edit_btn.short_description = "Amal"
    
    actions = ['make_active', 'make_inactive']
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} ta harf faollashtirildi")
    make_active.short_description = "✅ Tanlanganlarni faollashtirish"
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} ta harf nofaollashtirildi")
    make_inactive.short_description = "❌ Tanlanganlarni nofaollashtirish"

# ================= RAQAMLAR =================
@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('value_badge', 'value', 'word', 'image_thumb', 'audio_icon', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    search_fields = ('word', 'value')
    ordering = ('order',)
    save_on_top = True
    readonly_fields = ('image_preview', 'audio_preview', 'count_image_preview')
    
    fieldsets = (
        ('📝 Asosiy (Matnni tahrirlang)', {
            'fields': ('value', 'word', 'order', 'is_active', 'color', 'description')
        }),
        ('🖼️ Rasmlar va Ovoz (Almashtirish mumkin)', {
            'fields': ('image_preview', 'image', 'audio_preview', 'audio', 'count_image_preview', 'count_image'),
            'description': 'Kompyuterdan yangi fayl tanlasangiz, eskisi avtomatik o\'chadi va yangisi yuklanadi. Internet kerak emas!'
        }),
    )
    
    def value_badge(self, obj):
        return format_html('<div style="width:40px; height:40px; background:{}; color:white; border-radius:12px; display:flex; align-items:center; justify-content:center; font-weight:900;">{}</div>', obj.color, obj.value)
    value_badge.short_description = "Raqam"
    
    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:45px; height:45px; object-fit:cover; border-radius:8px;" />', obj.image.url)
        return "-"
    image_thumb.short_description = "Rasm"
    
    def audio_icon(self, obj):
        return format_html('🔊' if obj.audio else '🔇')
    audio_icon.short_description = "Ovoz"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    def audio_preview(self, obj): return audio_player_tag(obj, 'audio')
    def count_image_preview(self, obj): return image_preview_tag(obj, 'count_image')
    image_preview.short_description = "Hozirgi rasm"
    audio_preview.short_description = "Hozirgi ovoz"
    count_image_preview.short_description = "Miqdor rasmi"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/number/{}/change/" style="background:#1ABC9C; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px;">✏️ Tahrirlash</a>', obj.pk)
    edit_btn.short_description = ""

# ================= HAYVON KATEGORIYA =================
class AnimalInline(admin.TabularInline):
    model = Animal
    extra = 0
    fields = ('name', 'image_thumb_inline', 'is_active', 'order')
    readonly_fields = ('image_thumb_inline',)
    show_change_link = True
    
    def image_thumb_inline(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:40px; height:40px; border-radius:8px; object-fit:cover;" />', obj.image.url)
        return "-"

@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'type', 'animal_count', 'order', 'color_preview', 'edit_btn')
    list_editable = ('order',)
    list_filter = ('type',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    inlines = [AnimalInline]
    readonly_fields = ('image_preview',)
    
    fieldsets = (
        ('📝 Kategoriya ma\'lumoti (Tahrirlash)', {
            'fields': ('name', 'slug', 'type', 'description', 'icon', 'color', 'order', 'image_preview', 'image')
        }),
    )
    
    def animal_count(self, obj):
        return format_html('<span style="background:#FFE66D; padding:4px 10px; border-radius:12px; font-weight:bold;">{} ta</span>', obj.animals.count())
    animal_count.short_description = "Hayvonlar"
    
    def color_preview(self, obj):
        return format_html('<div style="width:30px; height:30px; background:{}; border-radius:8px; border:2px solid #eee;"></div>', obj.color)
    color_preview.short_description = "Rang"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    image_preview.short_description = "Kategoriya rasmi"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/animalcategory/{}/change/" style="background:#F39C12; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px;">✏️ Tahrirlash</a>', obj.pk)
    edit_btn.short_description = ""

# ================= HAYVONLAR =================
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'name', 'category', 'audio_status', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active', 'category__type')
    search_fields = ('name', 'name_en', 'description')
    ordering = ('order',)
    list_per_page = 20
    save_on_top = True
    readonly_fields = ('image_preview', 'audio_sound_preview', 'audio_name_preview')
    
    fieldsets = (
        ('📝 Asosiy matnlar (Qo\'lda tahrirlash - Internet shart emas)', {
            'fields': ('category', 'name', 'name_en', 'order', 'is_active', 'color', 'description', 'where_lives', 'what_eats', 'interesting_fact'),
            'description': 'Barcha matn maydonlarini shu yerdan bevosita yozib, o\'zgartirishingiz mumkin.'
        }),
        ('🖼️ Rasm (Mavjudini bosib ko\'ring, yangisini yuklang)', {
            'fields': ('image_preview', 'image'),
        }),
        ('🔊 Ovozlar (Mavjudini eshitib, yangisini yuklash)', {
            'fields': ('audio_sound_preview', 'audio_sound', 'audio_name_preview', 'audio_name'),
            'description': 'Kompyuteringizdan MP3/WAV fayl tanlang. Eski fayl avtomatik almashadi. Masalan: mushuk ovozi - miyov.mp3'
        }),
    )
    
    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:60px; height:60px; object-fit:cover; border-radius:12px;" />', obj.image.url)
        return format_html('<div style="width:60px; height:60px; background:#eee; border-radius:12px; display:flex; align-items:center; justify-content:center;">🐾</div>')
    image_thumb.short_description = "Rasm"
    
    def audio_status(self, obj):
        has_sound = "✅" if obj.audio_sound else "❌"
        has_name = "✅" if obj.audio_name else "❌"
        return format_html('<span title="Hayvon ovozi">{} Ovoz</span><br><span title="Nom talaffuzi">{} Nom</span>', has_sound, has_name)
    audio_status.short_description = "Ovozlar"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    def audio_sound_preview(self, obj): return audio_player_tag(obj, 'audio_sound')
    def audio_name_preview(self, obj): return audio_player_tag(obj, 'audio_name')
    image_preview.short_description = "Hozirgi rasm - Ko'rish"
    audio_sound_preview.short_description = "Hozirgi hayvon ovozi - Eshitish"
    audio_name_preview.short_description = "Hozirgi nom talaffuzi - Eshitish"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/animal/{}/change/" style="background:#E67E22; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px; font-weight:bold;">✏️ Tahrirlash</a>', obj.pk)
    edit_btn.short_description = "Tahrirlash"

# ================= RANGLAR =================
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_badge', 'name', 'name_en', 'hex_code', 'image_thumb', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'name_en')
    save_on_top = True
    readonly_fields = ('image_preview', 'audio_preview', 'color_big_preview')
    
    fieldsets = (
        ('🎨 Rang ma\'lumoti', {
            'fields': ('name', 'name_en', 'hex_code', 'color_big_preview', 'order', 'is_active')
        }),
        ('🖼️ Rasm va Ovoz (Tahrirlash)', {
            'fields': ('image_preview', 'image', 'audio_preview', 'audio')
        }),
    )
    
    def color_badge(self, obj):
        return format_html('<div style="width:35px; height:35px; background:{}; border-radius:10px; border:2px solid #eee;"></div>', obj.hex_code)
    color_badge.short_description = "Rang"
    
    def color_big_preview(self, obj):
        return format_html('<div style="width:100%; height:60px; background:{}; border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; text-shadow:1px 1px 2px black;">{} - {}</div>', obj.hex_code, obj.name, obj.hex_code)
    color_big_preview.short_description = "Rang ko'rinishi"
    
    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:40px; height:40px; border-radius:8px; object-fit:cover;" />', obj.image.url)
        return "-"
    image_thumb.short_description = "Rasm"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    def audio_preview(self, obj): return audio_player_tag(obj, 'audio')
    image_preview.short_description = "Rasm"
    audio_preview.short_description = "Ovoz"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/color/{}/change/" style="background:#3498DB; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px;">✏️</a>', obj.pk)
    edit_btn.short_description = ""

# ================= SO'ZLASHUV =================
class PhraseInline(admin.TabularInline):
    model = Phrase
    extra = 1
    fields = ('text', 'translation', 'difficulty', 'order', 'is_active', 'audio', 'image')
    show_change_link = True
    ordering = ('order',)

@admin.register(ConversationTopic)
class ConversationTopicAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'phrase_count', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    inlines = [PhraseInline]
    readonly_fields = ('image_preview',)
    
    fieldsets = (
        ('💬 Mavzu (Matnni tahrirlang)', {
            'fields': ('title', 'slug', 'description', 'icon', 'color', 'order', 'is_active', 'image_preview', 'image'),
        }),
    )
    
    def phrase_count(self, obj):
        return format_html('<span style="background:#E5D9FF; padding:4px 10px; border-radius:12px;">{} ibora</span>', obj.phrases.count())
    phrase_count.short_description = "Iboralar"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    image_preview.short_description = "Mavzu rasmi"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/conversationtopic/{}/change/" style="background:#8E44AD; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px;">✏️ Tahrirlash + Iboralar</a>', obj.pk)
    edit_btn.short_description = ""

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'difficulty_badge', 'image_thumb', 'audio_icon', 'order', 'is_active', 'edit_btn')
    list_editable = ('order', 'is_active')
    list_filter = ('topic', 'difficulty', 'is_active')
    search_fields = ('text', 'translation', 'example')
    save_on_top = True
    readonly_fields = ('image_preview', 'audio_preview')
    
    fieldsets = (
        ('📝 Ibora matni (Tahrirlash - qo\'lda yozing)', {
            'fields': ('topic', 'text', 'translation', 'example', 'difficulty', 'order', 'is_active'),
            'description': 'Matnni bevosita shu yerdan yozib tahrirlang. Internet kerak emas!'
        }),
        ('🖼️ Rasm va Ovoz (Faylni almashtirish)', {
            'fields': ('image_preview', 'image', 'audio_preview', 'audio'),
        }),
    )
    
    def difficulty_badge(self, obj):
        colors = {'oson': '#2ECC71', 'orta': '#F39C12', 'qiyin': '#E74C3C'}
        return format_html('<span style="background:{}; color:white; padding:4px 10px; border-radius:12px; font-size:11px; font-weight:bold;">{}</span>', colors.get(obj.difficulty, '#999'), obj.get_difficulty_display())
    difficulty_badge.short_description = "Daraja"
    
    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:40px; height:40px; object-fit:cover; border-radius:8px;" />', obj.image.url)
        return "-"
    image_thumb.short_description = "Rasm"
    
    def audio_icon(self, obj):
        return format_html('🔊' if obj.audio else '🔇')
    audio_icon.short_description = "Ovoz"
    
    def image_preview(self, obj): return image_preview_tag(obj, 'image')
    def audio_preview(self, obj): return audio_player_tag(obj, 'audio')
    image_preview.short_description = "Hozirgi rasm"
    audio_preview.short_description = "Hozirgi ovoz - Eshitish"
    
    def edit_btn(self, obj):
        return format_html('<a href="/admin/core/phrase/{}/change/" style="background:#8E44AD; color:white; padding:5px 12px; border-radius:15px; text-decoration:none; font-size:11px;">✏️</a>', obj.pk)
    edit_btn.short_description = ""

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('type', 'is_active')
