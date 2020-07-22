from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.states.forms import AddForm,DelForm
from myproject.models import State

state_blueprint=Blueprint('states',__name__,template_folder='templates/states')

@state_blueprint.route('/add',methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name=form.name.data

        new_state=State(name)

        db.session.add(new_state)
        db.session.commit()

        return redirect(url_for('states.list'))

    return render_template('add.html',form=form)

@state_blueprint.route('/delete',methods=['GET','POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data

        state=State.query.get(id)

        db.session.delete(state)
        db.session.commit()

        return redirect(url_for('states.list'))

    return render_template('delete.html',form=form)

@state_blueprint.route('/list')
def list():

    state_list = State.query.all()
    return render_template('list.html',state_list=state_list)
