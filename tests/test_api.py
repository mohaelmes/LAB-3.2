import unittest
from app import app, db, Item

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Inicializa el cliente de prueba y la base de datos
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        # Elimina la base de datos después de cada prueba
        db.session.remove()
        db.drop_all()

    def test_add_item(self):
        response = self.app.post('/items', json={'name': 'Item 1', 'description': 'Description of Item 1'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('name', response.get_json())

    def test_get_items(self):
        self.app.post('/items', json={'name': 'Item 1', 'description': 'Description of Item 1'})
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.get_json()), 0)
    
    def test_update_item(self):
        item = Item(name="Item 1", description="Description of Item 1")
        db.session.add(item)
        db.session.commit()
        response = self.app.put(f'/items/{item.id}', json={'name': 'Updated Item', 'description': 'Updated description'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated Item')

    def test_delete_item(self):
        item = Item(name="Item 1", description="Description of Item 1")
        db.session.add(item)
        db.session.commit()
        response = self.app.delete(f'/items/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Item deleted')

if __name__ == '__main__':
    unittest.main()
