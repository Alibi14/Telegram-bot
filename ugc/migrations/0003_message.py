# Generated by Django 3.2.4 on 2021-06-06 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_auto_20210606_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': ('Сообщение',),
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
