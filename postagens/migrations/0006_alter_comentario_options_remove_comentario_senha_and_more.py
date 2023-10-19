# Generated by Django 4.2.5 on 2023-10-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagens', '0005_alter_comentario_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='senha',
        ),
        migrations.AddField(
            model_name='comentario',
            name='atualizado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
