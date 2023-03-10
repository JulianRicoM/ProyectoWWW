# Generated by Django 4.1.4 on 2022-12-17 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partidos', '0003_alter_resultado_resultado'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_apuesta', models.CharField(max_length=30, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='TipoApuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_apuesta', models.CharField(max_length=30, verbose_name='Apuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuesta.estado')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partidos.partidos')),
                ('tipo_apuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuesta.tipoapuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
