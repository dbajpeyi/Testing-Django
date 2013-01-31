from django.contrib import admin
from blogs.models import Blog, Category

#class BlogInline(admin.TabularInline):
#	model = Blog
#	extra = 2
	

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ['title']}
	fieldsets = [(None, {'fields':['title']}),('Date Information',{'fields':['posted']}),('Slug',{'fields':['slug'], 'classes' :['collapse']}),]

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ['title']}
#	inlines = [BlogInline]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
