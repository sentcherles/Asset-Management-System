from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Asset

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['excludeNav'] = True
        return context

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['excludeNav'] = True
        return context


@login_required
def viewAssets(request):
    assets = Asset.objects.all()
    return render(request, 'viewAssets.html', {'assets': assets})


@login_required
def assetState(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = UpdateStateForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('assetDetail', pk=asset.pk)
    else:
        form = UpdateStateForm(instance=asset)
    return render(request, 'assetState.html', {'form': form, 'asset': asset})


class AssetsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Asset
    template_name = 'assetDetail.html'
    context_object_name = 'asset'


@login_required
def adminDashboard(request):
    return render(request, "dashboards/adminDashboard.html")


@login_required
def assetmanagerDashboard(request):
    return render(request, "dashboards/assetmanagerDashboard.html")


@login_required
def technicianDashboard(request):
    return render(request, "dashboards/technicianDashboard.html")


@login_required
def reporterDashboard(request):
    return render(request, "dashboards/reporterDashboard.html")


@login_required
def auditorDashboard(request):
    return render(request, "dashboards/auditorDashboard.html")


@login_required
def userDashboard(request):
    return render(request, "dashboards/userDashboard.html")


@login_required
def verificationPage(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        return redirect("/admin/")
    elif user.groups.filter(name="Asset Manager").exists():
        return redirect("assetmanagerDashboard")
    elif user.groups.filter(name="Technician").exists():
        return redirect("technicianDashboard")
    elif user.groups.filter(name="Auditor").exists():
        return redirect("auditorDashboard")
    elif user.groups.filter(name="Reporter").exists():
        return redirect("reporterDashboard")
    elif user.groups.filter(name="User").exists():
        return redirect("userDashboard")
    else:
        return redirect("login")


def register_or_redirect(request):
    if request.user.is_authenticated:
        return redirect('verification')
    return redirect('register')


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'serialNumber', 'manufacturer', 'datePurchased', 'state']


class CreateAssetView(LoginRequiredMixin, generic.CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'assetForm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateStateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['state']
