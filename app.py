from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)  # 0 = not completed, 1 = completed
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_completed = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There was an issue updating your task: {e}"
    else:
        return render_template('update.html', task=task)

# New route for toggling task completion
@app.route('/toggle/<int:id>', methods=['POST'])
def toggle_complete(id):
    task = Todo.query.get_or_404(id)
    try:
        if task.completed == 0:
            task.completed = 1
            task.date_completed = datetime.utcnow()
        else:
            task.completed = 0
            task.date_completed = None
        
        db.session.commit()
        return jsonify({
            'success': True, 
            'completed': task.completed,
            'date_completed': task.date_completed.strftime('%b %d, %Y') if task.date_completed else None
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Route for viewing completed tasks
@app.route('/completed')
def completed_tasks():
    completed_tasks = Todo.query.filter_by(completed=1).order_by(Todo.date_completed.desc()).all()
    return render_template('completed.html', tasks=completed_tasks)

# Route for clearing all tasks
@app.route('/clear-all', methods=['POST'])
def clear_all():
    try:
        Todo.query.delete()
        db.session.commit()
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
