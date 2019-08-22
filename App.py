#from Usuarios import Application3
from tkinter import *
from tkinter import messagebox

import time
#from chamadaTela2 import janela


import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDFp_lhvJuvJE_or0ODMyqbI4jsiBS6Wlc",
    "authDomain": "sd-biblioteca-3a528.firebaseapp.com",
    "databaseURL": "https://sd-biblioteca-3a528.firebaseio.com",
    "projectId": "sd-biblioteca-3a528",
    "storageBucket": "",
    "messagingSenderId": "967381443181",
    "appId": "1:967381443181:web:b96e03b085893a38"
  };



firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() 
#authenticar um usuário 

#email = input("Enter the email : ")
#password = input("Enter the pass : ")
#user = auth.sign_in_with_email_and_password (email, password)

usu = auth.sign_in_with_email_and_password ("joao@gmail.com", "joao1996")

db=firebase.database()
#cliar
#livros = {"titulo": None, "autor": None, "paginas": None, "ano": None}


#db.child("biblioteca").child("livros").set(livros, usu['idToken'])
#base = db.child("biblioteca")


class Application1:
    def __init__(self, master=None):

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()

        self.titulo = Label(self.container1, text="Biblioteca SD")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.pack()


        #self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10)
        #self.btnBuscar["command"] = "self.buscarUsuario"
       # self.btnBuscar.pack(side=RIGHT)

        #self.bntInsert = Button(self.container3, text="Inserir",font=self.fonte, width=12)
       # self.bntInsert["command"] = "self.inserirUsuario"
       # self.bntInsert.pack(side=LEFT)

        #self.bntAlterar = Button(self.container4, text="Alterar",
       #                          font=self.fonte, width=12)
       # self.bntAlterar["command"] = "self.alterarUsuario"
       # self.bntAlterar.pack(side=LEFT)

        self.bntTeste = Button(self.container8, text="Livros", font=self.fonte, width=12)
        self.bntTeste["command"] = self.telinha

        self.bntTeste.pack(side=LEFT)

    
        #self.bntExcluir = Button(self.container6, text="Excluir",font=self.fonte, width=12)
       # self.bntExcluir["command"] = "self.excluirUsuario"
        #self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
   
    def telinha(self):
        root.destroy()
        jan = Tk()
        jan.title("Tela de Cadastro")

        jan.geometry("500x400")
        mario = PhotoImage(file = "img1.png")

        label = Label(jan, image = mario).place(x=100,y=20)
        photo = PhotoImage(file = "img1.png")
        label = Label(jan, image = photo).place(x=3,y=600)

        Application2(jan)
        jan.mainloop()
    
  

