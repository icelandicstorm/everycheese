import pytest

from ..models import Cheese
from .factories import CheeseFactory

# Connects our tests with our database
pytestmark = pytest.mark.django_db

def test__str__():
    """ cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
        firmness=Cheese.Firmness.SOFT,
    ) """
    """ cheese = CheeseFactory(name="Stracchino")
    
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
    """
    cheese = CheeseFactory()
    
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'


