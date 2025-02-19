class Note:
    def __init__(self, id, title, text):
        self.__id = id
        self.__title = title
        self.__text = text

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text

    def toString(self):
        return f"Note {self.__title} (ID={self.__id}): \n {self.__text}]"