from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import math
# Create your views here.
#渲染主页面
def queryAll(request, num=1):
    num = int(num)
    # 获取所有数据
    postList = Post.objects.all().order_by('-created')

    #创建分页器Paginator对象
    pageOj = Paginator(postList, 1)

    #获取每页的数据
    pageList = pageOj.page(num)

    # 生成页码数列表
    # # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > pageOj.num_pages:
        end = pageOj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList1 = range(begin, end + 1)

    return render(request, 'index.html', {'postList': pageList, 'pageList1': pageList1, 'num': num})

#阅读全文功能
def deteil(request, postid):
    postid = int(postid)
    post = Post.objects.get(id=postid)
    print(post)
    return render(request, 'detail.html', {'post': post})

#根据类别id查询所有帖子
def queryPostByCid(request,cid):

    postList = Post.objects.filter(category_id=cid)
    # Post.objects.filter(category__id=cid)

    return render(request,'article.html',{'postList':postList})

#根据发帖时间查询所有帖子
def queryPostByCreated(request,year,month):

    postList = Post.objects.filter(created__year=year,created__month=month)
    return render(request,'article.html',{'postList':postList})