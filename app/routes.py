from flask import Blueprint, request, redirect, render_template
from app import db
from app.models import ToDo

bp = Blueprint('todos', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'task' in request.form:
            task = request.form['task']
            new_todo = ToDo(task=task)
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')
        else:
            return "Error: No task provided!", 400

    todos = ToDo.query.all()
    return render_template('index.html', todos=todos)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = ToDo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')