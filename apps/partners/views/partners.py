from django.shortcuts import redirect, render
from apps.partners.forms.partner import PartnerForm
from apps.partners.models.partner import Partner


def partner_list(request):
    partners = Partner.objects.all()
    context = {
        'partners': partners
    }
    return render(request, 'partners/partner_list.html', context)


def partner_create(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()

    context = {
        'form': form,
        'title': 'Crear Nuevo Socio'
    }
    return render(request, 'partners/partner_form.html', context)

