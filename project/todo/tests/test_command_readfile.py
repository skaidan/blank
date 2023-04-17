from io import StringIO
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
import pathlib


class ClosepollTest(TestCase):
    def test_missing_command_parameters(self):
        out = StringIO()
        with self.assertRaises(CommandError) as cm:
            call_command("readfile", stdout=out)

    def test_successfull_command_output(self):
        out = StringIO()
        call_command("readfile", './todo/test/data/sample.uff.txt', stdout=out)
        self.assertIn("Successfully read", out.getvalue())
    
    def test_file_not_found_command(self):
        out = StringIO()
        call_command("readfile", './todo/test/data/sample.uff.txt', stdout=out)
        self.assertIn("Successfully read", out.getvalue())
