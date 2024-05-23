import unittest
from backend import Backend


class TestBackend(unittest.TestCase):

    def test_filter(self):
        backend = Backend(True)
        backend.add_book(["TestTitle", "TestAuthor", "TestGenre", 1000])
        backend.add_book(["Neville's Journal", "Neville", "Journal", 10])
        backend.add_book(["Blabook", "Tom", "Random", 504])
        backend.add_book(["Lalabok", "Tim", "Special", 6000])
        self.assertEqual(backend.filter_for("Title", "TestTitle").values.tolist()[0][0], "TestTitle")
        self.assertEqual(backend.filter_for("Author", "Tom").values.tolist()[0][0], "Blabook")
        self.assertEqual(len(backend.filter_for("Genre", "").values.tolist()),0)
        self.assertEqual(backend.filter_for("Pages", 10).values.tolist()[0][0], "Neville's Journal")




if __name__ == '__main__':
    unittest.main()
