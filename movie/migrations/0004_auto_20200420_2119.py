
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200420_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_rating',
            old_name='mid',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='movie_rating',
            old_name='uid',
            new_name='user',
        ),
    ]
