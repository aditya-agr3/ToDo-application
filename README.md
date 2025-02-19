
# Todo Application - Flask RESTful API

## Project Overview
This project is a **Flask-based RESTful API** for managing Todo items. The API provides endpoints to create, retrieve, update, and delete Todo items while ensuring proper data validation and error handling.

## Features
- **CRUD Operations**:
  - Create a new Todo item
  - Retrieve all or a specific Todo item
  - Update an existing Todo item
  - Delete a Todo item
- **Data Persistence**: Uses SQLite as the database for storing todos.
- **Input Validation**: Ensures required fields are provided.
- **Logging**: Logs API interactions and errors.
- **RESTful Design**: Follows best practices for API development.
- **Frontend**: Simple HTML & CSS frontend that interacts with the backend.

## Technologies Used
- **Backend**: Flask, Flask-SQLAlchemy, Flask-Marshmallow
- **Database**: SQLite
- **Frontend**: HTML, CSS (Styled using an external stylesheet)
- **Version Control**: Git & GitHub

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed and `pip` for package management.

### Steps to Run the Project
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/todo-flask-api.git
   cd todo-flask-api
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask Server**
   ```sh
   python app.py
   ```
5. **Access the API**
   Open `http://127.0.0.1:5000/` in a browser or use Postman to test API endpoints.

## API Endpoints
| Method | Endpoint         | Description                      |
|--------|-----------------|----------------------------------|
| POST   | `/todo`         | Create a new Todo item          |
| GET    | `/todo`         | Retrieve all Todo items         |
| GET    | `/todo/<id>`    | Retrieve a specific Todo item   |
| PUT    | `/todo/<id>`    | Update a Todo item              |
| DELETE | `/todo/<id>`    | Delete a Todo item              |

## Example API Request (Create Todo)
```sh
curl -X POST http://127.0.0.1:5000/todo -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, Eggs, Bread"}'
```

## Frontend Integration
The frontend (HTML + CSS) interacts with this API using **Fetch API** for dynamic updates. The UI allows users to **add, view, and manage Todo items** seamlessly.

## Future Improvements
- Implement JWT-based authentication for user-based todo lists.
- Add a React or Vue.js frontend for a more interactive experience.
- Use PostgreSQL or MongoDB for better scalability.

## License
This project is open-source under the **MIT License**.

## Author
Developed by **Aditya Agrawal**.

