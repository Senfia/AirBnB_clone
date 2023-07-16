#!/usr/bin/python3
"""
Tests console's functionality
"""
import sys
import unittest
import inspect
import io
import pycodestyle
from contextlib import redirect_stdout
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    class for testing HBNBCommand
    """

    @classmethod
    def setUpClass(cls):
        """
        Class method for the doc tests
        """
        cls.setup = inspect.getmembers(HBNBCommand, inspect.isfunction)

    def test_pycodestyle_HBNBCommand(self):
        """
        checks conformity with pycodestyle
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_test_HBNBCommand(self):
        """
        checks conformity with pycodestyle
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests module docstring documentation
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests class docstring documentation
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)