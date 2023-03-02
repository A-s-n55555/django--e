from django.shortcuts import render,get_list_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from clone1.models import Post,Comment
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  #in class based view
from django.contrib.auth.decorators import login_required   #in fun. based view
from clone1.forms import PostForm,CommentForm
# Create your views here.

class AboutView(TemplateView):
    template_name ='clone1/about.html'

class PostListView(ListView):
    model = Post
    template_name = 'clone1/post_list.html'
    context_object_name = 'posts'


    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    

class PostDetailView(DetailView):
    model =Post
    template_name='clone1/post_list.html'
    context_object_name = 'post'


# class CreatePostView(LoginRequiredMixin,CreateView):
#     login_url='/login/'
#     redirect_field_name='post_detail.html'
#     form_class=PostForm

#     model =Post



class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'clone1/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.publish()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})



class PostUpdateView(LoginRequiredMixin,UpdateView):
    # login_url='/login/'
    # redirect_field_name='clone1/post_detail.html'
    # form_class=PostForm

    model = Post
    
    form_class=PostForm
    success_url = reverse_lazy('post_detail')

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model =Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='clone1/post_list.html'

    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
   

#################################################
##################################################
@login_required
def post_publish(request,pk):
    post = get_list_or_404(Post,pk)
    post.publish
    return redirect('post_detail',pk=post.pk)


@login_required
def add_comment_to_post(request,pk):
    post =get_list_or_404(Post,pk=pk)
    if request.method =='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
        else:
            form=CommentForm()
        return render(request,'clone1/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_list_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment =get_list_or_404(comment,pk)
    post_pk =comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

