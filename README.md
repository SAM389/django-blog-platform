# Django Blog Application

A feature-rich blogging platform built with Django 5.0, featuring user authentication, social interactions, and content management.

## Features

- 📝 **Post Management**: Create, read, update, and delete blog posts
- 👤 **User Authentication**: Complete registration, login, and password reset functionality
- 💬 **Comments System**: Interactive commenting on blog posts
- ❤️ **Social Features**: Like and bookmark posts
- 🏷️ **Categories**: Organize posts by Science, History, Entertainment, and Sports
- 🖼️ **Image Upload**: Support for post images and user profile pictures
- 📄 **Pagination**: Efficient content browsing with 6 posts per page
- 👥 **User Profiles**: Customizable user profiles with image upload
- 🔍 **Filtering**: View posts by category or author

## Tech Stack

- **Backend**: Django 5.0.7
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4
- **Forms**: Django Crispy Forms with Bootstrap 4
- **Image Processing**: Pillow

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAM389/django-blog-platform.git
   cd django-blog-platform
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your own:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     EMAIL_HOST_USER=your-email@gmail.com
     EMAIL_HOST_PASSWORD=your-app-password
     ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
django_1stP/
├── blog/              # Main blog application
├── users/             # User authentication and profiles
├── django_1stP/       # Project settings
├── media/             # User uploaded files
├── static/            # Static files (CSS, JS, images)
└── manage.py          # Django management script
```

## Configuration

### Email Setup (Gmail)
To enable password reset functionality:
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password
3. Add credentials to `.env` file

## Usage

- **Create Posts**: Login and click "New Post"
- **Browse Categories**: Filter posts by category from the sidebar
- **Interact**: Like, bookmark, and comment on posts
- **Profile**: Customize your profile with a profile picture


## Future Enhancements

- [ ] Add search functionality
- [ ] Implement tags system
- [ ] Add rich text editor for posts
- [ ] Email notifications for comments

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
