from django.db.models import Count

from post.models import Post


def getRightIngo(request):
    #1、获取分类的信息
    r_cate_post = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    #2、近期文章
    r_crae_post = Post.objects.all().order_by('-created')[:3]

    # 3.获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(
        "select created,count('*') c from t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c desc,created desc")
    r_filepost = cursor.fetchall()

    return {'r_cate_post': r_cate_post, 'r_crae_post': r_crae_post, 'r_filepost': r_filepost}