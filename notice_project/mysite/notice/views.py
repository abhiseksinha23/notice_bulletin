from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from notice.models import Notices,queries,addinfo
from django.utils import timezone
from django.http import HttpResponseRedirect
from notice.forms import queriesForm, addinfoForm, NoticesForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = 'about.html'

class NoticesListView(ListView):
    model = Notices

    def get_queryset(self):
        return Notices.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NoticesDetailView(DetailView):
    model = Notices


class CreateNoticeView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'notice/notices_detail.html'

    form_class = NoticesForm

    model =  Notices


class NoticeUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'notice/notices_detail.html'

    form_class = NoticesForm

    model = Notices


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'notice/notices_list.html'

    model = Notices

    def get_queryset(self):
        return Notices.objects.filter(published_date__isnull=True).order_by('created_date')


class NoticeDeleteView(LoginRequiredMixin,DeleteView):
    model = Notices
    success_url = reverse_lazy('notices_list')


@login_required
def notice_publish(request, pk):
    notice = get_object_or_404(Notices, pk=pk)
    notice.publish()
    return redirect('notices_detail', pk=pk)

@login_required
def add_info_to_notice(request, pk):
    notice = get_object_or_404(Notices, pk=pk)
    if request.method == "POST":
        form = addinfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.notice = notice
            info.save()
            return redirect('notices_detail', pk=notice.pk)
    else:
        form = addinfoForm()
    return render(request, 'notice/addinfo_form.html', {'form': form})


@login_required
def info_approve(request, pk):
    info = get_object_or_404(addinfo, pk=pk)
    info.approve()
    return redirect('notices_detail', pk=info.notice.pk)


@login_required
def info_remove(request, pk):
    info = get_object_or_404(addinfo, pk=pk)
    notice_pk = info.notice.pk
    info.delete()
    return redirect('notices_detail', pk=notice_pk)


class CreateQueryView(CreateView):
    redirect_field_name = 'notice/thanks.html'

    form_class = queriesForm

    model =  queries

class QueryListView(ListView):
    model = queries

class QuaryDetailView(DetailView):
    model =  queries

class QueryDeleteView(DeleteView):
    model = queries
    success_url = reverse_lazy('queries_list')


class thanksView(TemplateView):
    template_name = 'thanks.html'
