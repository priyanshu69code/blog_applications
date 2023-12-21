# Django Blog Project

## Project Overview

This Django project is a simple blog application that allows users to create, edit, and delete blog posts. It includes user authentication, allowing users to sign up, log in, and log out. Each blog post has a title, content (with rich text support using CKEditor), creation time, and author information.

## Project Structure

The project consists of the following components:

- **Models:**

  - `Blog`: Represents a blog post with fields for title, body, creation time, author, and a unique identifier (`blog_id`).

- **Forms:**

  - `BlogForm`: A form for creating and editing blog posts.

- **Views:**

  - `home`: Displays the 10 most recent blog posts on the home page.
  - `login_view`: Handles user login.
  - `signup`: Handles user registration.
  - `logout_user`: Logs out the user.
  - `create_blog`: Allows logged-in users to create new blog posts.
  - `view_blog_post`: Displays a single blog post.
  - `user_posts`: Displays all blog posts created by the logged-in user.
  - `delete_post`: Deletes a blog post (only allowed by the author).
  - `edit_post`: Edits a blog post (only allowed by the author).

- **Templates:**
  - `home.html`: Home page template showing recent blog posts.
  - `login.html`: Login page template.
  - `signup.html`: User registration page template.
  - `create.html`: Blog creation page template.
  - `readblog.html`: Template for displaying a single blog post.
  - `user_posts.html`: Template for displaying all blog posts by the logged-in user.
  - `edit_post.html`: Template for editing a blog post.

## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/django-blog-project.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd django-blog-project
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Admin):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the Admin Panel:**

   - Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
   - Log in with the admin credentials created in step 7.
   - user : admin
   - password : admin@54321

10. **Explore the Blog App:**
    - Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the home page.
    - Use the navigation links to log in, sign up, create blog posts, and manage your posts.

## Notes

- Ensure that CKEditor is properly configured in your Django project. Follow the CKEditor documentation for integration instructions.

- This project uses the default SQLite database. For production, consider using a more robust database like PostgreSQL.

- Customize the project based on your requirements and add additional features as needed.

Feel free to contribute, report issues, or provide feedback!
