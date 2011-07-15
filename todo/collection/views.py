from collection import app
from collection.forms import TaskForm
from collection.documents import Task
from flask import g,request,flash,render_template, redirect, url_for
import datetime

@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        flash('Saved!')
        form.save()
        return redirect(url_for('list_tasks'))
    return render_template('/tasks/new.html', form=form)

@app.route('/')
@app.route('/tasks/')
@app.route('/tasks/<int:page>')
def list_tasks(page=1):
    title = u'Tasks list'
    pagination = Task.query.paginate(page=page, per_page=5)
    val=datetime.datetime.now()
    return render_template('/tasks/list_all.html', pagination=pagination, title=title,datetime=val)

@app.route('/help')
def help():
    return render_template('tasks/help.html')

@app.route('/about')
def help():
    return render_template('tasks/about.html')

@app.route('/tasks/delete/<id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    task.remove()
    return redirect(url_for('list_tasks'))

@app.route('/tasks/redo/<id>')
def redo(id):
    task = Task.query.get_or_404(id)
    task.remove()
    task.save()
    return redirect(url_for('list_tasks'))

@app.route('/tasks/edit/<id>')
def edit_task(id):
    task = Task.query.get(id)
    form = TaskForm(document=task)
    return render_template('/tasks/edit.html', form=form, task=task)

@app.route('/tasks/edit/<id>', methods=['POST'])
def update_task(id):
    task = Task.query.get(id)
    form = TaskForm()
    if form.validate_on_submit():
        form.instance = task
        form.save()
        return redirect(url_for('list_tasks'))
    form = TaskForm(document=task)
    return render_template('/tasks/edit.html', form=form, task=task)
