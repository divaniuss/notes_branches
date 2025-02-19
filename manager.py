class Manager:
    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def search(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def delete(self, id):
        self.notes = [note for note in self.notes if note.id != id]

    def show_all(self):
        print("Все заметки: \n")
        for note in self.notes:
            print(note.toString())