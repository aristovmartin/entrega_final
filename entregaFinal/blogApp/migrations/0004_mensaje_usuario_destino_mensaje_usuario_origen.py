# Generated by Django 4.0.4 on 2022-06-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_alter_perfil_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='usuario_destino',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario_origen',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
