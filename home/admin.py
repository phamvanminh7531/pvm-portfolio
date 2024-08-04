from django.contrib import admin
from .models import AboutMeModel, TechUsedTagModel, ProjectModel, AchievementModel, HomeButtonModel

admin.site.register(AboutMeModel)
admin.site.register(TechUsedTagModel)
admin.site.register(AchievementModel)
admin.site.register(HomeButtonModel)

@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'demo_link')
    search_fields = ('title',)
    filter_horizontal = ('tech_used_tag',)
# @admin.register(AboutMeModel)
# class AboutMeModelAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request, obj=None):
#         return not AboutMeModel.objects.exists()