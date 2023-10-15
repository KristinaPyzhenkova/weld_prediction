import joblib
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'mysecretkey'

best_model_v1 = joblib.load('best_model_v1.pkl')


class WeldForm(FlaskForm):
    IW = DecimalField('IW', validators=[InputRequired()])
    IF = DecimalField('IF', validators=[InputRequired()])
    VW = DecimalField('VW', validators=[InputRequired()])
    FP = DecimalField('FP', validators=[InputRequired()])
    submit = SubmitField('Рассчитать')


@app.route('/', methods=['POST', 'GET'])
def calculate_weld_parameters():
    form = WeldForm()
    if form.validate_on_submit():
        IW = form.IW.data
        IF = form.IF.data
        VW = form.VW.data
        FP = form.FP.data

        # Выполняем вычисления для глубины шва и ширины шва
        predicted_results = best_model_v1.predict([[IW, IF, VW, FP]])
        depth = round(predicted_results[0][0], 2)
        width = round(predicted_results[0][1], 2)

        flash(f'Глубина шва: {depth}\nШирина шва: {width}')
    return render_template('weld_form.html', form=form)
