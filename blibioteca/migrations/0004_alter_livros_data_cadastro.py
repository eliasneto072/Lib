# Generated by Django 4.2.1 on 2023-06-02 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blibioteca', '0003_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
