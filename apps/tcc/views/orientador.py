from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from apps.tcc.models import Orientador
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Orientador
    fields = '__all__'
    success_message = 'Orientador cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientador")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientador - Arquivos'
        context['descricao'] = 'Cadastro de Orientador'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Orientador
    fields = '__all__'
    success_message = 'Orientador atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientador")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientador - Arquivos'
        context['descricao'] = 'Editar Orientador'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Orientador
    success_message = 'Orientador excluído com sucesso!'
    error_message = 'Orientador não pode ser excluído!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_orientador")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientador - Arquivos'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrientadorDelete, self).delete(request, *args, **kwargs)


class OrientadorList(ListView):
    model = Orientador
    template_name = "cadastros/listas/orientador.html"