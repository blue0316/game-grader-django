from django.contrib import admin
from core.models import User, InviteTeam, TeamDetail, ActiveTeam, TeamMember, NewGame, NewPlan, Period

# admin.site.register(NewPlan)
# admin.site.register(Period)

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
    list_display = ('user','title','event','eventdate','get_sharewith')

    def get_sharewith(self,obj):
        return [sharewith.username for sharewith in obj.sharewith.all()]

@admin.register(NewPlan)
class NewPlanAdmin(admin.ModelAdmin):
    list_display = ('user','planname','plantype','scheduledate','scheduletime','notification','get_period')

    def get_period(self,obj):
        return [periods.periodname for periods in obj.periods.all()]

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('periodname','duration')