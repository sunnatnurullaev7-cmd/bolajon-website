# 🛠️ ADMIN QO'LLANMA - Barcha ma'lumotlarni tahrirlash

Sizning talabingiz bo'yicha tizimda mavjud bo'lgan barcha ma'lumotlarni admin dan **qo'lda, internetisiz** tahrirlash mumkin! Rasm, ovoz, matn - hammasi!

## 1. Admin ga kirish

```
Login: admin
Parol: admin123
URL: http://127.0.0.1:8000/admin/
```

Saytning o'zida ham agar admin bo'lib kirgan bo'lsangiz, har bir sahifa tepasida sariq **ADMIN MODE** banner chiqadi va har bir karta yonida **⚙️ Tahrirlash** tugmasi bor.

## 2. Mavjudini tahrirlash - QADAM-BA-QADAM

### Misol: A harfini tahrirlash

1. `/admin/` ga kiring → **Harflar** → ro'yxatda A harfini toping
2. Yoki saytda: **Harflar** → **A harfi** ni oching → **✏️ Admin da tahrirlash** tugmasini bosing

**Admin tahrirlash sahifasida siz ko'rasiz:**

#### A) Matnlarni tahrirlash (Internet shart emas!)
- **Harf**: A (o'zgartiring)
- **Harf nomi**: A harfi (yozing)
- **Misol so'z**: Olma (yangi matn yozing)
- **Tavsif**: Bolalar uchun tavsif
- **Rang**: #FF6B6B (rang kodi)
- **Tartib**: 1,2,3...

#### B) Rasmni ko'rish va almashtirish
Sahifada 2 qism bor:
- **Hozirgi rasm (Ko'rish)** - mavjud rasmni ko'rasiz (100x100 preview)
- **Rasm** maydoni - `Choose File` tugmasi

**Qanday almashtiriladi?**
1. Hozirgi rasmni ko'ring
2. `Choose File` ni bosing → Kompyuteringizdan yangi rasm tanlang (JPG, PNG)
3. Pastga tushib **SAQLASH** tugmasini bosing
4. ✅ Eski rasm o'chadi, yangisi yuklanadi! Internet kerak emas - fayl kompyuteringizdan!

#### C) Ovozni eshitish va almashtirish
- **Hozirgi ovoz (Eshitish)** - 🎧 audio player bor, bosib eshiting!
- `Yuklab olish` linki - mavjud ovozni yuklab olishingiz mumkin
- Yangi ovoz yuklash: `Choose File` → MP3/WAV/M4A tanlang → **SAQLASH**

Xuddi shu tartib **Misol rasmi** va **Misol ovozi** uchun ham!

### 3. Barcha bo'limlar uchun bir xil

#### 🔢 Raqamlar
- `Raqamlar` → Tahrirlash → 3 ta fayl: `Asosiy rasm`, `Ovoz`, `Miqdor rasmi` (3 ta olma rasmi)
- Matn: `bir, ikki` ni o'zgartiring

#### 🐾 Hayvon kategoriyalari
- `Hayvon kategoriyalari` → Tahrirlash
- Ichida **Hayvonlar** jadvali bor - o'sha kategoriyadagi hayvonlarni to'g'ridan-to'g'ri ko'rib tahrirlay olasiz
- Inline jadvalda rasm thumbnail ko'rinadi

#### 🦁 Hayvonlar (Eng muhim - 2 ta ovoz!)
- `Hayvonlar` → Tahrirlash sahifasida:
  - **Rasm (Hozirgi)** - hayvon rasmini ko'rasiz
  - **Hayvon ovozi** - miyov, vov... ovozni player da eshitasiz
  - **Nom talaffuzi** - mushuk so'zini eshitasiz
- Har birini alohida almashtirish mumkin!

**Hayvon matnlarini tahrirlash:**
- Qayerda yashaydi? → `O'rmonda` ni o'zgartiring
- Nima yeydi? → `Go'sht` ni yozing
- Qiziqarli fakt → matnni yozing

#### 🎨 Ranglar
- Rang nomi, HEX kodi `#FF0000`
- Katta rang preview ko'rinadi
- Rasm: masalan qizil olma rasmi
- Ovoz: `Qizil` degan ovoz

#### 💬 So'zlashuv
- `So'zlashuv mavzulari` → Tahrirlash
- Ichida **Iboralar** inline jadvali - shu mavzudagi barcha iboralarni bir joyda tahrirlay olasiz!
- Yoki `So'zlashuv iboralari` → alohida har bir iborani tahrirlash

**Ibora tahrirlash:**
- `Salom!` matnini `Salom, do'stim!` ga o'zgartiring
- Tarjimasi, Misol, Qiyinlik darajasi (oson/o'rtacha/qiyin)
- Rasm va Ovoz - preview bilan

## 4. Yangisini qo'lda qo'shish

Har bir bo'limda **+ Qo'shish** tugmasi:

- `/admin/core/letter/add/` → Yangi harf
  - Harf, nomi, tartib, rang kiriting
  - Rasm va ovoz tanlang → SAQLASH

- `/admin/core/animal/add/` → Yangi hayvon
  - Avval kategoriya tanlang!
  - Rasm yuklash majburiy
  - 2 ta ovoz ixtiyoriy

- `/admin/core/phrase/add/` → Yangi ibora
  - Mavzu tanlang
  - Matn yozing
  - Rasm/ovoz yuklang

**Internet shart emas!** Barcha fayllar `media/` papkaga sizning kompyuteringizdan yuklanadi.

## 5. Saytning o'zidan tahrirlash (Tezkor)

Agar admin bo'lib kirgan bo'lsangiz (`admin / admin123`):

- Har bir Harf/Raqam/Hayvon/Rang/Ibora kartochkasida **✏️ Tahrirlash** tugmasi chiqadi
- Uni bossangiz to'g'ridan-to'g'ri admin tahrirlash sahifasiga o'tasiz
- Tezda o'zgartirib SAQLASH ni bosasiz - saytda darhol yangilanadi!

## 6. O'chirish

Admin ro'yxatda checkbox bilan belgilab → Pastdagi **Action** menyudan:
- `Tanlanganlarni o'chirish`
- Yoki ichiga kirib pastdagi **O'chirish** qizil tugma

## 7. Faol / Nofaol qilish

Agar vaqtincha ko'rsatmaslik kerak bo'lsa:
- Tahrirlash ichida `Faolmi?` checkbox ini olib tashlang → SAQLASH
- Yoki ro'yxatda `Faol` ustunida to'g'ridan-to'g'ri on/off qilishingiz mumkin

Ro'yxatda **Action**:
- `Tanlanganlarni faollashtirish`
- `Tanlanganlarni nofaollashtirish`

## 8. Maslahatlar

- **Rasm o'lchami**: 500KB - 2MB optimal. Juda katta yuklamang.
- **Ovoz**: MP3 tavsiya etiladi, 100KB - 1MB.
- **Nomlash**: Fayl nomini tushunarli qiling: `a-harfi.mp3`, `mushuk.jpg`
- **Backup**: `media/` papkani va `db.sqlite3` ni vaqti-vaqti bilan nusxalab oling.

## 9. Tez-tez so'raladigan savollar

**Q: Rasmni almashtirsam eskisi o'chadimi?**
A: Ha, avtomatik! Yangi fayl yuklaganda eski fayl o'rnini bosadi.

**Q: Internet kerakmi?**
A: Yo'q! Barcha fayllar kompyuteringizdan yuklanadi. Faqat Django server ishlashi kerak.

**Q: Matnni qanday tahrirlayman?**
A: Admin da istalgan text maydoniga yangi matn yozib SAQLASH ni bosing.

**Q: Ovozni eshitish mumkinmi admin da?**
A: Ha! Yangi admin da har bir ovoz uchun audio player bor - bosib eshitasiz!

**Q: Bir vaqtning o'zida ko'p rasm yuklasa bo'ladimi?**
A: Hozircha har bir maydon alohida. Har bir harf/hayvon uchun alohida kirib yuklaysiz. Bu xavfsizlik uchun.

---

**Xullas:** Admin panel to'liq sizning qo'lingizda! Rasm, ovoz, matn - barchasini ko'rib, eshitib, qo'lda tahrirlay olasiz. Internet shart emas!

Yordam kerak bo'lsa: `/admin/` dagi har bir bo'limda tavsif yozilgan.
