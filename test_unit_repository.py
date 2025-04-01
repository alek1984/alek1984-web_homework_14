import unittest
from app.repository import notes

class TestRepositoryNotes(unittest.TestCase):

    def setUp(self):
        # Налаштування перед кожним тестом
        self.notes = notes

    def test_get_note(self):
        # Тест для функції get_note
        note = self.notes.get_note(1)
        self.assertIsNotNone(note)
        self.assertEqual(note['id'], 1)

    # Додайте інші тести для функцій репозиторію

if __name__ == '__main__':
    unittest.main()