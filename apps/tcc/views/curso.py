from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from apps.tcc.models import Curso
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = '__all__'
    success_message = 'Curso cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos - Arquivos'
        context['descricao'] = 'Cadastro de Curso'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = '__all__'
    success_message = 'Curso atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos - Arquivos'
        context['descricao'] = 'Editar Curso'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    success_message = 'Curso excluído com sucesso!'
    error_message = 'Curso não pode ser excluído!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_curso")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos - Arquivos'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CursoDelete, self).delete(request, *args, **kwargs)


class CursoList(ListView):
    model = Curso
    template_name = "cadastros/listas/curso.html"