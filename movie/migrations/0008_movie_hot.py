
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200504_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_hot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_number', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
            options={
                'db_table': 'Movie_hot',
                'ordering': ['-rating_number'],
            },
        ),
    ]
