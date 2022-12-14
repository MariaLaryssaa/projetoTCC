# Generated by Django 4.1 on 2022-08-23 15:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=150)),
                ('ultimo_nome', models.CharField(max_length=150)),
                ('foto', models.ImageField(upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('modalidade', models.CharField(choices=[('B', 'Bacharelado'), ('L', 'Licenciatura'), ('T', 'Tecnológica')], max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=150)),
                ('ultimo_nome', models.CharField(max_length=150)),
                ('curriculo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('ano_documento', models.IntegerField(verbose_name='ano do documento')),
                ('resumo', models.TextField()),
                ('arquivo_documento', models.FileField(upload_to='arquivo/')),
                ('palavra_chave', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.autor')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.curso')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.orientador')),
            ],
        ),
    ]
