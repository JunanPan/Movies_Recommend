
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200421_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField()),
                ('movie_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_source', to='movie.Movie')),
                ('movie_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_target', to='movie.Movie')),
            ],
            options={
                'ordering': ['-similarity'],
            },
        ),
        migrations.AlterField(
            model_name='movie_rating',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_similarity',
            field=models.ManyToManyField(through='movie.Movie_similarity', to='movie.Movie'),
        ),
    ]
