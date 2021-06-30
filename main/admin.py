from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	# fields = ["tutorial_title",
	# 		  "tutorial_published",
	#       	  "tutorial_content",]

	fieldsets = [
	("Title/Date" , {"fields" : ["tutorial_title" , "tutorial_published"]}),
	("Content" , {"fields": [ "tutorial_content"]}),
	("URL" , {"fields": [ "tutorial_slug"]}),
	("Series" , {"fields": [ "tutorial_series"]}),
	]      	  


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
