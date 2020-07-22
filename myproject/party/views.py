from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.party.forms import AddForm
from myproject.models import Party

party_blueprint = Blueprint('parties',__name__,template_folder='templates/party')

@party_blueprint.route('/add_party',methods=['GET','POST'])
def add_party():

    form = AddForm()

    if form.validate_on_submit():

        state_id = form.state_id.data
        name=form.name.data

        new_party = Party(name,state_id)

        db.session.add(new_party)
        db.session.commit()

        return redirect(url_for('states.list'))

    return render_template("add_party.html",form=form)
