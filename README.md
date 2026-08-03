# 🌈 BOLAJON - Bolalar Nutqini Rivojlantirish Platformasi

**Zamonaviy, bolalarni qiziqtiruvchi Django web ilova**

Samarqandlik ota-onalar va bolajonlar uchun: harflar, raqamlar, uy va yovvoyi hayvonlar, ranglar, so'zlashuv va nutqni rivojlantirish bo'yicha to'liq platforma.

Barcha rasmlar, ovozlar, matnlar **faqat Admin panel orqali** kiritiladi!

---

## 🎯 Bo'limlar

### 1. 🔤 Harflar (Letter)
- A-Z harflar
- Har bir harf uchun: rasm, talaffuz ovozi (MP3/WAV)
- Misol so'z (Olma), misol rasmi va misol ovozi
- Rang, tartib raqami

### 2. 🔢 Raqamlar (Number)
- 1-... raqamlar
- So'z bilan (bir, ikki), rasm, ovoz
- Miqdor rasmi (masalan 3 ta olma rasmi)
- Vizual sanash nuqtalari

### 3. 🐾 Hayvonlar
**Kategoriyalar:** Uy hayvonlari, Yovvoyi hayvonlar, Qushlar, Suv hayvonlari, Hasharotlar

Har bir hayvon uchun:
- Rasm (majburiy)
- Ovozi: hayvon ovozi (miyov, vov) + nomi talaffuzi
- Qayerda yashaydi, nima yeydi, qiziqarli fakt
- Admin yuklaydi

### 4. 🎨 Ranglar (Color)
- Rang nomi (Qizil), inglizcha nomi, HEX kodi (#FF0000)
- Rangga oid rasm (qizil olma), talaffuz ovozi

### 5. 💬 So'zlashuv / Nutq (Conversation)
**Mavzular:** Salomlashish, Tanishish, Oila, O'yinchoqlar, Oziq-ovqat, Yordam so'rash va h.k.

Har bir ibora:
- Matn: "Salom, qanday ahvoldasan?"
- Tushuntirish: tarjimasi / izohi
- Rasm, ovozli talaffuz
- Misol gap, qiyinlik darajasi (oson/o'rtacha/qiyin)

### 6. 🎮 Mashqlar (Exercise)
- Moslashtirish (rasm-so'z), Eshit va top, Qaytarib ayt, Jumboq

---

## 💻 Texnologiya

- **Python Django 5.0**
- **SQLite** (dev), PostgreSQL ga oson o'tadi
- **Tailwind CSS CDN** - zamonaviy, bolalar uchun yorqin dizayn
- **Pillow** - rasm yuklash
- **Mobilga mos** (responsive), soft shadows, bubble dizayn, animatsiyalar

---

## 🚀 O'rnatish (Lokal)

```bash
# 1. Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 2. Kutubxonalar
pip install -r requirements.txt

# 3. Baza yaratish
python manage.py makemigrations
python manage.py migrate

# 4. Admin user
python manage.py createsuperuser
# username: admin, password: o'zingiz kiriting

# 5. Demo ma'lumot (ixtiyoriy)
python manage.py loaddata fixtures/demo.json
# yoki qo'lda admin orqali kiriting

# 6. Serverni ishga tushirish
python manage.py runserver

# Brauzerda:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/admin/
```

---

## 👨‍💼 Admin orqali qanday kiritiladi?

1. `/admin/` ga kiring
2. **Harflar** -> Add Letter
   - Harf: A, Nomi: A harfi, Rang: #FF6B6B
   - Rasm yuklang: A harfi rasmi
   - Ovoz yuklang: A talaffuzi mp3
   - Misol: Olma, rasm: olma, ovoz: olma.mp3

3. **AnimalCategory** -> avval kategoriya qo'shing
   - Nomi: Uy hayvonlari, Type: uy, Icon: 🐶, Rang: #FFE66D

4. **Hayvonlar** -> Add Animal
   - Kategoriya: Uy hayvonlari
   - Nomi: Mushuk, inglizcha: Cat
   - Rasm: mushuk.jpg
   - Hayvon ovozi: miyov.mp3
   - Nom talaffuzi: mushuk.mp3
   - Tavsif: Mushuklar yumshoq, yoqimtoy...

5. **Xuddi shu tartib** Raqamlar, Ranglar, So'zlashuv mavzulari va iboralar uchun.

> **Muhim:** Barcha media fayllar `media/` papkaga saqlanadi. `MEDIA_URL` va `MEDIA_ROOT` sozlangan.

---

## 🎨 Dizayn xususiyatlari

- **Baloo 2** + **Nunito** fontlari - bolalar uchun qiziqarli
- **Bubble** - yumaloq burchaklar (24px, 32px)
- **Pastel ranglar**: #FF6B6B, #4ECDC4, #FFE66D, #8E44AD
- **Wiggle va float animatsiyalar**
- **Audio tugmalar**: bosganda ovoz ijro etiladi
- **Ota-onalar uchun maslahatlar** har bir sahifada

---

## 📂 Loyiha tuzilmasi

```
bolajon/
├── bolajon/
│   ├── settings.py
│   ├── urls.py
├── core/
│   ├── models.py (Letter, Number, AnimalCategory, Animal, Color, ConversationTopic, Phrase, Exercise)
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
├── templates/
│   ├── base.html (asosiy shablon)
│   ├── home.html (bosh sahifa)
│   ├── core/
│   │   ├── letter_list.html
│   │   ├── letter_detail.html
│   │   ├── number_list.html
│   │   ├── number_detail.html
│   │   ├── animal_list.html
│   │   ├── animal_detail.html
│   │   ├── conversation_list.html
│   │   ├── conversation_detail.html
│   │   ├── color_list.html
├── static/css, js
├── media/ (admin yuklagan fayllar)
├── manage.py
└── requirements.txt
```

---

## 🔮 Kengaytirish g'oyalari

- [ ] Test / Quiz tizimi - ball yig'ish
- [ ] Foydalanuvchi profili - bolajon ismi, progress
- [ ] Ovoz yozish - bola qaytarib aytadi, yozib oladi
- [ ] Ertaklar bo'limi
- [ ] Ochki (gamification) tizimi
- [ ] Telegram bot integratsiyasi

---

## 📞 Muallif

Samarqand, UZ - 2026. Bolajonlar uchun ❤️ bilan yaratildi.

Savollar bo'lsa admin panel README ni o'qing yoki kodni ko'rib chiqing - barcha joyda Uzbek tilida commentlar yozilgan!

---

## 📸 Admin qanday ko'rinadi?

- Harflar: rasm + audio + misol
- Raqamlar: rasm + count image + audio
- Hayvonlar: 2 ta audio (ovozi + nomi), kategoriya, faktlar
- So'zlashuv: mavzu -> iboralar -> har bir ibora ovoz + rasm

Hammasi tayyor! Faqat `python manage.py runserver` qiling va `/admin/` da ma'lumot kiritishni boshlang!
