# Generated by Django 4.0.5 on 2024-03-20 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_finished', models.DateTimeField(auto_now_add=True)),
                ('game_type', models.CharField(choices=[('MathGame', 'Math Facts Practice'), ('AnagramGame', 'Anagram Hunt')], max_length=200)),
                ('game_settings', models.JSONField(default=dict)),
                ('final_score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]