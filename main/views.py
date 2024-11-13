from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Мебель, которая создаёт атмосферу вашего дома. '
                        'Мы предлагаем не просто предметы интерьера, а продуманные решения, которые подчеркивают '
                        'ваш стиль и отвечают самым высоким требованиям к качеству и функциональности. '
    }
    return render(request, 'main/about.html', context)


def delivery(request):
    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Мы ценим ваше время и стремимся сделать процесс покупки максимально удобным. '
                        'Поэтому предлагаем вам гибкие условия доставки и оплаты.'
                        'Наша цель — сделать процесс покупки простым и комфортным. '
    }
    return render(request, 'main/delivery.html', context)


def information (request):
    context = {
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
        'text_on_page': 'Если у вас есть вопросы или пожелания, не стесняйтесь обращаться к нам! '
                        'Мы всегда рады помочь вам.'
    }
    return render(request, 'main/info.html', context)




