from flask import *
import sqlite3

app = Flask(__name__)

#User name and password for Admin Login
database={'jeeva':'123'}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin_login')
def admin_login():
    return render_template("admin_login.html")


@app.route('/form_login',methods=['POST','GET'])
def login():
    user_name=request.form['username']
    password=request.form['password']
    if user_name not in database:
	    return render_template('admin_login.html',info='Invalid User')
    else:
        if database[user_name]!=password:
            return render_template('admin_login.html',info='Invalid Password')
        else:
	         return render_template('admin_page.html')


@app.route('/admin_page')
def admin_page():
    return render_template("admin_page.html")


@app.route("/add_employee")
def add_employee():
    return render_template("add_employee.html")


@app.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            gender = request.form["gender"]
            contact = request.form["contact"]
            dob = request.form["dob"]
            year = request.form["year"]
            salary = request.form["salary"]
            dept = request.form["dept"]
            address = request.form["address"]
            with sqlite3.connect("employee_detials.db") as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT into Employee_Info (name, email, gender, contact, dob, year, salary, dept, address) values (?,?,?,?,?,?,?,?,?)",(name, email, gender, contact, dob, year, salary, dept, address))
                connection.commit()
                msg = "Employee detials successfully Added"
        except:
            connection.rollback()
            msg = "We can not add Employee detials to the database"
        finally:
            return render_template("success_record.html",msg = msg)
            connection.close()


@app.route("/delete_employee")
def delete_employee():
    return render_template("delete_employee.html")


@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("employee_detials.db") as connection:
        cursor = connection.cursor()
        cursor.execute("select * from Employee_Info where id=?", (id,))
        rows = cursor.fetchall()
        if not rows == []:
            cursor.execute("delete from Employee_Info where id = ?",(id,))
            msg = "Employee detial successfully deleted"
            return render_template("delete_record.html", msg=msg)
        else:
            msg = "can't be deleted"
            return render_template("delete_record.html", msg=msg)


@app.route("/employee_info")
def employee_info():
    connection = sqlite3.connect("employee_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Employee_Info")
    rows = cursor.fetchall()
    return render_template("employee_detials.html",rows = rows)


@app.route("/admin_search")
def admin_search():
    return render_template("admin_search.html")


@app.route("/search_by_id")
def search_by_id():
    return render_template("search_by_id.html")


@app.route("/search_by_name")
def search_by_name():
    return render_template("search_by_name.html")


@app.route("/search",methods = ["POST"])
def search():
    name = request.form["name"]
    connection = sqlite3.connect("employee_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Employee_Info where name=?",(name,))
    rows = cursor.fetchall()
    if not rows == []:
        return render_template("employee_detials.html", rows=rows)
    else:
        msg = 'Invalid User Name'
        return render_template("search_record.html",msg = msg)


@app.route("/search_id",methods=['POST','GET'])
def search_id():
    id = request.form["id"]
    connection = sqlite3.connect("employee_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Employee_Info where id=?",(id,))
    rows = cursor.fetchall()
    if not rows == []:
        return render_template("employee_detials.html", rows=rows)
    else:
        msg = 'Invalid User ID'
        return render_template("search_record.html",msg = msg)


@app.route('/user_login')
def user_login():
    return render_template("user_login.html")


# The Employees who are all entered in the Employee Management System, there name will be the Username and there Employee id will be the Password for User Login.
@app.route("/userform_login",methods=['POST','GET'])
def userfrom_login():
    name = request.form["username"]
    pwd = request.form["password"]
    connection = sqlite3.connect("employee_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Employee_Info where name in (?) and id in (?)",(name,pwd))
    rows = cursor.fetchall()
    if not rows == []:
        return render_template("useremployee_detials.html", rows=rows)
    else:
        msg = 'Invalid User'
        return render_template("usersearch_record.html",msg = msg)




if __name__ == '__main__':
    app.run(debug = True)
