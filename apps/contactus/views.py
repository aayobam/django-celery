from django.urls import reverse_lazy
from apps.contactus.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView



class ContactUsView(FormView):
    form_class = ContactForm
    template_name = "contact_us.html"
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        form.send_contact_mail()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html"
