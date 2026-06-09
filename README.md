# AddressBook

A professional, modern contact management system built with Django. Organize your personal and professional contacts with ease.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Django](https://img.shields.io/badge/Django-6.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

✨ **Professional Contact Management**
- Manage unlimited contacts with detailed information
- Organize contacts by groups and relationships
- Mark favorites and filter by categories
- Add photos, notes, and custom fields
- Search and sort contacts instantly

🔐 **Secure User Authentication**
- User registration and login system
- Password-protected accounts
- Professional landing page for new users
- Session-based authentication

🎨 **Beautiful UI**
- Brown and white professional theme
- Responsive design (desktop & mobile)
- Intuitive sidebar navigation
- Real-time search functionality

📊 **Contact Organization**
- Categorize by relationships (Friend, Family, Colleague, etc.)
- Create custom groups
- Alphabetical grouping
- Multiple sorting options

## Tech Stack

- **Backend**: Django 6.0.5
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Image Handling**: Pillow

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/addressbook.git
cd addressbook
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Linux/macOS:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Apply database migrations**
```bash
python manage.py migrate
```

6. **Create a superuser (admin account)**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

The app will be available at **http://127.0.0.1:8000/**

## Usage

### Landing Page
- Visit the home page to register a new account or login
- Choose between tabbed Login and Register forms

### Dashboard
- After authentication, you're redirected to the contact dashboard
- Use the sidebar to navigate between different sections

### Adding Contacts
- Click "New Contact" or "✦ Add Contact" button
- Fill in contact details (name, email, phone, etc.)
- Upload a photo (optional)
- Save the contact

### Managing Groups
- Go to "Groups" in the sidebar
- Create custom groups to organize contacts
- Assign contacts to groups when creating/editing

### Searching & Filtering
- Use the search bar to find contacts by name, email, phone, or company
- Filter by relationship type (Friends, Family, Colleagues)
- Sort by name, recent, or company

### Logout
- Click the "Logout" button in the sidebar footer

## Project Structure

```
addressbook/
├── addressbook/          # Main Django project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── contacts/            # Main app
│   ├── models.py        # Contact and Group models
│   ├── views.py         # View logic
│   ├── forms.py         # Form definitions
│   ├── urls.py          # App URL patterns
│   ├── migrations/      # Database migrations
│   └── admin.py
├── templates/           # HTML templates
│   ├── landing.html     # Landing page
│   ├── registration/    # Auth templates
│   └── contacts/        # Contact templates
├── static/              # CSS, JS, images
│   ├── css/
│   │   └── style.css    # Main stylesheet (brown/white theme)
│   └── js/
├── media/               # User-uploaded files
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Database

The project uses **SQLite3** by default, which is file-based and requires no additional setup. The database file is `db.sqlite3`.

To reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## Admin Panel

Access the Django admin panel at **http://127.0.0.1:8000/admin/**

Use your superuser credentials to manage contacts and users directly.

## Theme & Customization

The color scheme uses a professional brown and white palette:
- **Primary Color**: Brown (#7a4f29)
- **Background**: White (#fffdfa)
- **Accent**: Dark Brown (#603e24)

Customize colors in `static/css/style.css` by modifying the CSS variables in the `:root` selector.

## API & Development

### Running migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a new app
```bash
python manage.py startapp myapp
```

### Collecting static files (for production)
```bash
python manage.py collectstatic
```

## Deployment

For production deployment, consider using:
- **Web Server**: Gunicorn or uWSGI
- **Reverse Proxy**: Nginx or Apache
- **Database**: PostgreSQL (instead of SQLite)
- **Hosting**: Heroku, AWS, DigitalOcean, or similar

See Django deployment documentation: https://docs.djangoproject.com/en/6.0/howto/deployment/

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please open a GitHub issue.

## Changelog

### v1.0.0 (2026-06-09)
- Initial release
- User authentication system
- Contact CRUD operations
- Group management
- Search and filtering
- Professional landing page
- Brown/white theme

---

**Made with ❤️ using Django**
