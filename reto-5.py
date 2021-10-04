import sys
"""proyecto agenda"""

def add_contact(name_contact_book):
    answer_contact="si"
    print("\t\t........................................................................")
    print("\t \t Ingresaste a la opcion para crear un nuevo contacto")
    print("\t\t........................................................................")
    write_file=open(name_contact_book,"a")
    while answer_contact=="si" or answer_contact=="SI" or answer_contact=="Si":
        name_last_name=input("Ingrese el nombre y apellido del estudiante: ")
        personal_id=input("Ingrese el numero de cedula del estudiante: ")
        number_phone=input("Ingrese el numero de celular del estudiante: ")
        search_contact=open(name_contact_book,"r")
        list_contacts=[]
        list_contacts= [linea.rstrip() for linea in search_contact]
        contacts_count=list_contacts.count(personal_id)
        if  contacts_count==0:
            write_file.write(name_last_name +"\n")
            write_file.write(personal_id+"\n")
            write_file.write(number_phone+"\n")
            print("El estudiante a sido agregado....")
            answer_contact=input("desea agragar otro contacto si/no: ")
        else:
            print("...................................................................")
            print("El numero de cedula ingresado ya existe en la lista de contactos verifique el numero de cedula y vuelva a intentarlo.")
            print("...................................................................")

def search_contact(name_contact_book):
    try:
        print("\t\t........................................................................")
        print("\t \t Ingresaste a la opcion para buscar un contacto")
        print("\t\t........................................................................")
        search_contact=open(name_contact_book,"r")
        #read_contacts=search_contact.readlines()
        #print(read_contacts)
        list_contacts=[]
        list_contacts= [linea.rstrip() for linea in search_contact]
        name_contact=input("Ingrese el nombre y apellido del contacto que desea buscar: ")
        try:
            contact_index=list_contacts.index(name_contact)
            index_number_phone=contact_index+2
            print("**********************************************************")
            print(f"El numero de celular del estudiante {name_contact} es: ",list_contacts[index_number_phone])
        except:
            print("**********************************************************")
            print("El contacto que busca no existe, revise el nombre del contacto y vuelva a buscarlo")
    except:
        print("El nombre de agenda ingresado no existe, revise el nombre de la agenda y vuelva a ingresarlo")

def delete_contact(name_contact_book):
    try:
        print("\t\t........................................................................")
        print("\t \t Ingresaste a la opcion para aliminar un contacto")
        print("\t\t........................................................................")
        read_contact=open(name_contact_book,"r")
        list_contacts=[]
        list_contacts= [linea.rstrip() for linea in read_contact]
        number_id=input("ingrese el numero de cedula del contacto que desea borrar: ")
        try:
            index_number_id=list_contacts.index(number_id)
            index_name=index_number_id-1
            index_number_phone=index_number_id+2
            name=list_contacts[index_name]
            print("**********************************************************")
            print(f"El numero de cedula del estudiante a eliminar es {number_id}, el nombre es {name}. el contacto sera borardo de la agenda.....")
            del list_contacts[index_name:index_number_phone]
            write_file=open(name_contact_book,"w")
            for item in list_contacts:
                write_file.write(item + "\n")
        except:
            print("**********************************************************")
            print("el contacto que desea eliminar no existe en la agenda, revise el numero de cedula del contacto y vuelva a intentarlo")
    
    except:
        print("El nombre de agenda ingresado no existe, revise el nombre de la agenda y vuelva a ingresarlo")

def show_contacts(name_contact_book):
    try:
        print("\t\t........................................................................")
        print("\t \t Ingresaste a la opcion para visualizar todos los contactos")
        print("\t\t........................................................................")
        show_contacts=open(name_contact_book,"r")
        read_contacts=show_contacts.read()
        print(read_contacts)
    except:
        print("\t El nombre de agenda ingresado no existe, revise el nombre de la agenda y vuelva a ingresarlo")
    
def show_contacts_letter(name_contact_book):
    try:
        print("\t\t........................................................................")
        print("\t \t Ingresaste a la opcion para vizualizar contactos por una letra especifica")
        print("\t\t........................................................................")

        search_letter=input("ingrese la letra por la cual desea realizar la busqueda de contactos: ")
        show_contact=open(name_contact_book,"r")
        list_contacts=[]
        values=[]
        list_contacts= [line.rstrip() for line in show_contact]
        for value in list_contacts:
            first_letter=value.startswith(search_letter)
            values.append(first_letter)
        contacts_count=values.count(True)

    
        if contacts_count >=1:
            show_contact=open(name_contact_book,"r")
            for line in show_contact:
                line=line.strip()
                if not line.find(search_letter):
                    print("**********************************************************")
                    index_name=list_contacts.index(line)
                    index_number_id=index_name +1
                    index_number_phone=index_name+2
                    name=list_contacts[index_name]
                    id_contact=list_contacts[index_number_id]
                    phone=list_contacts[index_number_phone]
                    print(name)
                    print(id_contact)
                    print(phone)
                    print("**********************************************************")
                      
        else:
            print("**********************************************************")
            print(f"No hay ningun contacto que empiece por la letra {search_letter} en la agenda de contactos.")
            print("**********************************************************")
    except:
        print("El nombre de agenda ingresado no existe, revise el nombre de la agenda y vuelva a ingresarlo")



print("\t\t.............................................................")
print("\t\t........................Su agenda............................")
print("\t\t.............................................................")

while True:
    try:
        new_contact_book=int(input("\n 1. Crear nueva agenda \n 2. Editar y consultar contactos de una agenda ya existente \n Inserte la opcion deseada 1 o 2: "))
        if new_contact_book ==1 or new_contact_book==2:
            break
        else:
            print("**********************************************************")
            print("El numero ingresado no esta dentro de las opciones, debe ser '1' o '2'. Intentelo de nuevo.")
            print("**********************************************************")
    except:
        print("**********************************************************")
        print("El valor ingresado no es valido debe ser '1' o '2'. intentelo de nuevo.")
        print("**********************************************************")
        
if new_contact_book==1:
    new_file=input("\t Ingrese el nombre y extencion del archivo a crear: ")
    file_text=open(new_file,"x")

elif new_contact_book==2:
    
    answer=1
    print(".......................................................................")
    name_contact_book=input("Ingrese el nombre y extencion de la agenda existente: ")
    while answer<=0 or answer >=0:
        print("\t *************************************************************")
        print("\t ****************menu de contactos****************************")
        print("\t *************************************************************")
        print("\t 1. Opcion para agregar un nuevo contacto.")
        print("\t 2. Opcion para buscar el numero de celular de un contacto a traves del nombre y apellido.")
        print("\t 3. Opcion para borar un contacto de la agenda a traves del numero de cedula.")
        print("\t 4. Opcion para mostar en consola todos los contactos de la agenda.")
        print("\t 5. Opcion para mostar en consola los contactos que empiezan por una letra determinada ")
        print("\t 6. Opcion para salir del menu.")

        answer=int(input("Ingrese la opcion deseada:" ))

        if answer==1:
            print("**********************************************************")
            add_contact(name_contact_book)
        elif answer==2:
            print("**********************************************************")
            search_contact(name_contact_book)
        elif answer==3:
            delete_contact(name_contact_book)
        elif answer == 4:
            show_contacts(name_contact_book)
        elif answer == 5:
            show_contacts_letter(name_contact_book)
        elif answer==6:
            print("Saliste del menu")
            sys.exit()
        else:
            print("**********************************************************")
            print("Por favor ingrese una opcion valida")
            print("**********************************************************")
