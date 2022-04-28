# Generated by Django 3.2.8 on 2021-10-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('imdb_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('movie_link', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('War', 'War'), ('Comedy', 'Comedy'), ('Suspense', 'Suspense'), ('-', '-')], default='-', max_length=10)),
                ('poster', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]