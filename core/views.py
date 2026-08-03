from django.shortcuts import render, get_object_or_404
from .models import Letter, Number, Animal, AnimalCategory, ConversationTopic, Phrase, Color, Exercise

def home(request):
    letters = Letter.objects.filter(is_active=True)[:8]
    numbers = Number.objects.filter(is_active=True)[:10]
    categories = AnimalCategory.objects.all()[:6]
    animals = Animal.objects.filter(is_active=True)[:6]
    topics = ConversationTopic.objects.filter(is_active=True)[:6]
    colors = Color.objects.filter(is_active=True)[:8]
    
    context = {
        'letters': letters,
        'numbers': numbers,
        'categories': categories,
        'animals': animals,
        'topics': topics,
        'colors': colors,
        'letters_count': Letter.objects.filter(is_active=True).count(),
        'numbers_count': Number.objects.filter(is_active=True).count(),
        'animals_count': Animal.objects.filter(is_active=True).count(),
        'phrases_count': Phrase.objects.filter(is_active=True).count(),
    }
    return render(request, 'home.html', context)

# HARFLAR
def letter_list(request):
    letters = Letter.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/letter_list.html', {'letters': letters})

def letter_detail(request, pk):
    letter = get_object_or_404(Letter, pk=pk, is_active=True)
    all_letters = Letter.objects.filter(is_active=True).order_by('order')
    # prev/next
    prev_letter = Letter.objects.filter(is_active=True, order__lt=letter.order).order_by('-order').first()
    next_letter = Letter.objects.filter(is_active=True, order__gt=letter.order).order_by('order').first()
    if not next_letter:
        # try by id if order same
        next_letter = Letter.objects.filter(is_active=True, pk__gt=letter.pk).order_by('pk').first()
    if not prev_letter:
        prev_letter = Letter.objects.filter(is_active=True, pk__lt=letter.pk).order_by('-pk').first()
    
    context = {
        'letter': letter,
        'all_letters': all_letters,
        'prev_letter': prev_letter,
        'next_letter': next_letter,
    }
    return render(request, 'core/letter_detail.html', context)

# RAQAMLAR
def number_list(request):
    numbers = Number.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/number_list.html', {'numbers': numbers})

def number_detail(request, pk):
    number = get_object_or_404(Number, pk=pk, is_active=True)
    all_numbers = Number.objects.filter(is_active=True).order_by('order')
    prev_number = Number.objects.filter(is_active=True, order__lt=number.order).order_by('-order').first() or Number.objects.filter(is_active=True, value__lt=number.value).order_by('-value').first()
    next_number = Number.objects.filter(is_active=True, order__gt=number.order).order_by('order').first() or Number.objects.filter(is_active=True, value__gt=number.value).order_by('value').first()
    return render(request, 'core/number_detail.html', {
        'number': number,
        'all_numbers': all_numbers,
        'prev_number': prev_number,
        'next_number': next_number,
    })

# HAYVONLAR
def animal_category_list(request):
    categories = AnimalCategory.objects.all().order_by('order')
    return render(request, 'core/animal_category_list.html', {'categories': categories})

def animal_list(request, slug=None):
    categories = AnimalCategory.objects.all()
    if slug:
        category = get_object_or_404(AnimalCategory, slug=slug)
        animals = Animal.objects.filter(category=category, is_active=True).order_by('order')
    else:
        category = None
        animals = Animal.objects.filter(is_active=True).order_by('order')
    
    # filtering by type query param
    type_filter = request.GET.get('type')
    if type_filter:
        animals = animals.filter(category__type=type_filter)
    
    context = {
        'animals': animals,
        'categories': categories,
        'current_category': category,
        'type_filter': type_filter,
    }
    return render(request, 'core/animal_list.html', context)

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk, is_active=True)
    related = Animal.objects.filter(category=animal.category, is_active=True).exclude(pk=animal.pk)[:4]
    return render(request, 'core/animal_detail.html', {'animal': animal, 'related': related})

# RANGLAR
def color_list(request):
    colors = Color.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/color_list.html', {'colors': colors})

# SO'ZLASHUV
def conversation_list(request):
    topics = ConversationTopic.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/conversation_list.html', {'topics': topics})

def conversation_detail(request, slug):
    topic = get_object_or_404(ConversationTopic, slug=slug, is_active=True)
    phrases = topic.phrases.filter(is_active=True).order_by('order')
    all_topics = ConversationTopic.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/conversation_detail.html', {
        'topic': topic,
        'phrases': phrases,
        'all_topics': all_topics,
    })

# mashqlar
def exercise_list(request):
    exercises = Exercise.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/exercise_list.html', {'exercises': exercises})
