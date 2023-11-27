#Importar las dependencias necesarias para el funcianamiento del proyecto 
from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
from datetime import datetime


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./static/img"

#Configuracion para la base de datos(Nombre, puerto, usuario y contraseña)

app.config["SECRET_KEY"] = "clavesecreta"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "sapphireinventory"

mysql = MySQL(app)


#Rutas para ejecutar peticiójn HTTP, con los metodos que hacen dicha petición
@app.route("/", methods=["GET"])
def index():
    if "email" in session:
        return redirect(url_for("main"))
    else:
        return render_template("index.html")
    
    
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["pass"]
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE user_email = %s AND user_pass = %s",(email,password))
    user = cur.fetchone()
    cur.close()
    
    if user:
        session["email"] = email
        session["id"] = user[0]  
        session["name"] = user[1]
        session["lastName"] = user[2]
        session["userRol"] = user[7]
        userRol = session["userRol"]

        return redirect(url_for("main"))
    else:
        return render_template("index.html", message = "Credenciales incorrectas")

#Administrador
@app.route("/users")
def users():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()

        curUserList = mysql.connection.cursor()
        curUserList.execute("SELECT * FROM users")
        usersList = curUserList.fetchall()

        cur.close()
        curUserList.close()
        if session["userRol"] == 1:
            return render_template("admin/users.html", users= users[0], usersList = usersList)
        else:
            return redirect(url_for("main"))
    else:
        return render_template("index.html")


@app.route("/addUser", methods=["POST"])
def addUser():
    userName = request.form["nombreUsuario"]
    userLastName = request.form["apellidoUsuario"]
    userPhoneNumber = request.form["telefonoUsuario"]
    userEmail = request.form["correoUsuario"]
    userPass = request.form["contrasenaUsuario"]

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (user_name, user_lastName, user_phoneNumber, user_email, user_pass) VALUES (%s, %s, %s,%s, %s)", (userName, userLastName, userPhoneNumber,userEmail,userPass))

    mysql.connection.commit()
    cur.close()
    return redirect(url_for("users"))


@app.route("/deleteUser", methods=["POST"])
def deleteUser():
    userId = request.form["userId"]
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE user_id = %s", (userId,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("users"))


@app.route("/updateUser/<userId>")
def updateUser(userId):
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        
        curUsers = mysql.connection.cursor()
        curUsers.execute("SELECT * FROM users WHERE user_id = %s",(userId))
        usersData = curUsers.fetchall()
        return render_template("admin/updateUser.html", users= users[0],
                               usersData = usersData[0])
    else:
        return redirect(url_for("index"))
    
@app.route("/updateUserForm/<userId>", methods=["POST", "GET"])
def updateUserForm(userId):
    name = request.form["nombre"]
    lastName = request.form["apellido"]
    phone = request.form["telefono"]
    email = request.form["correo"]

    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET user_name = %s, user_lastName = %s, user_phoneNumber = %s, user_email = %s WHERE user_id = %s", (name,lastName,phone, email, userId))

    mysql.connection.commit()
    cur.close()
    return redirect(url_for("users"))


@app.route("/resetPassword")
def resetPassword():
    return render_template("resetPass.html")


@app.route("/main")
def main():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchone()
        
        curUserQty = mysql.connection.cursor()
        curUserQty.execute("SELECT COUNT(user_id) AS total FROM users")
        userQty = curUserQty.fetchall()
        
        curProductQty = mysql.connection.cursor()
        curProductQty.execute("SELECT COUNT(product_id) as total FROM products")
        productQty = curProductQty.fetchall()

        curCategoryQty = mysql.connection.cursor()
        curCategoryQty.execute("SELECT COUNT(category_id) as total FROM categories")
        categoryQty = curCategoryQty.fetchall()

        curEntries = mysql.connection.cursor()
        curEntries.execute("SELECT SUM(product_qty) as totalExistencias FROM products")
        entries = curEntries.fetchall()
        
        cur.close()
        curUserQty.close()
        curProductQty.close()
        curCategoryQty.close()
        curEntries.close()



        
        
        if session["userRol"] == 1:
            return render_template("admin/main.html", users= users,userQty = userQty[0], productQty = productQty[0], categoryQty = categoryQty[0], entries = entries[0])
        
        
        if session["userRol"] == 2:
            return render_template("emp/main.html", users= users,userQty = userQty[0], productQty = productQty[0], categoryQty = categoryQty[0],entries = entries[0])
        
    else:
        return redirect(url_for("index"))
    

@app.route("/usersPerfil")
def usersPerfil():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        cur.close()
        return render_template("admin/usersPerfil.html", users= users[0])
    else:
        return render_template("index.html")


@app.route("/insertarUserImg/<id>", methods=["POST"])
def insertarUserImg(id):
    img = request.files["img"]

    tiempo = datetime.now()
    horaActual = tiempo.strftime("%Y%H%M%S")
    if img.filename!="":
        nuevoNombre=horaActual+"_"+img.filename
        img.save(os.path.join(app.config["UPLOAD_FOLDER"], nuevoNombre))
    else:
        return redirect(url_for("usersPerfil"))
  
    cur = mysql.connection.cursor()
    cur.execute("""
           UPDATE users 
           SET user_img = %s
           WHERE user_id = %s
               """,(nuevoNombre,id))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("usersPerfil"))


