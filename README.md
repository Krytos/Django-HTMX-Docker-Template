# Django HTMX Showcase

A comprehensive demonstration of HTMX integration with Django, showcasing various interactive web techniques without writing JavaScript.

## Overview

This project demonstrates how to use [HTMX](https://htmx.org/) with Django to create modern, interactive web applications with minimal JavaScript. HTMX allows you to access AJAX, CSS Transitions, WebSockets, and Server Sent Events directly in HTML, using attributes, so you can build dynamic interfaces with the simplicity of Django's template system.

![HTMX Showcase Screenshot](https://imgur.com/BSyPwUl.png)

## Features

The showcase includes the following examples:

### 1. Click to Load
Load additional content when a button is clicked without refreshing the page.

![Click to Load Demo](https://i.imgur.com/aZJSpLS.png)

### 2. Form Submission
Submit forms and update the DOM with server responses, all without page refreshes.

![Form Submission Demo](https://i.imgur.com/mn5QEe9.png)

### 3. Infinite Scroll
Automatically load more content when the user scrolls to the bottom of the page.

![Infinite Scroll Demo](https://i.imgur.com/nMoTZ79.png)

### 4. Active Search
Filter and search through content as you type, with real-time results.

![Active Search Demo](https://i.imgur.com/tYp84Ju.png)

### 5. Table Sort
Sort table data by clicking on column headers, with backend processing.

![Table Sort Demo](https://i.imgur.com/FikiRbb.png)

### 6. Modal Dialog
Open modal dialogs with content loaded from the server.

![Modal Dialog Demo](https://i.imgur.com/UMfAPb0.png)
![Modal Dialog Demo](https://i.imgur.com/vUrJ6rY.png)

## Technologies Used

- [Django 5.0.6](https://www.djangoproject.com/) - Python web framework
- [HTMX 2.0.4](https://htmx.org/) - Modern browser features, directly in HTML
- [Bulma CSS](https://bulma.io/) - CSS framework for styling
- [Docker](https://www.docker.com/) - Containerization
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- [Faker](https://faker.readthedocs.io/) - Generating test data

## Installation

### Prerequisites

- Docker and Docker Compose
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Krytos/Django-HTMX-Docker-Template.git
   cd Django-HTMX-Docker-Template
   ```

2. Start the Docker containers:
   ```bash
   docker compose up app
   ```

3. The application will be available at [http://localhost:8000](http://localhost:8000)

## Development

### Running Tests
```bash
docker compose --profile test watch
```

### Project Structure

```
django-htmx-showcase/
├── app/
│   ├── htmx_project/          # Django project settings
│   ├── showcase/              # Main application with HTMX examples
│   │   ├── migrations/        # Database migrations
│   │   ├── templates/         # HTML templates (examples organized here)
│   │   │   ├── base.html      # Base template with common elements
│   │   │   ├── index.html     # Home page with links to all examples
│   │   │   ├── partials/      # Partial templates for HTMX responses
│   │   ├── admin.py           # Django admin configuration
│   │   ├── forms.py           # Forms for the application
│   │   ├── models.py          # Data models
│   │   ├── urls.py            # URL routing
│   │   └── views.py           # View functions for all examples
│   ├── manage.py              # Django management script
│   ├── populate_contacts.py   # Script to generate sample data
│   ├── Dockerfile             # Docker configuration for the app
│   └── pyproject.toml         # Python dependencies and project config
└── compose.yaml               # Docker Compose configuration
```

## Key Concepts

### How HTMX Works with Django

HTMX allows you to make AJAX requests directly from HTML attributes. When combined with Django's template system, this enables dynamic web applications with minimal JavaScript:

1. HTML elements use attributes like `hx-get`, `hx-post`, `hx-trigger`, etc.
2. HTMX intercepts these events and makes requests to your Django endpoints
3. Django views return HTML fragments (usually from partial templates)
4. HTMX updates the DOM with the returned HTML

### Example Pattern

A typical HTMX + Django pattern:

1. In your template:
   ```html
   <button hx-get="{% url 'load_more' %}" 
           hx-target="#content" 
           hx-swap="appendChild">
     Load More
   </button>
   <div id="content">
     <!-- Content goes here -->
   </div>
   ```

2. In your `urls.py`:
   ```python
   path('load-more/', views.load_more, name='load_more')
   ```

3. In your `views.py`:
   ```python
   def load_more(request):
       # Get some data
       return render(request, 'partials/more_content.html', {'data': data})
   ```

4. In your partial template (`partials/more_content.html`):
   ```html
   <div class="item">{{ data }}</div>
   ```


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [HTMX](https://htmx.org/) - For making interactive web interfaces simpler
- [Django](https://www.djangoproject.com/) - For the amazing web framework
- [Bulma](https://bulma.io/) - For the CSS framework