from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial
# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db # to give pytest access to the database
def test_create_tutoriall():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"

##We can update the previous code as a fixture to be used several times:

@pytest.fixture
def new_tutorial(db): #See: https://pytest-django.readthedocs.io/en/latest/helpers.html#db
    #The argument of db comes from pytest.fixture and helps it connect to the database
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django' ##title is a function under the new_tutorial returned object. You can verify this under the tutorials models
    new_tutorial.save() # same as above
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

##################################################################################

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk #pk is primary key from tutorial object(automatically generated)