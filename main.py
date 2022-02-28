import mysql.connector
import os

cnx = mysql.connector.connect(user="root", password="Darshan@45",
                              host="35.232.41.194",
                              database="doctors")
cursor = cnx.cursor()
# importing Flask and other modules
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/fv', methods=["GET", "POST"])
def addDoctor():
    if request.method == "POST":
        name = request.form.get("fullname")
        speciality = request.form.get("spec")
        location = request.form.get("loc")
        qualification = request.form.get("qual")
        hospital_name = request.form.get("hn")
        contact_number = request.form.get("cn")
        experience = request.form.get("exp")
        rating = request.form.get("rt")
        try:
            cursor.execute(
                "INSERT INTO doctors (name, speciality, location, qualification, hospital, contact, experience, rating) values ('" + name + "', '" + speciality + "', '" + location + "', '" + qualification + "', '" + hospital_name + "', '" + contact_number + "', '" + experience + "', '" + rating + "');")
            cnx.commit()
            print("Done success!")
        except:
            print("Error: Data not done;")
        return feed()
    return render_template("Sign up.html")

@app.route('/')
def feed():
    query = "select * from doctors ORDER BY rating DESC;"
    cursor.execute(query)

    id = []
    names = []
    spec = []
    locations = []
    qualification = []
    h_name = []
    contact = []
    experience = []
    rating = []
    for (doc_id, doc_name, doc_spec, doc_location, doc_qual, hosp_name, contact_num, doc_exp, doc_rat) in cursor:
        id.append(doc_id)
        names.append(doc_name)
        spec.append(doc_spec)
        locations.append(doc_location)
        qualification.append(doc_qual)
        h_name.append(hosp_name)
        contact.append(contact_num)
        experience.append(doc_exp)
        rating.append(doc_rat)

    aman = """
    <!DOCTYPE html>
<html lang="en">
<head>
<style>
h1{
  font-family:Helvetica Neue;
  height:45px;
  text-align:center;
  padding: 12px;
}

textarea {
  padding-left: 100px;
  font-size: large;
}
body {
  background-color: #ffffff
}

textarea{
  width: 20%;
  /*padding: 14px 20px;*/
  margin: 15px 0;
  border: none;
  border-radius: 4px;
}
div.lalala {
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  color: white;
  font-weight: bold;
  font-size:20px;
  font-family:Helvetica Neue;
  border: 3px solid #f1f1f1;
  z-index: 2;
  width: 70%;
  padding: 40px;
  float: left;
}
form {
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  color: white;
  font-weight: bold;
  border: 3px solid #f1f1f1;
  z-index: 2;
  width: 40%;
  padding: 40px;
  float: left;
}

.button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 4px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 12px;
}
</style>
    <center><h1 style="background-color:LightGrey;">Doctors Hub</h1></center>
    <p style="font-size: 20px; text-align: right; padding: 5px; padding-right: 40px; background-color:Silver;"><a href="/fv"><button class="button">BE A MEMBER</button></a></p>
</head>
<body>
<div>
  <div style="width: 100%">
    <img src='https://st.depositphotos.com/1028979/4049/i/600/depositphotos_40493159-stock-photo-doctor-working-with-healthcare-icons.jpg' style="float:right; padding-top: 55px; width="800" height="530">
  </div>
  <div >
    <p style="font-size: 20px; text-align: left; font-family:Helvetica Neue; padding: 5px;">TOP DOCTORS</p>
    
    <form> 
    """
    for i in range(len(names)):
        aman += "<div class= 'lalala'> Name:- " + names[i] + "</br> Speciality:- " + spec[i] + "</br> Rating:- " + str(rating[i]) + " out of 5</br>" + "</br>"
        aman += "<a style='color: white;' class='button' href='/invites?ev_name=" + names[i] + "'>View Profile</a>""</div>"
    aman += """
    </div>
    </form>
</div>
</body>
</html>
    """
    return aman


