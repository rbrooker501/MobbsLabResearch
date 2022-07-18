#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
<<<<<<< HEAD
=======
import dotenv
import pathlib
>>>>>>> 84827d3358ad91919475e0991baa2ed4d4708826


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
=======
    DOT_ENV_PATH = pathlib.Path() / '.env'
    if DOT_ENV_PATH.exists():
        dotenv.load_dotenv(str(DOT_ENV_PATH))
    else:
        print("No .ev found, be sure to make it!")
>>>>>>> 84827d3358ad91919475e0991baa2ed4d4708826
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MobbsSite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()