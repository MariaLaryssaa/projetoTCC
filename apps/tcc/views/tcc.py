from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from apps.tcc.models import TCC, Autor, Curso, Orientador
from apps.tcc.form import TCCForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class TCCCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = TCCForm
    success_message = 'TCC cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_tcc_usuario")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCCs - Arquivos'
        context['descricao'] = 'Cadastro de TCC'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class TCCUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = TCC
    form_class = TCCForm
    success_message = 'TCC atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_tcc_usuario")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCCs- Arquivos'
        context['descricao'] = 'Editar TCCs'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TCCDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = TCC
    success_message = 'TCC excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_tcc_usuario")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCCs - Arquivos'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TCCDelete, self).delete(request, *args, **kwargs)

class TCCList(ListView):
    model = TCC
    template_name = "index.html"

class TCCDetail(DetailView):
    model = TCC
    template_name = "cadastros/detalhes/tcc.html"

class TCCListPorUsuario(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = TCC
    template_name = "cadastros/listas/dashboard.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return TCC.objects.filter(titulo=self.request.user, titulo__icontains=nome)
        else:
            return TCC.objects.filter(titulo=self.request.user)

class TCCAutorList(ListView):
    model = TCC
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return TCC.objects.filter(autor=Autor.objects.get(pk=self.kwargs['autor']), titulo__icontains=nome)
        else:
            return TCC.objects.filter(autor=Autor.objects.get(pk=self.kwargs['autor']))

class TCCCursoList(ListView):
    model = TCC
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return TCC.objects.filter(curso=Curso.objects.get(pk=self.kwargs['curso']), titulo__icontains=nome)
        else:
            return TCC.objects.filter(curso=Curso.objects.get(pk=self.kwargs['curso']))

class TCCOrientadorList(ListView):
    model = TCC
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return TCC.objects.filter(orientador=Orientador.objects.get(pk=self.kwargs['orientador']), titulo__icontains=nome)
        else:
            return TCC.objects.filter(orientador=Orientador.objects.get(pk=self.kwargs['orientador']))