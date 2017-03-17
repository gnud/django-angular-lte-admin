import json

from django.contrib.auth import get_user_model
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


def jwt_response_payload_handler(token, user=None, request=None):
    """
    :param request:
    :param token:
    :param user:

    # TODO: get user abilities
    """

    try:
        usr = UserSerializer(user, context={'request': request}).data
    except:
        usr = {}
    response_data = {"errors": False, "data": {
        # TODO: return avatar
        # "user": {"id": user.id, "name": user.get_short_name(), "email": user.get_username(), "avatar": None, "roles": []},
        "user": usr,
        "token": token,
        # TODO: list permissions
        "abilities": {"admin.super": ["manage.users", "manage.roles", "manage.permissions"],
                      "admin.user": ["manage.users"], "admin.role": ["manage.roles"],
                      "admin.permission": ["manage.permissions"]}, "userRole": []}}
    return response_data


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
    queryset = get_user_model().objects.all().order_by('-id')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
