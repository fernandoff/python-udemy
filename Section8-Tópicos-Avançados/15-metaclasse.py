# %% [markdown]
# Metaclasse
# - Cria classe de forma dinâmica.
# - Pode ser útil na criação de frameworks onde as classes precisam ter um comportamento específico

# %%
class MeuMeta(type):
    def __new__(cls, nome, bases, dct):
        dct['novo_atributo'] = 'Valor adicionado pela metaclasse'
        return super().__new__(cls, nome, bases, dct)

# %%
class MinhaClasse(metaclass=MeuMeta):
    pass

# %%
obj = MinhaClasse()
obj.novo_atributo

# %%
class ValidadorMeta(type):
    def __new__(cls, nome, bases, dct):
        # Dicionário para armazenar as validações
        validacoes = dct.get('validacoes', {})
        
        for attr, tipo in validacoes.items():
            if not callable(tipo):
                raise TypeError(f"O tipo de validação para '{attr}' deve ser uma função.")
            
            # Adiciona uma nova função de validação
            def valida_func(self, value, attr=attr, tipo=tipo):
                if not isinstance(value, tipo):
                    raise ValueError(f"'{attr}' deve ser do tipo {tipo.__name__}")
                self.__dict__[attr] = value

            # Renomeia a função para evitar problemas de escopo
            valida_func.__name__ = f"seta_{attr}"

            dct[f"seta_{attr}"] = valida_func
        
        return super().__new__(cls, nome, bases, dct)

# %%
class Usuario(metaclass=ValidadorMeta):
    validacoes = {
        'nome': str,
        'idade': int,
    }

    def __init__(self, nome, idade):
        self.seta_nome(nome)
        self.seta_idade(idade)

    def __str__(self):
        return f"Usuario: {{ Nome = {self.nome}, Idade = {self.idade} }}"

# %%
try:
    user = Usuario("Alice", 30)
    print(f"Nome: {user.nome}, Idade: {user.idade}")

    # Tentativa de atribuir um tipo inválido
    #user.seta_idade("trinta")  # Isso irá gerar um ValueError
    user.seta_nome("Jhon")    

    print(user)
except ValueError as e:
    print(e)