@app.route("/mostrarImg/<id>")
def mostrarImg(id):
    return send_from_directory(os.path.join(app.config["UPLOAD_FOLDER"]), id)


@app.route("/categories")
def categories():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        curcategories = mysql.connection.cursor()
        curcategories.execute("SELECT * FROM categories")
        categories = curcategories.fetchall()
        cur.close()
        curcategories.close()

        if session["userRol"] == 1:
            return render_template("admin/categories.html", users= users[0], categories = categories)
        
        if session["userRol"] == 2:
            return render_template("emp/categories.html", users= users[0], categories = categories)
    else:
        return redirect(url_for("index"))
    
@app.route("/addCategory", methods=["POST"])
def addCategory():
    categoryName = request.form["nombreCategoria"]

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO categories (category_name) VALUES (%s)",(categoryName,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("categories"))
    

@app.route("/products")
def products():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()

        curProducts = mysql.connection.cursor()
        curProducts.execute("SELECT * FROM products")
        products = curProducts.fetchall()

        curCategories = mysql.connection.cursor()
        curCategories.execute("SELECT * FROM categories")
        categories = curCategories.fetchall()

        cur.close()
        curProducts.close()
        curCategories.close()

        if session["userRol"] == 1:
            return render_template("admin/products.html", users= users[0], products = products, categories = categories)
        
        if session["userRol"] == 2:
            return render_template("emp/products.html", users= users[0], products = products, categories = categories)
    else:
        return redirect(url_for("index"))
    
    
@app.route("/addProduct", methods=["POST"])
def addProduct():
    
    marca = request.form["marca"]
    nombreProducto = request.form["nombreProducto"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    categoria = request.form["categoria"]
    
    img = request.files["productImg"]
    tiempo = datetime.now()
    horaActual = tiempo.strftime("%Y%H%M%S")
    fechaReg = tiempo.strftime("%Y-%m-%d %I:%M:%S")
    
    if img.filename!="":
        nuevoNombre=horaActual+"_"+img.filename
        img.save(os.path.join(app.config["UPLOAD_FOLDER"], nuevoNombre))
    else:
        return redirect(url_for("products"))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products(product_mark,product_name,product_desc,product_qty,product_date,product_img,category_id_fk) VALUES(%s, %s,%s,%s,%s,%s,%s)",(marca,nombreProducto,descripcion,cantidad,fechaReg,nuevoNombre,categoria))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("products"))


@app.route("/deleteProduct", methods=["POST"])
def deleteProduct():
    productId = request.form["productId"]
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE product_id = %s",(productId))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("products"))


@app.route("/updateProduct/<productId>")
def updateProduct(productId):
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        
        curProducts = mysql.connection.cursor()
        curProducts.execute("SELECT * FROM products WHERE product_id = %s",(productId))
        products = curProducts.fetchall()


        return render_template("admin/updateProduct.html", users= users[0], products = products[0])
    else:
        return redirect(url_for("index"))
    

@app.route("/updateProduct/<productId>", methods=["POST","GET"])
def updateProductId(productId):
    updateMarca = request.form["updateMarca"]
    updateNombreProducto = request.form["updateNombreProducto"]
    updateDescripcion = request.form["updateDescripcion"]
    updateCantidad = request.form["updateCantidad"]
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET product_mark = %s, product_name = %s, product_desc = %s, product_qty = %s WHERE product_id = %s", (updateMarca,updateNombreProducto,updateDescripcion,updateCantidad,productId))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for("products"))


@app.route("/searchProduct")
def searchProduct():   
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        cur.close()
              
        if session["userRol"] == 1:
            return render_template("admin/searchProduct.html", users= users[0])
            
        if session["userRol"] == 2:
            return render_template("emp/searchProduct.html", users= users[0])
    else:
        return redirect(url_for("index"))


@app.route("/searchProductView", methods = ["POST"])
def searchProductView():

    email = session["email"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
    users = cur.fetchall()
    cur.close()

    product = request.form["buscar"]
    curProduct = mysql.connection.cursor()
    curProduct.execute("SELECT * FROM products WHERE product_id LIKE %s OR product_name LIKE %s", (product + "%", product + "%"))
    products = curProduct.fetchall()
    curProduct.close()

    return render_template("admin/searchView.html", users = users[0], products = products, mensaje = product.upper())


@app.route("/entries")
def entries():
    if "email" in session:
        email = session["email"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user_email = %s",[email])
        users = cur.fetchall()
        cur.close()

        curProducts = mysql.connection.cursor()
        curProducts.execute("SELECT * FROM products")
        products = curProducts.fetchall()
        curProducts.close()

        return render_template("admin/entries.html", users = users[0], products = products)
    else:
        return redirect(url_for("index"))

@app.route("/addEntry", methods=["POST"])
def addEntry():
    idproducto = request.form["producto"]
    cantidad = request.form["cantidad"]
    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET product_qty = product_qty + %s WHERE product_id = %s", (cantidad, idproducto))

    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for("entries"))




              













"""@app.route("/img/<imagen>")
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join("static/img"),imagen)
"""

@app.route("/logOut")
def logOut():
    session.clear()
    return redirect(url_for("index"))


#ejecutar la aplicación en un servidor local para pruebas, en este caso puerto 5000
if __name__ == "__main__":
    app.run(debug = True)