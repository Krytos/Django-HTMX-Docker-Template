from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Click to load
    path("click-to-load/", views.click_to_load, name="click_to_load"),
    path("load-more/", views.load_more_content, name="load_more_content"),
    # Form submission
    path("form-submit/", views.form_submit, name="form_submit"),
    path("submit-contact/", views.submit_contact_form, name="submit_contact_form"),
    # Infinite scroll
    path("infinite-scroll/", views.infinite_scroll, name="infinite_scroll"),
    path("load-more-contacts/", views.load_more_contacts, name="load_more_contacts"),
    # Active search
    path("active-search/", views.active_search, name="active_search"),
    path("search-contacts/", views.search_contacts, name="search_contacts"),
    # Table sort
    path("table-sort/", views.table_sort, name="table_sort"),
    path("sort-contacts/", views.sort_contacts, name="sort_contacts"),
    # Modal dialog
    path("modal/", views.modal, name="modal"),
    path(
        "contact-modal/<int:pk>/",
        views.contact_detail_modal,
        name="contact_detail_modal",
    ),
]
