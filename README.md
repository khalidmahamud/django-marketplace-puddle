# Puddle - Django Marketplace

Puddle is a modern Django-based marketplace application that allows users to buy and sell items with built-in messaging functionality. It features a clean, responsive design using Tailwind CSS and provides a complete e-commerce experience with user authentication, item management, and real-time conversations.

## Features

### 🛍️ **Item Management**
- Browse items by category and search functionality
- Create, edit, and delete items
- Upload item images
- Mark items as sold
- View item details with related items

### 👥 **User Authentication**
- User registration and login
- Secure authentication system
- User-specific dashboards

### 💬 **Messaging System**
- Start conversations with item sellers
- Real-time messaging between buyers and sellers
- Conversation inbox for managing all chats
- Message history and timestamps

### 📊 **Dashboard**
- Personal dashboard for managing your items
- View all items you've created
- Quick access to item management

### 🎨 **Modern UI/UX**
- Responsive design with Tailwind CSS
- Clean and intuitive interface
- Mobile-friendly layout

## Project Structure

```
puddle/
├── core/                    # Core app (homepage, auth, base templates)
│   ├── templates/core/     # Base templates and core pages
│   ├── forms.py           # Authentication forms
│   └── views.py           # Homepage and auth views
├── item/                   # Item management app
│   ├── models.py          # Item and Category models
│   ├── views.py           # Item CRUD operations
│   ├── forms.py           # Item creation/editing forms
│   └── templates/item/    # Item-related templates
├── conversation/           # Messaging system
│   ├── models.py          # Conversation and Message models
│   ├── views.py           # Chat functionality
│   └── templates/conversation/ # Chat templates
├── dashboard/              # User dashboard
│   ├── views.py           # Dashboard views
│   └── templates/dashboard/ # Dashboard templates
├── media/                  # User uploaded files
│   └── item_images/       # Item images
└── puddle/                # Main project settings
    ├── settings.py        # Django settings
    └── urls.py           # URL configuration
```

## Models

### Item Model
- **Category**: Foreign key to Category model
- **Name**: Item name (max 255 characters)
- **Description**: Detailed item description
- **Price**: Item price (float)
- **Image**: Optional item image upload
- **is_sold**: Boolean flag for sold items
- **created_by**: Foreign key to User model
- **created_at**: Auto-generated timestamp

### Category Model
- **Name**: Category name (max 255 characters)

### Conversation Model
- **Item**: Foreign key to Item model
- **Members**: Many-to-many relationship with User model
- **created_at**: Conversation start time
- **modified_at**: Last message timestamp

### ConversationMessage Model
- **Conversation**: Foreign key to Conversation model
- **Content**: Message text
- **created_by**: Foreign key to User model
- **created_at**: Message timestamp

## Installation

### Prerequisites
- Python 3.8+
- Django 5.1.1
- SQLite3 (default database)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd puddle
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Buyers
1. **Browse Items**: Visit the homepage to see featured items
2. **Search & Filter**: Use the search bar and category filters on `/items/`
3. **View Details**: Click on any item to see full details
4. **Start Conversation**: Click "Contact seller" to message the seller
5. **Manage Chats**: Access your inbox at `/inbox/` to view all conversations

### For Sellers
1. **Sign Up/Login**: Create an account or log in
2. **Add Items**: Click "New item" to list items for sale
3. **Manage Items**: Use your dashboard at `/dashboard/` to manage your listings
4. **Respond to Messages**: Check your inbox for buyer inquiries
5. **Mark as Sold**: Edit items to mark them as sold when purchased

## URL Structure

- `/` - Homepage with featured items
- `/items/` - Browse all items with search and filters
- `/items/new/` - Create new item (login required)
- `/items/<id>/` - Item detail page
- `/items/<id>/edit/` - Edit item (owner only)
- `/items/<id>/delete/` - Delete item (owner only)
- `/dashboard/` - User dashboard (login required)
- `/inbox/` - Message inbox (login required)
- `/inbox/<id>/` - Conversation detail
- `/login/` - User login
- `/signup/` - User registration
- `/contact/` - Contact page

## Configuration

### Settings
The project uses Django's default settings with the following customizations:
- **Database**: SQLite3 (easily changeable to PostgreSQL/MySQL)
- **Media Files**: Configured for image uploads
- **Authentication**: Custom login/logout URLs
- **Debug**: Set to `True` for development

### Security Notes
⚠️ **Important**: This is a development setup. For production:
- Change the `SECRET_KEY` in `settings.py`
- Set `DEBUG = False`
- Configure proper database settings
- Set up static file serving
- Use environment variables for sensitive data

## Technologies Used

- **Backend**: Django 5.1.1
- **Database**: SQLite3
- **Frontend**: HTML, Tailwind CSS
- **Authentication**: Django's built-in auth system
- **File Uploads**: Django's ImageField
- **Template Engine**: Django Templates

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Happy selling and buying! 🛍️**
