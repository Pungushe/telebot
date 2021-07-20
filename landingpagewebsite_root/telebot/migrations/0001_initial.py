# Generated by Django 3.2.3 on 2021-05-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tq_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tq_chat', models.CharField(max_length=200, verbose_name='Чат айди')),
                ('tq_message', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Настройку',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]