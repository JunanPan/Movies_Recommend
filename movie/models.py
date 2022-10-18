from django.db import models
from django.db.models import Avg
from django.core import validators
# 模型层，主要在这里写代码
# 模型是数据交互的接口
# 模型类中的每一个了类属性都代表数据库的一个字段
# ORM框架（对象关系映射）：使用类和对象对数据库进行操作，避免了用sql语句

# 这边每次更新，如修改字段啥的，都要重新make migrations make migrate
# Genre数据自己导入


class Genre(models.Model):  # 继承models.Model的类就是模型类
    # name就是类属性，对应数据表中的一个字段
    name = models.CharField(max_length=100)

    class Meta:  # 通过内部类改变名字
        db_table = 'Genre'

    def __str__(self):  # 定义__str__方法，自定义输出格式
        # 输出Genre.objects.all()的时候可以看到输出结果
        # 在views中调用定义
        return f"<Genre:{self.name}>"


class Movie(models.Model):  # 会生成movie_movie表 即：应用名—类名
    # 电影名
    name = models.CharField(max_length=256)
    # imdb_id是info文件里面的电影顺序
    imdb_id = models.IntegerField()

    # 时长
    time = models.CharField(max_length=256, blank=True)
    # 类型
    # 多对多，django自动生成第三张表 这里是movie_genre
    # manyTomany在任意一个类中添加即可
    genre = models.ManyToManyField(Genre)  # 没有指定Through，会自动生成movie_genre表

    # 发行时间
    release_time = models.CharField(max_length=256, blank=True)
    # 简介
    intro = models.TextField(blank=True)
    # 导演
    director = models.CharField(max_length=256, blank=True)
    # 编剧
    writers = models.CharField(max_length=256, blank=True)
    # 演员
    actors = models.CharField(max_length=512, blank=True)
    # 电影和电影之间的相似度,A和B的相似度与B和A的相似度是一致的，所以symmetrical（对称）设置为False
    # 直接通过Movie_similarity实现关联
    # self,自己的id和自己的id进行关联，两个字段分别为 movie_source_id/movie_target_id
    movie_similarity=models.ManyToManyField("self",through="Movie_similarity",symmetrical=False)
    # 使用内部Meta类，给模型赋予属性，Meta下有很多内建的类属性，可以对模型类做一些控制

    class Meta:
        db_table = 'Movie'  # 改表名
        # 改完后依然要make migration migrate

    def __str__(self):
        return f"<Movie:{self.name},{self.imdb_id}>"

    def get_score(self):
        # 定义一个获取平均分的方法，模板中直接调用即可
        # 格式 {'score__avg': 3.125}
        # __set反向属性，对应另一端类名的小写+下划线set
        result_dct = self.movie_rating_set.aggregate(Avg('score'))  # 以movie_id分组，对score做聚合
        try:
            # 只保留一位小数
            result = round(result_dct['score__avg'], 1)
        except TypeError:
            return 0
        else:
            return result

    def get_user_score(self, user):
        return self.movie_rating_set.filter(user=user).values('score')

    def get_score_int_range(self):
        return range(int(self.get_score()))

    def get_genre(self):
        # 和genre关联，可以直接.genre查询
        genre_dct = self.genre.all().values('name')
        genre_lst = []
        for dct in genre_dct.values():
            genre_lst.append(dct['name'])
        return genre_lst

    def get_similarity(self, k=5):
        # 获取5部最相似的电影的id
        similarity_movies = self.movie_similarity.all()[:k]
        print(similarity_movies)
        # objects是管理器对象 数据的增删改查可以通过object来实现
        # 调用就是模型类.objects.调用方法
        # movies=Movie.objects.filter(=similarity_movies)
        # print(movies)
        return similarity_movies


class Movie_similarity(models.Model):  # 对应movie_movie_similarity
    # on_delete级联删除的一个规则
    movie_source = models.ForeignKey(Movie, related_name='movie_source', on_delete=models.CASCADE)  # models.CASCADE串联，要删一起删
    movie_target = models.ForeignKey(Movie, related_name='movie_target', on_delete=models.CASCADE)
    similarity = models.FloatField()

    class Meta:
        # 按照相似度降序排序
        ordering = ['-similarity']


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)  # 唯一约束
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)  # 邮件，也加个唯一约束吧 别有重复了
    rating_movies = models.ManyToManyField(Movie, through="Movie_rating")  # 指定第三张表就是这个Movie_rating

    def __str__(self):
        return "<USER:( name: {:},password: {:},email: {:} )>".format(self.name, self.password, self.email)

    class Meta:
        db_table = 'User'


class Movie_rating(models.Model):
    # 评分的用户
    # foreignKey 一对多关联
    # 在数据表movie_rating中中就是user_id，一个外键 #有指定Through的ManyToMany都要ForeignKey来明确
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    # 评分的电影
    # 在数据表movie_rating中就是movie_id，外键
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, unique=False)
    # 分数
    score = models.FloatField()
    # 评论，可选
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Movie_rating'


class Movie_hot(models.Model):
    """存放最热门的一百部电影"""
    # 电影外键
    # movie_hot表中的movie_id
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 评分人数
    rating_number = models.IntegerField()

    class Meta:
        db_table = 'Movie_hot'
        ordering = ['-rating_number']  # 热度，从大到小排序
