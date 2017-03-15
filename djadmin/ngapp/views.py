import json

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from ngapp.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets



# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('ngapp/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def register(request):
    # TODO: hardcoded register response, need to be rewritten to use following:
    # django auth via ajax

    response_data = {
        "message": "OK",
        "status_code": "200"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def login(request):
    # TODO: hardcoded login response, need to be rewritten to use following:
    # - get user info
    # - get JWT-Auth token
    # - get user abilities
    response_data = {
        "errors": False, "data": {
            "user": {"id": 2, "name": "Damjan", "email": "gnu_d@freedom.local", "avatar": None, "email_verified": "1",
                     "email_verification_code": "715wUmo6EpY6Q30yv4ZXpv7mf6Hto2LxFfUFwCXI",
                     "created_at": "2016-12-17 16:07:08", "updated_at": "2016-12-17 16:07:08", "roles": []},
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImlzcyI6Imh0dHA6XC9cL2xvY2FsaG9zdDo4MDAxXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNDg5NTI5ODcxLCJleHAiOjE0ODk1NDc4NzEsIm5iZiI6MTQ4OTUyOTg3MSwianRpIjoiNTU2MDk5YmI0ZTI3YjNlMzc3Zjg3M2YzNTMwYjUxMTUifQ.KF-nJFg1TBuwLBpp5-nxn9CCQyPibSFsOKVL7swWtG4",
            "abilities": {"admin.super": ["manage.users", "manage.roles", "manage.permissions"],
                          "admin.user": ["manage.users"], "admin.role": ["manage.roles"],
                          "admin.permission": ["manage.permissions"]}, "userRole": []}
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def me(request):
    # TODO: hardcoded login response, need to be rewritten to use following:
    # - get user info
    response_data = {
        "errors": False,
        "data": {"id": 2, "name": "Damjan", "email": "gnu_d@freedom.local", "avatar": None, "email_verified": "1",
                 "email_verification_code": "715wUmo6EpY6Q30yv4ZXpv7mf6Hto2LxFfUFwCXI",
                 "created_at": "2016-12-17 16:07:08", "updated_at": "2016-12-17 16:07:08"}
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
