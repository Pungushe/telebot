# Generated by Django 3.2.3 on 2021-05-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmpSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smp_img', models.ImageField(upload_to='Sliderimg/')),
                ('smp_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('smp_text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
