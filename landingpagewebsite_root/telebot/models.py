from django.db import models

class TeleSettings(models.Model):
    tq_token=models.CharField(max_length=200, verbose_name='Токен')
    tq_chat=models.CharField(max_length=200, verbose_name='Чат айди')
    tq_message=models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tq_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
