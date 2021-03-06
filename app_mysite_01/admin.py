from django.contrib import admin
from .models import Category,Tag,Post,Comment,AboutMe,AboutSite,FriendWeb,MessageBoard,webSettings

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_time','publish','status')
    list_filter = ('status','created_time','publish','author')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag,TagAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','reader_name','body','created_time','active')
    list_filter = ('active','created_time',)
    search_fields = ('reader_name','body')

admin.site.register(Comment,CommentAdmin)

class AboutSiteAdmin(admin.ModelAdmin):
    list_display = ('created_time','updated_time')

admin.site.register(AboutSite,AboutSiteAdmin)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('created_time','updated_time')

admin.site.register(AboutMe,AboutMeAdmin)

class FriendwebAdmin(admin.ModelAdmin):
    list_display = ('friend_web_name','web_address','created','active')
    list_filter = ('friend_web_name','web_address','active',)

admin.site.register(FriendWeb,FriendwebAdmin)

class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ('reader_name','body','created_time','active')
    list_filter = ('reader_name',)
    search_fields = ('reader_name','body')

admin.site.register(MessageBoard,MessageBoardAdmin)

class WebSettingsAdmin(admin.ModelAdmin):
    list_display = ('web_name','web_footer_body','active')

admin.site.register(webSettings,WebSettingsAdmin)
