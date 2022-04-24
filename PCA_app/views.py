from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from .forms import DiapasonForm


def InputPage(request):
    if request.method == 'POST':
        form = DiapasonForm(request.POST)
        print('----------------')
        print(form.data)
        if (form.data.dict()['first_number'] == '') or (form.data.dict()['second_number'] == '') or \
                (form.data.dict()['first_number'] == '' and form.data.dict()['second_number'] == ''):
            return HttpResponse('<h1>Enter data into fields</h1>')
        if form.is_valid():
            cd = form.cleaned_data
            first = cd['first_number']
            second = cd['second_number']
            request.session['first'] = first
            request.session['second'] = second
            return HttpResponseRedirect('Graph', {'form': form}, RequestContext(request))
    else:
        form = DiapasonForm()
    return render(request, 'PCA_app/InputPage.html', {'form': form})
