# Django To-Do App 📝

A simple task management app built with Django. Users can add, edit, delete, and mark tasks as completed. Perfect for practicing Django basics!

## Features
✅ Add, edit, and delete tasks  
✅ Mark tasks as completed  
✅ User authentication (if added)  
✅ Simple and clean UI  

## Installation  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/mruna18/django_todo.git
   cd django_todo
   
2. Create and activate a virtual environment

  ```sh
  python -m venv myenv
  myenv\Scripts\activate
```
3. Install dependencies

```sh
pip install -r requirements.txt
```

4. Apply database migrations

```sh
python manage.py migrate
```

5. Run the development server

```sh
python manage.py runserver
```
Open your browser and go to http://127.0.0.1:8000/ 🚀

Folder Structure
```
django_todo/
│── myproject/        # Main Django project folder
│   ├── myapp/        # Django app for To-Do functionality
│   ├── templates/    # HTML templates
│   ├── static/       # CSS, JS, images
│   ├── db.sqlite3    # SQLite database (ignored in Git)
│   ├── manage.py     # Django management script
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
```

---
💡 **Happy coding!** If you have any suggestions or improvements, feel free to contribute. 🚀  
