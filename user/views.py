from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import CustomUserCreationForm
from django.core.mail import send_mail


class RegisterView(CreateView):
    template_name = 'user/user_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе'
        from_email = 'puxeen@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)