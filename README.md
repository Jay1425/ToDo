# Flask To-Do List

A simple and efficient To-Do List web application built using Flask. This app allows users to manage their tasks by adding, updating, and deleting them.

## Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- User authentication (if implemented)
- Simple and clean UI

## Technologies Used
- Flask (Backend)
- SQLAlchemy (Database ORM)
- HTML, tailwind

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Jay1425/ToDo.git
   cd ToDo
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables (If Needed):**
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```
   The app will be running at `http://127.0.0.1:5000/`

## Usage
- Open your browser and go to `http://127.0.0.1:5000/`
- Add tasks to your list
- Mark tasks as completed or delete them when done

## Folder Structure
```
ToDo/
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── config.py
├── requirements.txt
└── run.py

```
## Contributing
Feel free to contribute by submitting a pull request or opening an issue!

## Contact
For any questions or feedback, reach out at [jayraychura13@gmail.com] or visit my [GitHub](https://github.com/Jay1425).
