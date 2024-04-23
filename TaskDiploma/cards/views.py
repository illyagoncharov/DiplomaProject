from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib import messages
from cards.forms import CardForm, CardEditForm
from cards.models import Card
from mainapp.constants import CardStatus


class AdminRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class TaskDashboard(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'cards/trellocards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = CardStatus.STATUS_LIST
        form = CardForm()
        context['form'] = form
        return context

    def post(self, request):
        form = request.POST
        card_id = form['card_id']
        step = form['nextstep']
        card = Card.objects.get(id=card_id)
        self.nextstatus(request, card, step)
        url= reverse('cards:taskdashboard')
        return redirect(url)

    def permissions_decorator(func):
        def wrapper(request, card, step):
            status = card.status
            p1 = request.user.is_superuser and status == "Ready" and step == "next"
            p2 = request.user.is_superuser and status == "Done" and step == "back"
            p3 = card.performer.id == request.user.id and status == "Ready" and step == "back"
            p4 = card.performer.id == request.user.id and status != "Ready" and status != "Done"
            p5 = card.performer.id == request.user.id and status != 'New' and step != 'back'
            permissions = (p1, p2, p3, p4, p5)
            if any(permissions):
                func(card, step)
            else:
                if request.user.is_superuser:
                    messages.error(request,
                                   f"No, {request.user}, it is impossible! Only between Ready and Done!")
                else:
                    messages.error(request,
                               f"No, {request.user}, it is impossible! Only your card and Only between New and Ready!")
        return wrapper

    @staticmethod
    @permissions_decorator
    def nextstatus(card, step):
        if step == 'back':
            step = CardStatus.back
        else:
            step = CardStatus.next
        status = card.status.lower().replace(" ",'')
        card.status = step[status]
        card.save()


class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    template_name = 'cards/card_create.html'
    fields = ['title', 'task', 'performer']

    def post(self, request, *args, **kwargs):
        form = CardForm(request.POST)
        print( request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Card.objects.create(user=self.request.user, title=cd['title'], task=cd['task'], performer=cd["performer"])
            messages.success(request,
                       f"Ok, {request.user}, you created a TaskCard!")
        else:
            messages.error(request,
                             f"Form is not valid: {form.errors.as_text()}")
            return HttpResponseRedirect(request.path)

        url = reverse("cards:taskdashboard")
        return redirect(url)


class CardEdit(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = CardForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            card_id = request.POST['card_id']
            Card.objects.filter(id=card_id).update(title=cd['title'], task=cd['task'], performer=cd['performer'])
            messages.success(request,
                             f"Ok, {request.user}, you update a TaskCard!")
        else:
            messages.error(request,
                             f"Form is not valid: {form.errors.as_text()}")

        url = reverse("cards:taskdashboard")
        return redirect(url)


class CardDelete(AdminRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'




