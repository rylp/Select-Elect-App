from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Politician,State
from myproject.politicians.forms import AddForm

politician_blueprint = Blueprint('politicians',__name__,template_folder='templates/politicians')

@politician_blueprint.route('/add_politician',methods=['GET','POST'])
def add_politician():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        state_id=form.state_id.data

        get_state = State.query.get(state_id)
        state = get_state.name

        polit = Politician(name,state,state_id)

        db.session.add(polit)
        db.session.commit()

        return redirect(url_for('politicians.list_politicians'))

    return render_template('add_politician.html',form=form)


@politician_blueprint.route('/list_politicians')
def list_politicians():

    pol_list = Politician.query.all()
    return render_template('list_politicians.html',pol_list=pol_list)
