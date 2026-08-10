class Cliente:
     def __init__(self, id, nome, cpf, email):
          self.id = id
          self.nome = nome
          self.cpf = cpf
          self.email = email

     def exibir_detalhes(self):
          print(f"ID: {self.id} | Nome : {self.nome} | CPF : {self.cpf} | EMAIL : {self.email}")

     def atualizar_email(self, novo_email):
          if "@" in novo_email and "." in novo_email:
               self.email = novo_email
               print(f"E-mail do cliente {self.nome} atualizado para {self.email}")
          else:
               print("Email inválido !  o email precisa conter '@' e '.'.")

     def to_dict(self):
          return{
               "id": self.id,
               "nome": self.nome,
               "cpf": self.cpf,
               "email": self.email,
          }

     @classmethod
     def from_dict(cls, dados):
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            cpf=dados["cpf"],
            email=dados["email"]
        )