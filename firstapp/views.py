from django.shortcuts import render
from .models import TeamMember


def index(request):
    team_members = TeamMember.objects.all()  # Fetch all TeamMember objects
    context = {"team_members": team_members}
    return render(request, "index.html", context)
