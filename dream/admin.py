from django.contrib import admin
from dream.models import Preference, Agenda,Recruitment, CustomUser, Preference_people,Agenda_people,Recruitment_people,Preference_Tag,Agenda_Tag,Recruitment_Tag

admin.site.title = '管理画面'
admin.site.site_header = 'KUBB管理'
admin.site.index_title = 'メニュー'

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'is_staff', 'is_active', 'date_joined', 'icon_id')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'create_date')
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'create_date')
    
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'adress', 'create_date')
    
class Preference_peopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username')
    
class Agenda_peopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username')
    
class Recruitment_peopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username')
    
class Preference_TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
class Agenda_TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
class Recruitment_TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Preference, PreferenceAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(Preference_people, Preference_peopleAdmin)
admin.site.register(Agenda_people, Agenda_peopleAdmin)
admin.site.register(Recruitment_people, Recruitment_peopleAdmin)
admin.site.register(Preference_Tag, Preference_TagAdmin)
admin.site.register(Agenda_Tag, Agenda_TagAdmin)
admin.site.register(Recruitment_Tag, Recruitment_TagAdmin)