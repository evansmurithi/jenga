from django.test import TestCase
from model_mommy import mommy

from jenga.construction_site import models


class TestSupplier(TestCase):

    def test_str_representation(self):
        s = mommy.make(models.Supplier, name='ABC Supplier')
        assert str(s) == 'ABC Supplier'


class TestMaterial(TestCase):

    def test_str_representation(self):
        m = mommy.make(models.Material, name='Steel', unit_of_measurement='METRES')
        assert str(m) == 'Steel (METRES)'


class TestConstructionSite(TestCase):

    def test_str_representation(self):
        s = mommy.make(
            models.ConstructionSite, name='Site XYZ', location='Dagoretti')
        assert str(s) == 'Site XYZ at Dagoretti'
