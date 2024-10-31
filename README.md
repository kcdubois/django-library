# Library Reservation System

## Overview

The **Library Reservation System** is a web application built to manage a library’s core operations, including book
cataloging, user reservations, and administration of library resources. Built using **Django** for the backend and
**PostgreSQL** as the database, this application provides a comprehensive system for both users and administrators to
manage library interactions seamlessly.

## Features

### For Users:
- **User Registration and Login:** Sign up and log in securely to access library resources.
- **Profile Management:** Update personal information and manage account settings.
- **Book Catalog Browsing:** Search and filter through available books, categorized by genre and author.
- **Book Reservations:** Reserve books for future pickup with reservation tracking.
- **Notification Settings:** Set preferences for notifications, including reservation updates and reminders.

### For Admins:
- **User and Book Management:** View, add, edit, or remove users and books.
- **Author and Category Management:** Maintain lists of authors and book categories.
- **Reservation Management:** Approve, reject, and manage reservations, including overdue monitoring.
- **Inventory Management:** Oversee book inventory, including damaged or missing items.
- **Reports and Analytics:** Access various reports on user activity, popular books, overdue statistics, and more.
- **System Settings and Permissions:** Configure library-specific settings, control user roles, and access levels.

## Technologies

- **Backend:** Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript (Django templates)

## Entity Relationship Diagram (ERD)

The database structure is designed to support efficient management of users, books, reservations, and administrative
tasks. Below is the ERD for the database schema:

:::mermaid
flowchart TD
    USER[User] -->|Makes| RESERVATION[Reservation]
    RESERVATION -->|For| BOOK[Book]
    BOOK -->|Written by| AUTHOR[Author]
    BOOK -->|Belongs to| CATEGORY[Category]
    
    USER -->|Manages Profile| USER_PROFILE[Profile Management]
    BOOK -->|Listed in| BOOK_CATALOG[Catalog]
    BOOK -->|Managed by Admin| BOOK_MANAGEMENT[Book Management]
    RESERVATION -->|Managed by Admin| RESERVATION_MANAGEMENT[Reservation Management]
    BOOK -->|Managed by Admin| INVENTORY_MANAGEMENT[Inventory Management]

:::

## Contribution Guidelines

We welcome contributions to enhance the Library Reservation System. Please follow these steps:

### Fork the repository.

Create a new branch (feature/your-feature).
Make your changes.
Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For issues or feature requests, please create an issue on this repository or contact the project maintainer.