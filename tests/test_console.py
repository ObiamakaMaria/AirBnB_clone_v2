#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def main(cls):
        """setup for the test"""
        cls.handler = HBNBCommand()
    @classmethod
    def teardown(cls):
        """ this will tear it down the handler down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass
    def test_create(self):
        """Test create command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.handler.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.handler.onecmd("create users")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.handler.onecmd("create User email='me@gmail.com' "
                               "password='seebe3r'")
        with patch('sys.stdout', new=StringIO()) as f:
            self.handler.onecmd("all User")
            self.assertEqual("[[User]", f.getvalue()[:7])

