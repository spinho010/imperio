# Generated by Django 3.1.7 on 2021-06-02 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bairro_internet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro_net', models.CharField(max_length=60)),
                ('nome_rua', models.CharField(blank=True, max_length=60, null=True, verbose_name='Rua:')),
            ],
        ),
        migrations.CreateModel(
            name='plano_internet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_plano', models.CharField(max_length=60)),
                ('data_assinatura', models.CharField(blank=True, max_length=60, null=True, verbose_name='Data Plano:')),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=60, verbose_name='Nome Completo:')),
                ('endereço', models.ForeignKey(max_length=60, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendas.bairro_internet')),
                ('plano', models.ForeignKey(max_length=60, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendas.plano_internet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
