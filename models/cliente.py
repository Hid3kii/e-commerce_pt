class Cliente:
     def __init__(self, id, nome, cpf, email):
          self.id = id
          self.nome = nome
          self.cpf = cpf
          self.email = email

     def exibir_DETALHES(self):
          print(f"ID: {self.id} | Nome : {self.nome} | CPF : {self.cpf} | EMAIL : {self.email}")

     def atualizar_email(self, novo_email):
          if "@" in novo_email and "." in novo_email:
               self.email = novo_email
               print(f"E-mail do cliente {self.nome} atualizado para {self.email}")
          else:
               print("Email inválido !  o email precisa conter '@' e '.'.")