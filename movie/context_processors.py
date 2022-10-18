from .models import User
'''
如果我们不使用上下文处理器的话，那么我们需要在每一个视图函数中都去获取一下session中的user_id,这就是一件很不爽的事情了，
而如果我们定义了上下文处理器，那么我们就不需要每一个视图函数中都去获取session中user_id的值了，只需要在上下文处理器中去获取就是了。
'''


# 上下文处理器
def movie_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user=User.objects.get(pk=user_id)
            context['movie_user'] = user
        except:
            pass
    return context
