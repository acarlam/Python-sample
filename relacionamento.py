#relacionamento.py

class Relationship:
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on

class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []


    def add_column(self, name, kind, description=""):
        column = Column(name=name, kind=kind, description=description)
        self._columns.append(column)
        return column
    

    def add_references(self, name, to, on):
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)


    def add_referenced(self, name, by, on):
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)


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

class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super().__init__(name,  kind, description="")
        self._is_pk = True

if __name__ == ''--if __name__ == "__main__":
    
                    