class Application2:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()

        self.titulo = Label(self.container1, text="Cadastro de livros")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.pack()


        self.lblidusuario = Label(self.container2,text="COD:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtcodlivro = Entry(self.container2)
        self.txtcodlivro["width"] = 10
        self.txtcodlivro["font"] = self.fonte
        self.txtcodlivro.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Título:",font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txttitulo = Entry(self.container3)
        self.txttitulo["width"] = 25
        self.txttitulo["font"] = self.fonte
        self.txttitulo.pack(side=LEFT)


        self.lbltelefone = Label(self.container4, text="Autor:",font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txtautor = Entry(self.container4)
        self.txtautor["width"] = 25
        self.txtautor["font"] = self.fonte
        self.txtautor.pack(side=LEFT)


        self.lblemail = Label(self.container5, text="Quant. de Páginas:",font=self.fonte, width=20)
        self.lblemail.pack(side=LEFT)

        self.txtqtdpaginas = Entry(self.container5)
        self.txtqtdpaginas["width"] = 25
        self.txtqtdpaginas["font"] = self.fonte
        self.txtqtdpaginas.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Ano da Publicação:",font=self.fonte, width=20)
        self.lblusuario.pack(side=LEFT)

        self.txtano = Entry(self.container6)
        self.txtano["width"] = 25
        self.txtano["font"] = self.fonte
        self.txtano.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
                                 font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack(side=LEFT)

        #self.bntTeste = Button(self.container8, text="Mudar de Tela",
        #                         font=self.fonte, width=12)
        #self.bntTeste["command"] = "self.telinha"

        #self.bntTeste.pack(side=LEFT)


        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

       
  

    def inserirUsuario(self):
       # user = Usuarios()
        idlivro=self.txtcodlivro.get()
        titulo = self.txttitulo.get()
        autor = self.txtautor.get()
        paginas = self.txtqtdpaginas.get()
        ano = self.txtano.get()
        #user.senha = self.txtsenha.get()

       # self.lblmsg["text"] = user.insertUser()
        if idlivro == "" or titulo == "" or autor == "" or paginas == "" or ano == "":
               messagebox.showinfo("Alerta", "Preencha todos os campos!")      
               return 
        

        tudo = db.child("livros").get()
        for d in tudo.each():
            print(d.key())
            if idlivro == d.key():
                messagebox.showinfo("Alerta", "Código já cadastrado!\nInforme um novo.")
                self.txtcodlivro.delete(0, END)
                return 
                       


        dados = {"titulo": titulo, "autor": autor, "paginas": paginas, "ano": ano}
        print(dados)     
       
        #db.child("livros").push(dados, usu['idToken'])
        #data = {"name": "Joe Tilsed"}
       
        lo = db.child("livros").get()
        print(lo.val())     
        db.child("livros").child(idlivro).set(dados)  #Esta linha armazena os dados no Firebase 
       
        self.txtcodlivro.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtautor.delete(0, END)
        self.txtqtdpaginas.delete(0, END)
        self.txtano.delete(0, END)
#        self.txtsenha.delete(0, END)


    def alterarUsuario(self):
        #user = Usuariocfs()
        idlivro = self.txtcodlivro.get()
        titulo = self.txttitulo.get()        
        autor = self.txtautor.get()
        paginas = self.txtqtdpaginas.get()
        ano = self.txtano.get()
        #user.senha = self.txtsenha.get()

        #self.lblmsg["text"] = user.updateUser()
        db.child("livros").child(idlivro).update({"titulo": titulo,"autor": autor,"paginas": paginas, "ano": ano})



        self.txtcodlivro.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtautor.delete(0, END)
        self.txtqtdpaginas.delete(0, END)
        self.txtano.delete(0, END)
        #self.txtsenha.delete(0, END)


    def excluirUsuario(self):
       # user = Usuarios()

        idlivro = self.txtcodlivro.get()

        #self.lblmsg["text"] = user.deleteUser()
        db.child("livros").child(idlivro).remove()
        self.txtcodlivro.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtautor.delete(0, END)
        self.txtqtdpaginas.delete(0, END)
        self.txtano.delete(0, END)
        #self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        #user = Usuarios()
        
            idlivro = self.txtcodlivro.get()
            if idlivro == "":
               messagebox.showinfo("Alerta", "Campo vazio. Informe um codigo!")      
               return     
            
            #self.lblmsg["text"] = user.selectUser(idlivro)
            #users = db.child("livros").child("titulo").get()
            #print("AQUI\n\n",users.val())
                    
        
            test = db.child("livros").child(idlivro).get(usu['idToken'])
             # Teste = lista dos dados buscados
            #print("\n\naaaaaaaaaaaaaaaaaaaa",test.val(),"aaaaaaaaaaaaaaaaaa")
            if test.val() == None:
                messagebox.showinfo("Alerta", "Livro não cadastrado!")
                self.txttitulo.delete(0, END)
                self.txtautor.delete(0, END)
                self.txtqtdpaginas.delete(0, END)
                self.txtano.delete(0, END)      
                return     
            



             
            
            print("\n\n\n")            
                #self.txtcodlivro.delete(0, END)
                #self.txtcodlivro.insert(INSERT, user.idlivro)
                
            tit = db.child("livros").child(idlivro).child("titulo").get()
            self.txttitulo.delete(0, END)
            #print("Valor de tit\n", tit.val())
            self.txttitulo.insert(INSERT, tit.val())

            aut = db.child("livros").child(idlivro).child("autor").get()
            self.txtautor.delete(0, END)
            self.txtautor.insert(INSERT, aut.val())

            pag = db.child("livros").child(idlivro).child("paginas").get()
            self.txtqtdpaginas.delete(0, END)
            self.txtqtdpaginas.insert(INSERT, pag.val())

            an = db.child("livros").child(idlivro).child("ano").get()
            self.txtano.delete(0, END)
            self.txtano.insert(INSERT, an.val())

    #        sen = db.child("biblioteca").child("livros").child("senha").get()
     #       self.txtsenha.delete(0, END)
      #      self.txtsenha.insert(INSERT, sen.val())
   
  



    
root = Tk()
root.title("Tela Inicial")   
root.geometry("500x400")
mario = PhotoImage(file = "img1.png")

label = Label(root, image = mario).place(x=100,y=20)
photo = PhotoImage(file = "img1.png")
label = Label(root, image = photo).place(x=3,y=600)

Application1(root)
root.mainloop()        


 