from django.views.generic import TemplateView, FormView
from core.forms import ContactForm, SingUpForm

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'
    page_title = 'Index'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class ThankYouTemplateView(TemplateView):
    template_name = 'core/thank-you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Thank-You'
        return context

class ContactFormView(FormView):
    template_name = 'core/contact-us.html'
    form_class = ContactForm
    success_url = '/thank-you.html/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Thank-You'
        context['nav_text_contact'] = 'active'
        return context

    def form_valid(self, form):
        form.load_in_db()
        return super().form_valid(form)

class SingUpFormView(FormView):
    template_name = 'core/singup.html'
    form_class = SingUpForm
    success_url = '/account/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_singup'] = 'active'
        return context

    def form_valid(self, form):
        form.save()
        # form.authenticate_user(self)
        return super().form_valid(form)

