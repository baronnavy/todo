from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel, Post
from django.urls import reverse_lazy

import io
import matplotlib.pyplot as plt
import numpy as np

from django.db.models import Count
from django.db import connection

from django.db.models import Max
from itertools import chain

from django.http import JsonResponse
# Create your views here.
import json 
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

from .form import FloorForm
from django.views import generic


class CustomJSONEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%m月%d日 %H:%M:%S")
        return super().default(obj)


# class PostList(ListView):
    # template_name = 'list.html'
    # model = TodoModel


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
   #print(TodoModel.objects.all().query)

    queryset = TodoModel.objects.all()
    #queryset = TodoModel.raw("SELECT ee FROM title")
    #queryset = TodoModel.objects.all().order_by('-title').distinct().values('title','duedate')

    #queryset = TodoModel.objects.filter(title__in=[item['title'] for item in TodoModel.objects.values('title').annotate(Count('id')).order_by().filter(id__count__gt=1)])
    #queryset = TodoModel.objects.order_by("title").aggregate(count=Count("title", distinct=True)
    
    form_class = FloorForm
    success_url = reverse_lazy('list')

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     context = {
    #         'message': "POST method OK!!",
    #     }
    #     user_location = request.POST['abcd1']
    #     print(user_location)
    #     self.object = None
    #     self.object_list = self.get_queryset()
    #     form = self.get_form()

    
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    #     return render(request, 'list.html', context)

    def post(self, request, *args, **kwargs):
        Labe = request.POST.get('author')
        print(Labe)
        title_list = TodoModel.objects.order_by('-title').distinct().values_list('title', flat=False)
        aaa = list(title_list)

        context = {
            'author': Labe,
            'a':aaa,
        }
        return render(request, 'list.html', context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        max_ids = TodoModel.objects.values('title').annotate(Max('duedate')).values_list('duedate__max')
        #context['c'] = TodoModel.objects.values('title').annotate(Max('duedate'))#.values('duedate')
        context['bbb'] = TodoModel.objects.all()
        # print(bbb)
        #context['b'] = TodoModel.objects.values('title').annotate(latest_date=Max('duedate'))
        #max_ids = TodoModel.objects.values('title').annotate(latest_date=Max('duedate'))
        #context['a'] = TodoModel.objects.filter(duedate=max_ids)
        #.raw('SELECT DISTINCT title,id FROM todo_todomodel'):

        title_list = TodoModel.objects.order_by('title').distinct().values_list('title', flat=False)
        context['a'] = list(title_list)
        duedate_1 = TodoModel.objects.values('title').annotate(Max('duedate')).values_list('title','duedate__max')
        #duedate_2 = TodoModel.objects.values('title').annotate(Max('duedate')).values_list('title')
        context['b'] = duedate_1
        
        # for k,v in duedate_1:
        #     print('k='+k)
        #     print(v)


        id_list = TodoModel.objects.filter(title__in=title_list).values_list('id')
        context['aaa'] = id_list
        title_model = TodoModel.objects.filter(id__in=id_list)
        context['c'] = title_model
        # print(id_list)
        f=[]
        test_list=['bb','cc','ee','dd']
        for p in title_list:
            aa = list(TodoModel.objects.filter(title__in= test_list)[:1].values_list('id'))
            #f = f.append(aa)
            #print(aa)
        #context['aaa'] =f
        
        #context['c'] = TodoModel.objects.all().order_by('-title').filter(id__in = f)
        
        """
        for item in title_list:
            context['e'] = TodoModel.objects.order_by('-duedate').filter(title = 'ee')[:1]
            context['d'] = TodoModel.objects.order_by('-duedate').filter(title = 'ddd')[:1]
        """
        items = TodoModel.objects.all().values()
        json_str = json.dumps(list(items), ensure_ascii=False, indent=2, cls=CustomJSONEncoder) 
        context['qs_json'] = json_str
        return context

class TodoList2(ListView):
    template_name = 'list2.html'
    model = TodoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['x'] = TodoModel.objects.order_by('x').distinct().values_list('title','x', flat=False)
        context['title'] = TodoModel.objects.order_by('title').distinct().values_list('title','x', flat=False)
        items = TodoModel.objects.all().values()
        json_str = json.dumps(list(items), ensure_ascii=False, indent=2, cls=CustomJSONEncoder) 
        context['qs_json'] = json_str
        return context

    def post(self, request, *args, **kwargs):
        label = request.POST.get('label')
        article = request.POST.get('article')
        print(label)
        print(article)
        x = TodoModel.objects.order_by('x').distinct().values_list('title','x', flat=False)
        title = TodoModel.objects.order_by('title').distinct().values_list('title','x', flat=False)
        if article != "":
            item = TodoModel.objects.filter(title=article)
        else:
            item = TodoModel.objects.all

        items = TodoModel.objects.all().values()
        json_str = json.dumps(list(items), ensure_ascii=False, indent=2, cls=CustomJSONEncoder) 
        
        context = {
            'x': x,
            'title':title,
            'label':label,
            'article':article,
            'model_list':item,
            'qs_json' : json_str

        }
        return render(request, 'list2.html', context)

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
   
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    form_class = FloorForm
    success_url = reverse_lazy('list')
   

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


# グラフ作成
def setPlt(pk):
    
    # 折れ線グラフを出力
    # TODO: 本当はpkを基にしてモデルからデータを取得する。
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([20, 90, 50, 30, 100, 80, 10, 60, 40, 70])
    plt.plot(x, y)


# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


def get_svg(request,  pk):
    setPlt(pk)       # create the plot
    svg = pltToSvg() # convert plot to SVG
    plt.cla()        # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response