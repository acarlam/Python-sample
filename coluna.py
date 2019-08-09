#coluna.py
from decimal import Decimal


class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description
        self.is_pk = False 

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)
        return _str

    def validate(self, data):
        if self._kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif self._kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif self.kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super().__init__(name,  kind, description="")
        self._is_pk = True