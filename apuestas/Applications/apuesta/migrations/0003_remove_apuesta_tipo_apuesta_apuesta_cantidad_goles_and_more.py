# Generated by Django 4.1.4 on 2022-12-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuesta', '0002_tipoapuesta_puntos_alter_apuesta_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apuesta',
            name='tipo_apuesta',
        ),
        migrations.AddField(
            model_name='apuesta',
            name='cantidad_goles',
            field=models.IntegerField(default=0, verbose_name='Tarjetas Rojas'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='goles_equipo_local',
            field=models.IntegerField(default=0, verbose_name='Goles Equipo Local'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='goles_equipo_visitante',
            field=models.IntegerField(default=0, verbose_name='Goles Equipo Visitante'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='tarjetas_amarillas',
            field=models.IntegerField(default=0, verbose_name='Tarjetas Amarillas'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='tarjetas_rojas',
            field=models.IntegerField(default=0, verbose_name='Tarjetas Rojas'),
        ),
    ]