@app.route('/invites', methods=["GET", "POST"])
def invites():
    #if request.method == "POST":
    ev_name = request.args.get('ev_name')

    curr = "select * from doctors where name ='" + ev_name +"';"
    cursor.execute(curr)
    record = cursor.fetchone()
    curr_name = record[1]
    spec = record[2]

    people = "select * from doctors where speciality ='" + spec + "'AND name !='" + curr_name +"' ORDER BY rating DESC;"
    cursor.execute(people)

    p_id = []
    p_names = []
    p_spec = []
    p_locations = []
    p_qualification = []
    p_h_name = []
    p_contact = []
    p_experience = []
    p_rating = []
    for (doc_id, doc_name, doc_spec, doc_location, doc_qual, hosp_name, contact_num, doc_exp, doc_rat) in cursor:
        p_id.append(doc_id)
        p_names.append(doc_name)
        p_spec.append(doc_spec)
        p_locations.append(doc_location)
        p_qualification.append(doc_qual)
        p_h_name.append(hosp_name)
        p_contact.append(contact_num)
        p_experience.append(doc_exp)
        p_rating.append(doc_rat)

    jariwala = """
    <!DOCTYPE html>
<html lang="en">
<head>
<style>
h1{
  font-family:Helvetica Neue;
  height:45px;
  text-align:center;
  padding: 12px;
}
textarea {
  padding-left: 100px;
  font-size: large;
}
body {
  background-color: #ffffff
}

input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

textarea{
  width: 20%;
  /*padding: 14px 20px;*/
  margin: 15px 0;
  border: none;
  border-radius: 4px;
}
div.lalala {
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  color: white;
  font-weight: bold;
  font-size:20px;
  font-family:Helvetica Neue;
  border: 3px solid #f1f1f1;
  z-index: 2;
  width: 70%;
  padding: 40px;
  float: left;
}
form {
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  color: white;
  font-weight: bold;
  border: 3px solid #f1f1f1;
  z-index: 2;
  width: 40%;
  padding: 40px;
  float: left;
}

.button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 4px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 12px;
}
</style>
    <center><h1 style="background-color:LightGrey;">Doctors Hub</h1></center>
    <p style="font-size: 20px; text-align: right; padding: 5px; padding-right: 40px; background-color:Silver;"><a href="/"><button class="button">Homepage</button></a></p>
</head>
<body>
<div>
  <div style="width: 100%">
    <img src='https://st.depositphotos.com/1028979/4049/i/600/depositphotos_40493159-stock-photo-doctor-working-with-healthcare-icons.jpg' style="float:right; padding-top: 55px; width="800" height="530">
  </div>
  <div >
  <h1 >ABOUT THE DOCTOR</h1>
  """

    jariwala += "<p> Name:- " + record[1]+"</p>"
    jariwala += "<p> Speciality:- " + record[2] + "</p>"
    jariwala += "<p> Location:- " + record[3] + "</p>"
    jariwala += "<p> Qualification:- " + record[4] + "</p>"
    jariwala += "<p> Hospital's Name:- " + record[5] + "</p>"
    jariwala += "<p> Contact Number:- " + record[6] + "</p>"
    jariwala += "<p> Experience:- " + record[7] + "</p>"
    jariwala += "<p> Rating:- " + str(record[8]) + " out of 5</p>"


    jariwala += """
    <a>
    <p style="font-size: 20px; text-align: left; font-family:Helvetica Neue; padding: 5px;">SIMILAR DOCTORS</p>
    <form> 
    """
    for i in range(len(p_names)):
        jariwala += "<div class= 'lalala'> Name:- " + p_names[i] + "</br> Speciality:- " + p_spec[i] + "</br> Rating:- " + str(p_rating[i]) + " out of 5</br>" + "</br>"
        jariwala += "<a style='color: white;' class='button' href='/invites?ev_name=" + p_names[i] + "'>View Profile</a>""</div>"
    jariwala += """
    </div>
    </form>
</div>
</body>
</html>
    """
    return jariwala




app.run(debug=True)
cnx.commit()
cursor.close()
cnx.close()

