from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import Contact


def index(request):
    """Render the index page with links to all HTMX showcases."""
    return render(request, "index.html")


# Click to load example
def click_to_load(request):
    """Render the click-to-load example page."""
    return render(request, "click_to_load.html")


def load_more_content(request):
    """Return additional content when requested via HTMX."""
    return render(request, "partials/more_content.html")


# Form submission example
def form_submit(request):
    """Render the form submission example page."""
    form = ContactForm()
    contacts = Contact.objects.all()[:5]  # Get the 5 most recent contacts
    return render(request, "form_submit.html", {"form": form, "contacts": contacts})


@require_http_methods(["POST"])
def submit_contact_form(request):
    """Handle form submission via HTMX."""
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        form = ContactForm()  # Reset the form
        contacts = Contact.objects.all()[:5]  # Get updated list
        return render(
            request, "partials/contact_list.html", {"contacts": contacts, "form": form}
        )
    return render(request, "partials/form_errors.html", {"form": form})


# Infinite scroll example
def infinite_scroll(request):
    """Render the infinite scroll example page."""
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)  # 5 contacts per page
    page_num = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "infinite_scroll.html", {"page_obj": page_obj})


def load_more_contacts(request):
    """Load more contacts for infinite scroll."""
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)  # 5 contacts per page
    page_num = request.GET.get("page", 2)  # Default to page 2 for additional loads
    page_obj = paginator.get_page(page_num)
    return render(request, "partials/contact_page.html", {"page_obj": page_obj})


# Active search example
def active_search(request):
    """Render the active search example page."""
    contacts = Contact.objects.all()
    return render(request, "active_search.html", {"contacts": contacts})


def search_contacts(request):
    """Search contacts based on query."""
    query = request.GET.get("query", "")
    contacts = (
        Contact.objects.filter(name__icontains=query)
        if query
        else Contact.objects.all()
    )
    return render(
        request, "partials/contact_search_results.html", {"contacts": contacts}
    )


# Table sort example
def table_sort(request):
    """Render the table sort example page."""
    sort_by = request.GET.get("sort", "name")
    if sort_by.startswith("-"):
        order_by = sort_by
    else:
        order_by = sort_by
    contacts = Contact.objects.all().order_by(order_by)
    return render(
        request, "table_sort.html", {"contacts": contacts, "sort_by": sort_by}
    )


def sort_contacts(request):
    """Return sorted contacts based on column."""
    current_sort = request.GET.get("current_sort", "name")
    sort_by = request.GET.get("sort", "name")

    if current_sort == sort_by:
        # Toggle sort direction
        sort_by = f"-{sort_by}" if not current_sort.startswith("-") else sort_by[1:]

    contacts = Contact.objects.all().order_by(sort_by)
    return render(
        request,
        "partials/sorted_contacts.html",
        {"contacts": contacts, "sort_by": sort_by},
    )


# Modal dialog example
def modal(request):
    """Render the modal dialog example page."""
    contacts = Contact.objects.all()
    return render(request, "modal.html", {"contacts": contacts})


def modal_close(request):
    """Close the modal dialog example page."""
    return render(request, "modal.html", {"contacts": []})


def contact_detail_modal(request, pk):
    """Return contact details in a modal dialog."""
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "partials/contact_modal.html", {"contact": contact})
