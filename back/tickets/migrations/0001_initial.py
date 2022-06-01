# Generated by Django 3.2.12 on 2022-06-01 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='poster/')),
                ('peoples', models.IntegerField(default=1)),
                ('place', models.CharField(max_length=100)),
                ('watch_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]