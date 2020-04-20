# apps.py
from django.apps import AppConfig


class Model Name Config(AppConfig):
    name = '#'
    verbose_name = '# ' # Representation in admin panel



# admin.py for exact app
from django.contrib import admin

from .models import # Model Name

list_display = [field.name for field in Class._meta.fields]

# Отображает все поля таблицы Class в админке
+
fields = ['#'] # Выводит все поля по таким названиям


	list_filter = ['# поле-критерий для фильтра'] 
	search_fields = ['# поля, по которым будем искать']

admin.site.register('# Model Name') # Models to represent on admin panel



# views.py for exact app
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import # Model Name

def View Name (request,):
	?latest_articles_list? = Model Name.objects.order_by('Field Name')[:5]
	# Var					 Value is imported from 'Model' and ordered by ('this Field') [:criteria]
    return render(request, 'path/to.html', {'latest_articles_list' : latest_articles_list})
    # Rendering correct html by path		with mapping {'this template variable' : to view`s object }

        	a = get_object_or_404(Model Name, attribute = Field Name) # Var is taken from 'Model' by value of 'attribute' given from Model`s Field
			# If object`s not found - raising an error

	    ?latest_comments_list? = a.comment_set.order_by('-id',) [:10]
	    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

	    	session_key = request.session.session_key
			if not session_key:
				request.session.cycle_key() # creating a session key for unauthorized user

			print(request.session.session_key)



# models.py for exact app
class Model Name (models.Model):
	Field Name = models. Type Field ('# placeholder', attributes = ...) # Definition of fields in models
	Field Name = models.ForeignKey(Connected Model`s Name, on_delete = models.CASCADE) '''Construction which connects two models 
	with deleting related 'Field' in 'Connected Model`s Name' in case deleting 'Field' '''

	def __str__(self):
	        return self. Field Name # Displays a model by definite Field

	        class Meta:
	        verbose_name = '#'
	        verbose_name_plural = '#s' # Metaclass which displays singular and plural names for model in admin panel



# urls.py for exact app
from django.urls import path
from . import views

app_name = '#  app name'
urlpatterns = [
    path('', views.index, name = 'index'), # Main page view
    path('<int:article_id>/View Name(or anything else)/', views.View Name, name = 'View Name'),
    	 #<int:?article?_id> - takes an id from the exact field
]

