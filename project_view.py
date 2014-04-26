# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, render_template, url_for, session, escape, jsonify, g
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from flaskstarter import app
from models import User, Project,Task
import flask_sijax


@app.route('/project/<project_id>', methods=['POST', 'GET'])
def project(project_id):
    pro = Project.objects.get(pk=project_id)
    return render_template('project.html',project=pro)


@app.route('/tasks/<project_id>', methods=['POST', 'GET'])
def tasks_list(project_id):
    pro = Project.objects.get(pk=project_id)
    tasks = Task.objects(project=pro)
    return render_template('tasks/list.html',project=pro,tasks=tasks)


@app.route('/newtask/<project_id>', methods=['POST', 'GET'])
def new_task(project_id):
    pro = Project.objects.get(pk=project_id)
    if request.method == "POST":
        task = Task()
        task.title = request.form['title']
        task.project = pro
        task.description = request.form['description']
        task.save()
        return redirect(url_for('tasks_list',project_id=project_id))
    return render_template('tasks/new.html',project=pro)


@app.route('/users/<project_id>', methods=['POST', 'GET'])
def users(project_id):
    pro = Project.objects.get(pk=project_id)
    return render_template('users/index.html',project=pro)



