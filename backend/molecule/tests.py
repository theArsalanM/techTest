from django.test import TestCase

from molecule.models import Molecule
from molecule.serializers import MoleculeSerializer


class TestMoleculeData(TestCase):
    def test_invalid_molecule_detail(self):
        resp = self.client.get('/api/molecule/1/')
        self.assertEqual(resp.status_code, 404)

    def test_valid_molecule_detail(self):
        resp = self.client.get('/api/molecule/97/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(MoleculeSerializer(instance=Molecule.objects.get(pk=97)).data, resp.data)

    def test_invalid_molecule_activity(self):
        resp = self.client.get('/api/molecule/1/activity/')
        self.assertEqual(resp.data['results'], [])
        self.assertEqual(resp.data['count'], 0)

    def test_valid_molecule_activity(self):
        resp = self.client.get('/api/molecule/97/activity/')
        self.assertEqual(resp.data['count'], 173)

    def test_molecule_list(self):
        resp = self.client.get('/api/molecule/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 3329)
