from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
# views here.

#when home is called this renders correct template and passes params to it
def home(req):
	context={
		'posts':Post.objects.all()
	}
	return render(req,'blog/home.html',context)



#to view all posts
class PostListView(ListView):
	"""docstring for PostListView,to view all posts"""
	model = Post
	template_name ='blog/home.html'	
	context_object_name ='posts'
	ordering =['-date_posted']
	paginate_by = 4 #show 4 articles per page if more than 4 exist add scroll buttons(pagination)

#to view all posts by the a specific user when username clicked
class UserPostListView(ListView):
	"""docstring for PostListView,to view all posts by the a specific user when username clicked"""
	model = Post
	template_name ='blog/user_posts.html'	
	context_object_name ='posts'
	ordering =['-date_posted']
	paginate_by = 4

	def get_queryset(self):

		user=get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

#to view a single selected post
class PostDetailView(DetailView):
	"""docstring for PostDetailView,to view a single selected post"""
	model = Post

#pseudo Api call to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
	"""docstring for PostCreateView,pseudo Api call to create posts"""
	model = Post
	fields=['title','content','image','category']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#pseudo Api call to Update posts
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	"""docstring for PostUpdateView,pseudo Api call to Update posts"""
	model = Post
	fields=['title','content','image','category']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#pseudo Api call to delete posts 
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	"""docstring for PostDeleteView, pseudo Api call to delete posts"""
	model = Post
	success_url ="/"
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#when gallery is called this renders correct template and passes params to it
def gallery(req):
	context={
		'posts':Post.objects.all().order_by('-date_posted'),
		'title':'gallery',
	}
	return render(req,'blog/gallery.html',context)

#when info is called this renders correct template and passes params to it
def info(req):
	context ={
		'title':'INFO ABOUT BLOGAwesome',
		'author':'Ephraim Tlhako',
		'doc':'THIS SERVES AS DOCUMENTATION FOR THIS PROJECT',
		'technology':' created with [DJANGO, PYTHON, HTML, BOOTSTRAP, CSS]',
		'ref':'references used [DJANGO DOCS,STACKOVERFLOW,YOUTUBE,SLP]',
		
		'content':'''

			 THIS DOCUMENTATION IS NOT MEANT TO EXPLAIN THE CODE BEHIND THIS PROJECT , ONLY HOW TO USE THE PROJECT 
			 AND PROBLEMS YOU MAY COME ACROSS WHEN USING THE PROJECT

			 INTRODUCTION
			 
			 This blog was made with the simple intension to mimic an actual full funtional blog with CRUD 
			 capabilities. Initially the blog was a simple web app where only admin can add delete and update posts.
			 This was not ideal for the dream i had plus i really wanted to impress,so i went and did 
			 my research learned a bit more about django and its capabilities. Needless to say i fell inlove.

			 from learning how to create routes to learnig how to add pictures and create user specific content.
			 so after all that hardwork and sleepless nights and a some bragging to a few friends here is the incomplete version of the BLOGAWESOME.

			 I SINCERELY HOPE YOU FIND THIS TO YOUR LIKING. !!!!!!ENJOY!!!!!! 
			 ''',
		
	}
	return render(req,'blog/info.html',context)

#when technology is called this renders correct template and passes params to it
def technology(req):
	 context={'posts':Post.objects.filter(category="technology").order_by('-date_posted'),}
	 return render(req,'blog/category.html',context)


#when IOT is called this renders correct template and passes params to it
def IOT(req):
	 context={'posts':Post.objects.filter(category="IOT").order_by('-date_posted'),}
	 return render(req,'blog/category.html',context)


#when new_discoveries is called this renders correct template and passes params to it
def New_discoveries(req):
	 context={'posts':Post.objects.filter(category="New_discoveries").order_by('-date_posted'),}
	 return render(req,'blog/category.html',context)

#when unspecified is called this renders correct template and passes params to it
def Unspecified(req):
	 context={'posts':Post.objects.filter(category="Unspecified").order_by('-date_posted'),}
	 return render(req,'blog/category.html',context)

