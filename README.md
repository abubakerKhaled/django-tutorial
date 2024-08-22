# Django Tutorial Repository

## Overview

This repository is designed as a step-by-step guide for learning Django, with each branch focusing on specific functionalities. Each branch builds upon the previous one, adding more features and complexity to the project. This approach allows you to learn Django incrementally by focusing on individual aspects of Django development.

## Branches Overview

### 1. `main`

- **Description**: This branch contains the fundamental setup of a Django project.
- **Features**:
  - Initial Django project setup.
  - Basic settings configuration.
  - Creation of a simple Django application.
  - Overview of the project structure.

### 2. `add-template`

- **Description**: Adds template functionality to the project, enabling the rendering of HTML pages.
- **Features**:
  - Setup of Django templates.
  - Configuration of template directories.
  - Basic template inheritance and rendering.
  - Introduction to Django's template language.

### 3. `model-migrations`

- **Description**: Introduces Django models and the migration system for database management.
- **Features**:
  - Creation of Django models for the application.
  - Understanding and running migrations.
  - How to use Django's ORM to interact with the database.
  - Creating and manipulating database records.

### 4. `postgresql-setup`

- **Description**: Configures PostgreSQL as the database for the Django project.
- **Features**:
  - Installation and setup of PostgreSQL.
  - Configuration of Django settings to connect to a PostgreSQL database.
  - Running migrations on PostgreSQL.
  - Using PostgreSQL-specific features in Django.

### 5. `user-login-logout`

- **Description**: Implements user authentication with login and logout functionality.
- **Features**:
  - Setup of Django's built-in authentication system.
  - Creation of login and logout views.
  - Handling user sessions.
  - Customizing authentication templates.

### 6. `user-registration`

- **Description**: Adds user registration functionality to the project, allowing users to create accounts.
- **Features**:
  - Implementation of user registration forms.
  - Validation and saving of user data.
  - Sending confirmation emails (if configured).
  - Customization of the registration process.

### 7. `word-counter`

- **Description**: Implements a simple word counter tool as a Django application.
- **Features**:
  - Creation of a form to input text.
  - Logic to count words in the submitted text.
  - Displaying word count results to the user.
  - Integration with existing templates and views.

## How to Use This Repository

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/django-tutorial.git
   cd django-tutorial
   ```

2. **Switch Between Branches**:
   Each branch is designed to be checked out individually to explore the specific functionality it introduces. Use the following command to switch branches:
   ```bash
   git checkout branch-name
   ```
   Replace `branch-name` with the desired branch (e.g., `user-login-logout`).

3. **Run the Project**:
   - Ensure you have the necessary Python environment set up.
   - Apply migrations (if necessary):
     ```bash
     python manage.py migrate
     ```
   - Run the development server:
     ```bash
     python manage.py runserver
     ```

4. **Explore the Functionality**:
   After switching to a specific branch, explore the added functionality by following the README notes or comments within the code.

## Learning Path

To get the most out of this tutorial, it is recommended to follow the branches in the following order:

1. `main` – Start with the fundamentals.
2. `add-template` – Learn how to work with templates.
3. `model-migrations` – Understand models and migrations.
4. `postgresql-setup` – Set up and use PostgreSQL with Django.
5. `user-login-logout` – Implement user authentication.
6. `user-registration` – Add user registration functionality.
7. `word-counter` – Build a small Django application for practice.

## Contributing

Contributions are welcome! If you want to add more tutorials or improve the existing ones, feel free to fork the repository and submit a pull request.
