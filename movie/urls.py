from django.urls import path, reverse
from . import views  # 用相对导入，导入views
# 子路由 匹配具体项目
app_name = 'movie'

# 必须有这个变量urlpatterns，拼错了就报错
urlpatterns = [
    # 默认首页
    # 地址，视图函数，name
    # name是为地址起别名
    # 视图函数，用来接收请求，返回html
    path('', views.IndexView.as_view(), name='index'),
    # 加括号，引入的是执行结果。不加括号，引入的是函数
    # 热门电影
    # http://127.0.0.1:8000/hot进来，匹配到hot了，把请求交给views.PopularMovieView.as_view()去处理
    path('hot', views.PopularMovieView.as_view(), name='hot'),
    # 登录
    path('login', views.LoginView.as_view(), name='login'),
    # 退出
    path('logout', views.UserLogout, name='logout'),
    # 注册
    path('register', views.RegisterView.as_view(), name='register'),
    # 分类查看
    path('tag', views.TagView.as_view(), name='tag'),
    # 电影详情页面
    path('detail/<int:pk>', views.MovieDetailView.as_view(), name='detail'),
    # 评分历史页面
    path('history/<int:pk>', views.RatingHistoryView.as_view(), name='history'),
    # 删除记录
    path('del_rec/<int:pk>', views.delete_recode, name='delete_record'),
    # 推荐页面
    path('recommend', views.RecommendMovieView.as_view(), name='recommend'),
    # 导入物品之间的相似度
    # path('calc_movie_similarity',views.calc_movie_similarity,name='calc_similarity')
]
