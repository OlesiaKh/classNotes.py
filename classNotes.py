class Notes:
    def __init__(self, file_name='notes.txt'):
        self.file_name = file_name

    def add_notes(self, contact_name, note):
        with open(self.file_name, 'a') as file:
            file.write(f"{contact_name}: {note}\n")

    def show_all_notes(self):
        with open(self.file_name, 'r') as file:
            notes = file.read()
        return notes

    def search_notes_by_tag(self, tag):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            matching_notes = [line for line in lines if tag in line]
        return ''.join(matching_notes)

# Inside  main bot's functionality
notes = Notes()

while True:
    user_input = input("Enter a command (add notes / show all notes / search notes / back): ").strip()

    if user_input == 'add notes':
        contact_name = input("Enter contact's name: ")
        note = input("Enter the note: ")
        notes.add_notes(contact_name, note)
        print("Note added!")

    elif user_input == 'show all notes':
        all_notes = notes.show_all_notes()
        print("All Notes:\n", all_notes)

    elif user_input == 'search notes':
        tag = input("Enter the tag to search for: ")
        matching_notes = notes.search_notes_by_tag(tag)
        if matching_notes:
            print("Matching Notes:\n", matching_notes)
        else:
            print("No notes found with this tag.")

    elif user_input == 'back':
        print("Going back to the previous menu.")
        break

    else:
        print("Unknown command. Please try again.")
