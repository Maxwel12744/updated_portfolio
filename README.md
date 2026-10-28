# Updated Portfolio

A personal portfolio website built with **Django** and **MySQL**. It presents my profile, skills, projects and curriculum vitae, and lets visitors get in touch through a contact form. Content is managed from the Django admin, so no code changes are needed to add a project or update my CV.

> **Live site:** [add your deployed URL here once it is online]

## Table of contents

- [Features](#features)
- [Tech stack](#tech-stack)
- [Screenshots](#screenshots)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database setup (MySQL)](#database-setup-mysql)
  - [Environment variables](#environment-variables)
  - [Run the project](#run-the-project)
- [Using the admin](#using-the-admin)
- [Pages and URLs](#pages-and-urls)
- [Running tests](#running-tests)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features

- Multi-page site with a shared navbar: Home, About, Skills, Projects, Curriculum Vitae and Contact
- Skills grouped by category (backend, frontend, databases, tools)
- Projects with image, description, technologies, live link and source link
- Curriculum Vitae page with education, experience and a downloadable PDF
- Contact form that saves messages to the database
- Content managed through the Django admin
- Responsive layout styled with Tailwind CSS
- Secrets and database credentials kept in a `.env` file, outside version control

> Update this list to match what is actually built in your version of the project.

## Tech stack

| Layer           | Technology                                 |
| --------------- | ------------------------------------------ |
| Language        | Python 3.12 or newer                       |
| Framework       | Django 6.1                                 |
| Database        | MySQL 8 (through PyMySQL)                  |
| Front end       | HTML, Django templates, Tailwind CSS (CDN) |
| Configuration   | python-dotenv                              |
| Version control | Git and GitHub                             |

## Screenshots

Add screenshots to a `docs/screenshots/` folder and link them here:

```markdown
![Home page](docs/screenshots/home.png)
![Projects page](docs/screenshots/projects.png)
```

## Project structure

```
updated_portfolio/
├── .venv/                  # virtual environment (not committed)
├── .env                    # secrets and database credentials (not committed)
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── updated_portfolio/      # project configuration
│   ├── __init__.py         # registers PyMySQL as the MySQL driver
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── portfolio/              # the app
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── tests.py
    ├── migrations/
    ├── templates/portfolio/
    └── static/portfolio/
```

The folder names above match the project name `updated_portfolio` and the app name `portfolio`. Change them here if yours differ.

## Getting started

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.12 or newer
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) 8.0 or newer, running on your machine
- [Git](https://git-scm.com/downloads)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```

2. **Create and activate a virtual environment**

   Git Bash:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```

   PowerShell:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   macOS and Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   When it is active, `(.venv)` appears at the start of your prompt.

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` does not exist yet, install the packages and create it:

   ```bash
   pip install django pymysql cryptography python-dotenv Pillow
   pip freeze > requirements.txt
   ```

### Database setup (MySQL)

Log in to MySQL as an administrator and create a dedicated database and user. Do not connect Django as `root`.

```sql
CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'choose_a_strong_password';
GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';

-- Only needed to run `python manage.py test`, which creates a temporary test database:
GRANT ALL PRIVILEGES ON `test\_%`.* TO 'portfolio_user'@'localhost';

FLUSH PRIVILEGES;
```

### Environment variables

Create a file named `.env` in the project root, next to `manage.py`. **Never commit this file.**

```env
SECRET_KEY=change-me-to-a-long-random-string
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=choose_a_strong_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

| Variable        | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| `SECRET_KEY`    | Django's secret key. Use a long random value and keep it private. |
| `DEBUG`         | `True` for local development, `False` in production.              |
| `ALLOWED_HOSTS` | Comma-separated domains the site may be served from.              |
| `DB_NAME`       | MySQL database name.                                              |
| `DB_USER`       | MySQL user for this project.                                      |
| `DB_PASSWORD`   | Password for that user.                                           |
| `DB_HOST`       | Database host, normally `127.0.0.1`.                              |
| `DB_PORT`       | Database port, normally `3306`.                                   |

Generate a secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

### Run the project

Run these from the folder that contains `manage.py`, with the virtual environment active:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> in your browser. Stop the server with `Ctrl+C`.

## Using the admin

Open <http://127.0.0.1:8000/admin/> and log in with the superuser you created. Each project has its own admin and its own users, so accounts from other Django projects do not carry over.

From the admin you can:

- Add and edit skills, projects and CV entries
- Upload a new CV PDF
- Read messages sent through the contact form

## Pages and URLs

| Page             | URL          |
| ---------------- | ------------ |
| Home             | `/`          |
| About            | `/about/`    |
| Skills           | `/skills/`   |
| Projects         | `/projects/` |
| Curriculum Vitae | `/cv/`       |
| Contact          | `/contact/`  |
| Admin            | `/admin/`    |

## Running tests

```bash
python manage.py test
```

## Deployment

Before putting the site online:

1. Set `DEBUG=False` and a real `SECRET_KEY` in the server's environment.
2. Add your domain to `ALLOWED_HOSTS`.
3. Create a MySQL database and user on the host, set the `DB_*` variables, then run `python manage.py migrate` and `python manage.py createsuperuser`.
4. Run `python manage.py collectstatic` and configure the host to serve the `staticfiles/` folder (and `media/` for uploads).
5. Keep `.env` out of the repository and set the same values in the host's environment settings.

Hosts that run Django with MySQL include PythonAnywhere. Static-only hosts such as Netlify cannot run a Django app.

## Troubleshooting

| Problem                                           | Fix                                                                                             |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `No module named 'django'`                        | The virtual environment is not active. Activate it, then run `pip install -r requirements.txt`. |
| `No module named 'pymysql'`                       | Run `pip install pymysql` inside the active virtual environment.                                |
| `Access denied for user`                          | The username or password in `.env` does not match the MySQL user you created.                   |
| `Unknown database`                                | Create the database with the SQL in the setup section.                                          |
| `Can't connect to MySQL server`                   | Start the MySQL service.                                                                        |
| `can't open file 'manage.py'`                     | Change to the folder that contains `manage.py`.                                                 |
| `400 Bad Request` with `DEBUG=False`              | Add your domain to `ALLOWED_HOSTS`.                                                             |
| `source` or `ls -a` fails in the VS Code terminal | That terminal is PowerShell. Use the PowerShell activation command, or switch to Git Bash.      |

## Roadmap

- [ ] Build the Home, About, Skills, Projects, CV and Contact pages
- [ ] Add dark mode
- [ ] Add project detail pages
- [ ] Send an email notification for new contact messages
- [ ] Deploy and connect a custom domain

## Contributing

This is a personal project, but suggestions and bug reports are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a pull request

## License

This project is licensed under the MIT License. Add a `LICENSE` file to the repository with the license text, or replace this section with the license you prefer.

## Author

**[Your Name]**

- GitHub: [@your-username](https://github.com/Maxwel12744)
- LinkedIn: [your-profile](https://www.linkedin.com/in/maxwel-odhiambo-0a1852388/in/# Updated Portfolio

A personal portfolio website built with **Django** and **MySQL**. It presents my profile, skills, projects and curriculum vitae, and lets visitors get in touch through a contact form. Content is managed from the Django admin, so no code changes are needed to add a project or update my CV.

> **Live site:** [Odhiambo-Maxwel.vercel.app]

## Contributing

This is a personal project, but suggestions and bug reports are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a pull request

## License

This project is licensed under the MIT License. Add a `LICENSE` file to the repository with the license text, or replace this section with the license you prefer.

## Author

**[Maxwel Ochieng Odhiambo]**

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-profile](https://www.linkedin.com/in/www.linkedin.com/in/maxwel-odhiambo-0a1852388)
- Email: your.maxochieng07@gmail.com)
