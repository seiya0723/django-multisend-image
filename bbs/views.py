from django.shortcuts import render,redirect

from django.views import View

from .models import Topic
from .forms import TopicForm,TopicImageForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["topics"]   = Topic.objects.order_by("-dt")

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if not form.is_valid():
            return redirect("bbs:index")

        topic       = form.save()

        # name属性contentを複数個取り出すため、request.FILES.getlist() を使う。
        contents    = request.FILES.getlist("content")

        print(contents)

        for content in contents:
            dic             = {}
            dic["topic"]    = topic
            dic["content"]  = str(content)

            file_dic            = {}
            file_dic["content"] = content
            
            # request.POST と request.FILES を作る。
            form    = TopicImageForm(dic, file_dic)

            if form.is_valid():
                form.save()
            else:
                print(form.errors)

        return redirect("bbs:index")

index   = IndexView.as_view()
