from django.db import models

class GlobalSetting(models.Model):
    id = models.CharField(verbose_name="ID", max_length=50, primary_key=True, default="development")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    
    class Meta:
        verbose_name = "Глобальная настройка"
        verbose_name_plural = "Глобальные настройки"
    
    def __str__(self):
        return self.id

class Variables(models.Model):
    name = models.CharField(verbose_name="Имя переменной", max_length=50, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    value = models.CharField(verbose_name="Значение", max_length=150, blank=True, null=True)
    
    class Meta:
        verbose_name = "Переменная"
        verbose_name_plural = "Переменные"
    
    def __str__(self):
        return self.name