import mysql.connector
from banco import Banco

class Usuarios(object):
    def __init__(self,id_usuario=0,nome="",telefone="",email="",usuario="",senha=""):
        self.info = {}
        self.idusuario = id_usuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
    
    def insertUser(self):
        banco = Banco()
        try:
          c = banco.conexao.cursor()
          c.execute("INSERT  INTO tb_usuario(nome, telefone, email, usuario, senha)VALUES(%s,%s,%s,%s,%s)",
                            (self.nome,self.telefone,self.email,self.usuario,self.senha))
          banco.conexao.commit()
          c.close()
          return "Usuario cadastrado com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na inserção de usuario: {e}"

    def alterUser(self):
        banco = Banco()
        try:
          c = banco.conexao.cursor()
          c.execute("update tb_usuario SET nome = %s,telefone = %s, email = %s, usuario = %s, senha = %s WHERE id_usuario = %s)",
                            (self.nome,self.telefone,self.email,self.usuario,self.senha))
          banco.conexao.commit()
          c.close()
          return "Usuario alterado com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na alteração do usuario: {e}"