from django.contrib import admin
from core.models import User, InviteTeam, TeamDetail, ActiveTeam, TeamMember, NewGame

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid','username','email','password','role')

@admin.register(TeamDetail)
class InviteTeamAdmin(admin.ModelAdmin):
    list_display = ('user','team_name','team_code')

@admin.register(InviteTeam)
class TeamDetailAdmin(admin.ModelAdmin):
    list_display = ('invite_by','invite_to','team')

@admin.register(ActiveTeam)
class ActiveTeamAdmin(admin.ModelAdmin):
    list_display = ('user','active_team')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user',"teamname","member")

@admin.register(NewGame)
class NewGameAdmin(admin.ModelAdmin):
    list_display = ('user','title','event','eventdate')