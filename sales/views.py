from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import CustomerInformation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .consts import ITEM_PER_PAGE
from django.db.models import Q

# Create your views here.
def index_view(request):
    return render(request, 'sales/index.html')

class ListSalesView(LoginRequiredMixin, ListView):
    model = CustomerInformation
    template_name = 'sales/sales_list.html'
    paginate_by = ITEM_PER_PAGE
    
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            object_list = CustomerInformation.objects.filter(
                Q(customer_name__icontains=query) | Q(place__icontains=query))
        else:
            object_list = CustomerInformation.objects.all()
        return object_list
    
    
class DetailSalesView(LoginRequiredMixin, DetailView):
    model = CustomerInformation
    object_list = CustomerInformation.objects.all()
    template_name = 'sales/sales_detail.html'
    
class CreateSalesView(LoginRequiredMixin, CreateView):
    template_name = 'sales/sales_create.html'
    model = CustomerInformation
    fields = ('user', 'date', 'customer_name', 'age', 'work', 'business', 'place', 'wants', 'result', 'other')
    success_url = reverse_lazy('sales')

class DeleteSalesView(LoginRequiredMixin, DeleteView):
    model = CustomerInformation
    object_list = CustomerInformation.objects.all()
    template_name = 'sales/sales_delete.html'
    fields = ('user', 'date', 'customer_name', 'age', 'work', 'business' 'place', 'wants', 'result', 'other')
    success_url = reverse_lazy('sales')

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

class UpdateSalesView(LoginRequiredMixin, UpdateView):
    model = CustomerInformation
    object_list = CustomerInformation.objects.all()
    template_name = 'sales/sales_update.html'
    fields = ('user', 'date', 'customer_name', 'age', 'work', 'business', 'place', 'wants', 'result', 'other')
    
    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})