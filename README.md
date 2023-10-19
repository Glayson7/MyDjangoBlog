# Blog API: A Django REST Framework Project

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Features](#features)
4. [Installation](#installation)
5. [API Endpoints](#api-endpoints)
6. [Usage Guide with Insomnia](#usage-guide-with-insomnia)
7. [Future Enhancements](#future-enhancements)
8. [Contributors](#contributors)
9. [License](#license)

---

## Introduction

Blog API is a robust and scalable API built on Django and the Django REST Framework. This API serves as the backend for a blog platform, providing a variety of features such as post creation, comments, likes, and advanced search functionalities. Built with best practices and optimized for performance, this project showcases a production-ready backend setup for a blog service.

## Technologies

- Python 3.x
- Django 3.x
- Django REST Framework
- SQLite

## Features

1. **Token-Based Authentication**: Secure and reliable user authentication.
2. **Post Management**: Complete CRUD operations for blog posts.
3. **Comment Management**: Add and delete comments on posts.
4. **Like Feature**: Users can like posts.
5. **Category Management**: List and manage post categories.
6. **Advanced Filtering**: Search posts by title, content, and author.
7. **Pagination**: Efficient pagination for post listing.
8. **Nested Data**: Retrieve comments and likes as nested data in posts.

## Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. **Clone the Repository**
   ```
   git clone https://github.com/Glayson7/MyDjangoBlog
   ```
2. **Navigate to the Directory**

   ```
   cd MyDjangoBlog
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```
   python manage.py migrate
   ```

5. **Start the Server**
   ```
   python manage.py runserver
   ```

## API Endpoints

| Endpoint                  | Description                    |
| ------------------------- | ------------------------------ |
| `POST /api/token/`        | User Authentication            |
| `POST /blog/create/`      | Create a new post              |
| `GET /blog/`              | List all posts                 |
| `GET /blog/post/:id`      | Get details of a specific post |
| `POST /blog/comment/:id/` | Add a comment to a post        |
| `POST /blog/like/:id/`    | Like a post                    |
| `GET /blog/categories/`   | List all categories            |

## Usage Guide with Insomnia

1. **Authentication**:

   - Method: POST
   - URL: `{{ base_url }}/api/token/`
   - Body: `{ "username": "your_username", "password": "your_password" }`

2. **Create Post**:

   - Method: POST
   - URL: `{{ base_url }}/blog/create/`
   - Body: `{ "title": "Post Title", "content": "Post Content", "categories": [1, 2] }`
   - Headers: `Authorization: Token YOUR_ACCESS_TOKEN`

3. **Advanced Post Filtering**:
   - Method: GET
   - URL: `{{ base_url }}/blog/?search=some_title&category=some_category_id&author__username=some_username`

Replace `{{ base_url }}` with your API's base URL.

## Future Enhancements

1. Unit and integration testing.
2. Frontend integration.
3. Additional features like "dislike", "share", etc.

## Contributors

- [Glayson Cardoso](https://github.com/glayson7)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Feel free to modify this README as needed for your portfolio.
