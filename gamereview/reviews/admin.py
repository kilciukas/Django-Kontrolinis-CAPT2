from django.contrib import admin

from .models import Publisher, Genre, Game, GameReview


class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'date_created', 'reviewer', 'content')
    list_editable = ('reviewer',)


admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(GameReview, GameReviewAdmin)