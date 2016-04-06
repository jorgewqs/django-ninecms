#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":  # pragma: nocover
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings_test")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
