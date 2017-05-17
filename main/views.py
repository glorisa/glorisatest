from django.shortcuts import render, HttpResponseRedirect
from .models import team, contact
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.conf import settings


class Index(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['leader'] = team.objects.filter(leader=True)
        context['others'] = team.objects.filter(leader=False)
        return context


def team_member_detail(request, **kwargs):
    member = team.objects.get(id=kwargs['id'])
    return render(request, 'main/profile.html', {'member_info': member})


def contactform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # send_mail(subject, message, email, ['gargsarthak30@gmail.com'], fail_silently=True)

        obj = contact.objects.create(name=name, company=company, phone=phone, email=email, subject=subject, message=message)

        subject = subject
        message = message + '\n' + "Name: " + name + '\n' + "company: " + company + '\n' + "phone: " + phone + '\n' + "email: " + email
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['gargsarthak30@gmail.com'], fail_silently=True)
        return HttpResponseRedirect(reverse('mail_success'))


class mail_success(TemplateView):
    template_name = 'main/_mail_success.html'