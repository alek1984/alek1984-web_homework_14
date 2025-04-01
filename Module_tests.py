# tests/test_unit_repository.py
import unittest
from app.repository import notes

class TestRepositoryNotes(unittest.TestCase):

    def setUp(self):
        self.notes = notes

    def test_get_note(self):
        note = self.notes.get_note(1)
        self.assertIsNotNone(note)
        self.assertEqual(note['id'], 1)

    def test_get_note_not_found(self):
        note = self.notes.get_note(999)
        self.assertIsNone(note)

    def test_create_note(self):
        new_note = {"title": "Test Note", "content": "This is a test note"}
        created_note = self.notes.create_note(new_note)
        self.assertIsNotNone(created_note)
        self.assertEqual(created_note['title'], "Test Note")

    # Додайте тести для інших функцій репозиторію (update_note, delete_note, etc.)

if __name__ == '__main__':
    unittest.main()