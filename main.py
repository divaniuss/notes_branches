from manager import Manager
from notes import Note

manager = Manager()

note1 = Note(1, "title1", "text1")
note2 = Note(2, "title2", "text2")
note3 = Note(3, "title3", "text3")

manager.add(note1)
manager.add(note2)
manager.add(note3)


manager.show_all()