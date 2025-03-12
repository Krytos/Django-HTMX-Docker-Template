from django.db import models


class Contact(models.Model):
    """
    Contact model for storing user contact information.
    Used in various HTMX examples throughout the application.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-created_at"]
