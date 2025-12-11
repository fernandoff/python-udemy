from enum import Enum

class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"

    def __str__(self):
        return self.value
    
