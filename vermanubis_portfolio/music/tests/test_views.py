import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import About
from ..serializers import AboutSerializer


# initialize the APIClient app
client = Client()
