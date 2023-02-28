# Generated by Django 4.1.5 on 2023-02-28 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0008_joke_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='JokeVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to='jokes.joke')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='jokevote',
            constraint=models.UniqueConstraint(fields=('user', 'joke'), name='one_vote_per_user_per_joke'),
        ),
    ]
