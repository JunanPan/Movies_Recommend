
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200420_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='poster',
            new_name='movie_id',
        ),
    ]
