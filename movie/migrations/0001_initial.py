#执行python3 manage.py makemigrations 生成迁移文件 当前这个文件就是这样来的
#而其他的0002 0003等都是django自带的一些表，自动生成的
#再执行python3 manage.py migrate 开始迁移2 将每一个应用下的migrations目录中的中间文件同步回数据库
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(#建个表，名字叫Genre
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Genre',
            },
        ),#要创建这些表，就要先写模型类，然后生成迁移文件，去迁移
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('poster', models.FileField(max_length=256, upload_to='')),
                ('duration', models.CharField(max_length=256)),
                ('release_time', models.CharField(max_length=256)),
                ('intro', models.TextField()),
                ('director', models.CharField(max_length=256)),
                ('writers', models.CharField(max_length=256)),
                ('actors', models.CharField(max_length=512)),
                ('genre', models.ManyToManyField(to='movie.Genre')),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='Movie_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(5)])),
                ('comment', models.TextField(blank=True)),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
            options={
                'db_table': 'Movie_rating',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('rating_movies', models.ManyToManyField(through='movie.Movie_rating', to='movie.Movie')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.AddField(
            model_name='movie_rating',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.User'),
        ),
    ]
