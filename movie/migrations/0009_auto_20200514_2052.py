
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_hot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Movie',
            old_name='movie_id',
            new_name='imdb_id'
        )
    ]
