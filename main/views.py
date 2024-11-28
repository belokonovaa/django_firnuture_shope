from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Магазин мебели HOME'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Мебель, которая создаёт атмосферу вашего дома.' \
                                  'Мы предлагаем не просто предметы интерьера, а продуманные решения, которые подчеркивают ' \
                                  'ваш стиль и отвечают самым высоким требованиям к качеству и функциональности.'
        return context


class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Доставка и оплата'
        context['content'] = 'Доставка и оплата'
        context['text_on_page'] = 'Мы ценим ваше время и стремимся сделать процесс покупки максимально удобным.' \
                                  'Поэтому предлагаем вам гибкие условия доставки и оплаты.' \
                                  'Наша цель — сделать процесс покупки простым и комфортным. '
        return context


class InformationView(TemplateView):
    template_name = 'main/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Контактная информация'
        context['content'] = 'Контактная информация'
        context['text_on_page'] = 'Если у вас есть вопросы или пожелания, не стесняйтесь обращаться к нам! '\
                                  'Мы всегда рады помочь вам.'
        return context




