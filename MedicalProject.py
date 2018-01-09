from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators
from wtforms.fields.html5 import TelField,DateField, EmailField
import firebase_admin
from firebase_admin import credentials, db
from Bookings import Patient

cred = credentials.Certificate('./cred/medical-project-9a0e0-firebase-adminsdk-btoyv-e8a2534b31.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://medical-project-9a0e0.firebaseio.com/'
})

root = db.reference()

app = Flask(__name__)

@app.route('/')
def home1():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/t')
def temp():
    return render_template('template.html')

@app.route('/hospital_info')
def hospital_info():
    return render_template('hospital_info.html')

@app.route('/MedicalRecords')
def MedicalRecords():
    return render_template('Medical Records.html')

class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)



class AppointmentForm(Form):
    PatientName = StringField('Patient Name',[validators.DataRequired()])
    #SelectDate=StringField("Select Date",[validators.DataRequired()])
    PhoneNumber=TelField("Phone Number",[validators.DataRequired()])
    PreferedDoc = SelectField('Prefered Doctors',[validators.DataRequired()] , choices=[('NONE', 'None'), ('DR_TAN', 'Dr Tan'), ('DR_SIM', 'Dr Sim'),
                                                ('DR_LIM', 'Dr Lim'), ('DR_LEO', 'Dr Leo'), ('DR_BRIAN', 'Dr Brian')],
                           default='NONE')

    Email = EmailField('Email',[validators.DataRequired()])
    Symptoms=StringField('Symptoms')
    Date=StringField("Select Date (DD/MM/YYYY)",[validators.DataRequired()])
    Time = SelectField("Select Time", [validators.DataRequired()], choices=[('','Select Time'),('10AM',"10 AM"),('10.30AM','10.30 AM'),
                                                                            ('11AM',"11 AM"),('11.30AM','11.30 AM'),('12PM',"12 PM"),
                                                                            ('12.30PM','12.30 PM'),('1PM',"1 PM"),('1.30PM','1.30 PM'),
                                                                            ('2PM', "2 PM"), ('2.30PM', '2.30 PM'),('3PM','3 PM'),
                                                                            ('3.30PM','3.30 PM'),("4PM","4 PM")],default='')
    Gender=RadioField("Gender",[validators.DataRequired()], choices=[("MALE", "Male"),("FEMALE","Female")])

@app.route('/appointment', methods=['GET', 'POST'])
def new():
    form = AppointmentForm(request.form)
    if request.method == 'POST' and form.validate():
        PatientName=form.PatientName.data
        PhoneNumber=int(form.PhoneNumber.data)
        PreferedDoc=form.PreferedDoc.data
        Email=form.Email.data
        Symptoms=form.Symptoms.data
        Date=form.Date.data
        Time=form.Time.data
        Gender=form.Gender.data

        patient=Patient(PatientName,PhoneNumber,PreferedDoc,Email,Symptoms,Date,Time,Gender)
        patient_db=root.child("bookings")
        patient_db.push({
            "PatientName" : patient.get_PatientName(),
            "PhoneNumber" : patient.get_PhoneNumber(),
            "PreferedDoc" : patient.get_PreferedDoc(),
            "Email" : patient.get_Email(),
            "Symptoms" : patient.get_Symptoms(),
            "Date" : patient.get_Date(),
            "Time" : patient.get_Time(),
            "Gender" : patient.get_Gender()
        })


        return redirect(url_for('appsuccess'))


    return render_template('appointment.html', form=form)

@app.route('/appointmentfeedback', methods=['GET', 'POST'])
def appsuccess():
    return render_template('AppointmentFeedback.html')











































if __name__ == '__main__':
    app.run()
