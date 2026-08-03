"""
Demo ma'lumotlar yaratish - media faylsiz, faqat matn va ranglar bilan
Admin keyin rasm va ovoz qo'shadi
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bolajon.settings')
django.setup()

from core.models import Letter, Number, AnimalCategory, Animal, Color, ConversationTopic, Phrase

print("🧹 Eski ma'lumotlarni tozalash...")
Letter.objects.all().delete()
Number.objects.all().delete()
Animal.objects.all().delete()
AnimalCategory.objects.all().delete()
Color.objects.all().delete()
ConversationTopic.objects.all().delete()
Phrase.objects.all().delete()

print("🔤 Harflar qo'shilmoqda...")
letters_data = [
    ("A", "A harfi", "Olma", "#FF6B6B"),
    ("B", "B harfi", "Baliq", "#4ECDC4"),
    ("D", "D harfi", "Daraxt", "#45B7D1"),
    ("E", "E harfi", "Eshik", "#96CEB4"),
    ("F", "F harfi", "Fil", "#FFEAA7"),
    ("G", "G harfi", "Gul", "#DDA0DD"),
    ("H", "H harfi", "Uy", "#98D8C8"),
    ("I", "I harfi", "Ish", "#F7DC6F"),
    ("J", "J harfi", "Jirafa", "#BB8FCE"),
    ("K", "K harfi", "Kitob", "#85C1E2"),
    ("L", "L harfi", "Lola", "#F8C471"),
    ("M", "M harfi", "Mushuk", "#82E0AA"),
    ("N", "N harfi", "Non", "#F1948A"),
    ("O", "O harfi", "Ona", "#FFB6C1"),
    ("P", "P harfi", "Piyola", "#AED6F1"),
    ("Q", "Q harfi", "Quyosh", "#FFD700"),
    ("R", "R harfi", "Rasm", "#FF7F50"),
    ("S", "S harfi", "Suv", "#87CEEB"),
    ("T", "T harfi", "Tovuq", "#D7BDE2"),
    ("U", "U harfi", "Uzum", "#A9DFBF"),
    ("V", "V harfi", "Vaza", "#F9E79F"),
    ("X", "X harfi", "Xat", "#A3E4D7"),
    ("Y", "Y harfi", "Yulduz", "#FADBD8"),
    ("Z", "Z harfi", "Zebra", "#D5DBDB"),
    ("O'", "O' harfi", "O'rdak", "#FF6B6B"),
    ("G'", "G' harfi", "G'ildirak", "#4ECDC4"),
    ("Sh", "Sh harfi", "Shar", "#45B7D1"),
    ("Ch", "Ch harfi", "Choy", "#96CEB4"),
    ("Ng", "Ng harfi", "Eng", "#FFEAA7"),
]

for i, (char, name, example, color) in enumerate(letters_data):
    Letter.objects.create(
        char=char,
        name=name,
        example_word=example,
        color=color,
        order=i,
        description=f"{char} harfi - {example} so'zi bilan o'rganamiz. Bolajon, {char} harfini qayta-qayta ayt!"
    )
print(f"✅ {Letter.objects.count()} ta harf qo'shildi")

print("🔢 Raqamlar qo'shilmoqda...")
numbers_data = [
    (0, "nol", "#FF6B6B"),
    (1, "bir", "#4ECDC4"),
    (2, "ikki", "#FFE66D"),
    (3, "uch", "#8E44AD"),
    (4, "to'rt", "#F39C12"),
    (5, "besh", "#3498DB"),
    (6, "olti", "#E74C3C"),
    (7, "yetti", "#1ABC9C"),
    (8, "sakkiz", "#9B59B6"),
    (9, "to'qqiz", "#E67E22"),
    (10, "o'n", "#2ECC71"),
]

for val, word, color in numbers_data:
    Number.objects.create(value=val, word=word, color=color, order=val, description=f"{val} raqami - {word}. Keling {val} ta narsani sanaymiz!")
print(f"✅ {Number.objects.count()} ta raqam qo'shildi")

print("🐾 Hayvon kategoriyalari...")
cats = [
    ("Uy hayvonlari", "uy-hayvonlari", "uy", "🐶", "#FFE66D", "Uyimizda yashaydigan do'stlarimiz"),
    ("Yovvoyi hayvonlar", "yovvoyi-hayvonlar", "yovvoyi", "🦁", "#FF6B6B", "O'rmonda, cho'lda yashaydigan hayvonlar"),
    ("Qushlar", "qushlar", "qushlar", "🦜", "#4ECDC4", "Osmonda uchadigan qushlar"),
    ("Suv hayvonlari", "suv-hayvonlari", "suv", "🐳", "#3498DB", "Dengiz va daryoda yashaydiganlar"),
]

cat_objs = {}
for name, slug, typ, icon, color, desc in cats:
    c = AnimalCategory.objects.create(name=name, slug=slug, type=typ, icon=icon, color=color, description=desc)
    cat_objs[slug] = c
print(f"✅ {AnimalCategory.objects.count()} kategoriya")

print("🦁 Hayvonlar qo'shilmoqda...")
animals_data = [
    ("uy-hayvonlari", "Mushuk", "Cat", "Uyda yashaydi, sichqon tutadi", "Uyda", "Sut, baliq", "Mushuklar qorong'uda ham ko'ra oladi!", "#FFB6C1"),
    ("uy-hayvonlari", "It", "Dog", "Eng sodiq do'st", "Uyda, hovlida", "Go'sht, non", "Itlar 1000 xil hidni ajrata oladi!", "#F7DC6F"),
    ("uy-hayvonlari", "Tovuq", "Chicken", "Tuxum beradi", "Katakda", "Don", "Tovuqlar har kuni tuxum qo'yadi!", "#F8C471"),
    ("uy-hayvonlari", "Sigir", "Cow", "Sut beradi", "Molxonada", "O't, pichan", "Sigir kuniga 100 litr suv ichadi!", "#D7BDE2"),
    ("yovvoyi-hayvonlar", "Sher", "Lion", "O'rmon qiroli", "Afrikada", "Go'sht", "Sher kuniga 20 soat uxlaydi!", "#F1948A"),
    ("yovvoyi-hayvonlar", "Fil", "Elephant", "Eng katta hayvon", "Afrika, Hindiston", "O't, barg", "Fil burnida 40 ming mushak bor!", "#AED6F1"),
    ("yovvoyi-hayvonlar", "Maymun", "Monkey", "Daraxtdan daraxtga sakraydi", "O'rmonda", "Banan, meva", "Maymunlar odamga o'xshaydi!", "#A9DFBF"),
    ("qushlar", "Chumchuq", "Sparrow", "Kichkina chiroyli qush", "Daraxtda", "Don, hasharot", "Chumchuq juda tez uchadi!", "#A3E4D7"),
    ("qushlar", "To'tiqush", "Parrot", "Gapira oladigan qush", "Uyda, o'rmonda", "Don, meva", "To'tiqush odam ovozini qaytara oladi!", "#85C1E2"),
    ("suv-hayvonlari", "Baliq", "Fish", "Suvda yashaydi", "Dengiz, daryo", "Suv o'tlari", "Baliqlar suvda nafas oladi!", "#87CEEB"),
]

for cat_slug, name, name_en, desc, where, eats, fact, color in animals_data:
    Animal.objects.create(
        category=cat_objs[cat_slug],
        name=name,
        name_en=name_en,
        description=desc,
        where_lives=where,
        what_eats=eats,
        interesting_fact=fact,
        color=color,
    )
print(f"✅ {Animal.objects.count()} ta hayvon")

print("🎨 Ranglar...")
colors_data = [
    ("Qizil", "Red", "#FF0000"),
    ("Ko'k", "Blue", "#0000FF"),
    ("Yashil", "Green", "#00FF00"),
    ("Sariq", "Yellow", "#FFFF00"),
    ("Qora", "Black", "#000000"),
    ("Oq", "White", "#FFFFFF"),
    ("Pushti", "Pink", "#FF69B4"),
    ("Binafsha", "Purple", "#800080"),
    ("Jigarrang", "Brown", "#A52A2A"),
    ("Apelsin rang", "Orange", "#FFA500"),
]

for i, (name, name_en, hex_code) in enumerate(colors_data):
    Color.objects.create(name=name, name_en=name_en, hex_code=hex_code, order=i)
print(f"✅ {Color.objects.count()} ta rang")

print("💬 So'zlashuv mavzulari...")
topics_data = [
    ("Salomlashish", "salomlashish", "👋", "#FF6B6B", "Birinchi uchrashuvda qanday salomlashamiz"),
    ("Tanishish", "tanishish", "🤝", "#4ECDC4", "Ismimizni aytish va tanishish"),
    ("Oila", "oila", "👨‍👩‍👧‍👦", "#FFE66D", "Oila a'zolari haqida gaplashish"),
    ("O'yinchoqlar", "oyinchoqlar", "🧸", "#8E44AD", "O'yinchoqlar haqida"),
    ("Taomlar", "taomlar", "🍎", "#F39C12", "Sevimli taomlar"),
    ("Yordam so'rash", "yordam", "🙏", "#3498DB", "Iltimos, rahmat, kechirasiz"),
]

topic_objs = {}
for title, slug, icon, color, desc in topics_data:
    t = ConversationTopic.objects.create(title=title, slug=slug, icon=icon, color=color, description=desc)
    topic_objs[slug] = t

phrases_data = [
    ("salomlashish", "Salom!", "Do'stona salomlashish", "Salom, do'stim!", "oson"),
    ("salomlashish", "Assalomu alaykum!", "Hurmat bilan salomlashish", "Assalomu alaykum, buvim!", "oson"),
    ("salomlashish", "Xayr!", "Xayrlashish", "Xayr, ertaga ko'rishamiz!", "oson"),
    ("salomlashish", "Qalaysan?", "Ahvol so'rash", "Salom, qalaysan?", "oson"),
    ("tanishish", "Mening ismim ...", "Ismni aytish", "Mening ismim Jasur!", "oson"),
    ("tanishish", "Sen kimisan?", "Tanishish savoli", "Salom, sen kimisan?", "oson"),
    ("tanishish", "Men 5 yoshdaman", "Yoshni aytish", "Men 5 yoshdaman!", "orta"),
    ("oila", "Bu onam", "Oilani tanishtirish", "Bu mening onam, u juda mehribon", "oson"),
    ("oila", "Bu dadam", "Dadani tanishtirish", "Bu dadam, u kuchli!", "oson"),
    ("oila", "Men oilamni yaxshi ko'raman", "Sevgi izhori", "", "orta"),
    ("oyinchoqlar", "Bu mening o'yinchog'im", "O'yinchoqni ko'rsatish", "Bu mening ayiqcham", "oson"),
    ("oyinchoqlar", "Birga o'ynaymizmi?", "O'ynashga taklif", "Kel, birga o'ynaymiz!", "orta"),
    ("taomlar", "Men olma yeyapman", "Taom haqida gapirish", "Olma juda shirin!", "oson"),
    ("taomlar", "Rahmat, to'ydim", "To'yganini aytish", "Rahmat oyijon, to'ydim", "oson"),
    ("yordam", "Iltimos", "Iltimos so'zi", "Iltimos, suv bering", "oson"),
    ("yordam", "Rahmat!", "Minnatdorchilik", "Katta rahmat!", "oson"),
    ("yordam", "Kechirasiz", "Uzr so'rash", "Kechirasiz, bilmay qoldim", "orta"),
]

for topic_slug, text, trans, example, diff in phrases_data:
    Phrase.objects.create(
        topic=topic_objs[topic_slug],
        text=text,
        translation=trans,
        example=example,
        difficulty=diff,
    )
print(f"✅ {ConversationTopic.objects.count()} mavzu, {Phrase.objects.count()} ibora")

print("\n🎉 Demo ma'lumotlar tayyor! Endi admin panelga kirib rasm va ovoz qo'shishingiz mumkin.")
print("Admin: python manage.py createsuperuser")
