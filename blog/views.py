from django.shortcuts import render
from django.views.generic import DeleteView , UpdateView , CreateView
from .models import Blog
import random
from django.db.models import Max
from django.urls import reverse_lazy
from .forms import BlogForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#
# class BlogListView(ListView):
#     Blogobjects=Blog.objects.all()
#
#     IDs = []
#     for i in Blogobjects:
#         IDs.append(i.id)
#     random_ID=random.choice(IDs)
#     queryset = Blog.objects.get(id=random_ID)
#     print(queryset)
#     if queryset == queryset:
#         random_ID = random.choice(IDs)
#         queryset = Blog.objects.get(id=random_ID)
#
#     x=2
#     extra_context = {'IDs': random_ID,'x':x}
#     template_name = 'blog/home.html'

def BlogListView(request):
    userid = request.user.id
    max_id = Blog.objects.all().aggregate(max_id=Max("id"))['max_id']
    if max_id is not None:
        while True:
            pk = random.randint(1, max_id)
            blogobj = Blog.objects.filter(pk=pk, user__is_active=True).first()
            # print(Blog.objects.filter(is_active=True))
            if blogobj:
                return render(request, "blog/home.html", {"blogobj": blogobj, "userid": userid})
    else:
        blogobj= None

        return render(request, "blog/home.html", {"blogobj": blogobj, "userid": userid})





# class BlogDetailView(DetailView):
#     def get_object(self):
#         return self.request.user
#     myobjects=Blog.objects.all()
#     print(myobjects.filter(user_id=1))

def BlogDetailView(request, id):
    userid = request.user.id
    blogobj = Blog.objects.all()
    userblog=(blogobj.filter(user_id=id))
    return render(request,template_name = 'blog/myblogs.html',context={"blogs":userblog,"userid":userid})

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model=Blog
    template_name = 'blog/Deletemyblogs.html'
    success_url = reverse_lazy('home')

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    queryset = Blog.objects.all()
    form_class = BlogForm
    # fields = ['blog',
    #           'tags']
    template_name = 'blog/updatemyblogs.html'
    success_url = reverse_lazy('home')


class BlogCreateView(LoginRequiredMixin,CreateView):
    form_class = BlogForm
    template_name = 'blog/createview.html'
    success_url = reverse_lazy('home')
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'blog/signup.html'



