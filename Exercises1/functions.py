from datetime import date

# 1. 💰 Calculadora de propina  

def calculate_tip(total=0,percentage=0):
     return total * (percentage / 100)
calculate_tip(100,15)
# 2. 📏 Conversor de unidades  

def meters_to_kilometers(meters=0):
    return meters / 1000
meters_to_kilometers(1500)
# 3. ✉️ Generador de email empresarial 

def create_email(name='',lastname='',email=''):
    
    valor = (name +"."+lastname+"@"+email).lower()
    return valor
    #print(valor)
    
create_email("lucia", "gomez", "empresa.com")

# 4. 🧾 Precio con impuestos  

def final_price(price=0,iva=0.21):
    return price + (price * iva)
final_price(100 , 0.10)
final_price(100)

# 5. 🔐 Simulador de login  

def validate_login(user='',password=''):
    
    if user == 'admin' and password == '1234':
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas") 
        return False
        
validate_login('admin','1234')
validate_login('user','wrohg')
# 6. 🧑‍💻 Generador de nombre de usuario  

def generate_username(name='',year=0):
    mod = year % 100
    return f"{name.lower()}{mod}"
(generate_username('Lucas',1997))
    
# 7. ✨ Formateador de nombres  

def format_name(fullName=''):
    return fullName.title()
format_name("juan perez")

# 8. 🎂 Calculadora de edad  

def calculate_age(birth=0):
    return date.today().year - birth
calculate_age(2000)

# 9. 📞 Validación de número telefónico  

def validate_phone(phone=0):
    
    cont = 0
    string= str(phone)
    
    for i in string:
        if i.isdigit():
            cont += 1   
    if cont == 10:
        return True
    else:
        return False
        
validate_phone(1234567890)
        
# 10. 🧠 Notas de estudiantes  

def student_average(name="",note1=0,note2=0,note3=0):
    averageNote = (note1 + note2 + note3) / 3 
    print(f"{name}: Promedio = {averageNote:.2f}")   
student_average("Ana",8,9,7)