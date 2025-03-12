import os
import sys


def populate_db():
    """Populates the database with initial data"""
    from populate_contacts import create_contacts
    from showcase.models import Contact

    if Contact.objects.all().values_list("created_at", flat=True).count() == 0:
        print("Populating database with initial data...")
        create_contacts(50)
    else:
        print("Database already populated")


def main():
    """Run administrative tasks."""
    populate_db()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "htmx_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
