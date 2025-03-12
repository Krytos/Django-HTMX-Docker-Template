#!/usr/bin/env python
"""
Script to populate the database with random contacts.

This script creates a specified number of randomly generated contacts
using the Faker library and saves them to the database.
"""

import argparse
import os
import random
import sys
from datetime import timedelta

import django
from django.utils import timezone

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "htmx_project.settings")
django.setup()

from faker import Faker

from showcase.models import Contact


def create_contacts(count: int) -> None:
    """
    Create and save random contacts to the database.

    Parameters
    ----------
        count: Number of contacts to create

    Returns
    -------
        None

    """
    fake = Faker()

    # Popular cities for more realistic data
    cities = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
        "Dallas",
        "San Jose",
        "Austin",
        "Jacksonville",
        "Fort Worth",
        "Columbus",
        "San Francisco",
        "Charlotte",
        "Indianapolis",
        "Seattle",
        "Denver",
        "Washington DC",
        "Boston",
        "Nashville",
        "Portland",
        "Las Vegas",
        "Miami",
    ]

    # Create contacts with randomly distributed creation dates
    print(f"Creating {count} random contacts...")

    for i in range(count):
        # Create a contact with random data
        contact = Contact(
            name=fake.name(),
            email=fake.email(),
            city=random.choice(cities),
            # Set creation date between now and 30 days ago for more diverse data
            created_at=timezone.now()
            - timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59),
            ),
        )

        # Save the contact to the database
        contact.save()

        # Print progress every 10 contacts
        if (i + 1) % 10 == 0 or i == 0 or i == count - 1:
            print(f"Progress: {i + 1}/{count} contacts created")

    print("Done! Database populated with random contacts.")


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Populate database with random contacts"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=50,
        help="Number of contacts to create (default: 50)",
    )

    args = parser.parse_args()

    try:
        # Ensure count is positive
        if args.count <= 0:
            print("Error: Count must be a positive number")
            sys.exit(1)

        # Create the contacts
        create_contacts(args.count)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
