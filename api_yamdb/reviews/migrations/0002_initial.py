# Generated by Django 3.2 on 2023-05-09 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(help_text='Автор отзыва', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(blank=True, help_text='Произведение, на которое написан отзыв', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Произведение'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='Автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(blank=True, help_text='Отзыв, к которому написан комментарий', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review', verbose_name='Отзыв'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='only_one_review'),
        ),
    ]
