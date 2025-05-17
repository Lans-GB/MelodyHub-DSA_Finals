# Example music list format:
# TITLE --- ARTIST --- GENRE --- MOOD
# Happy --- Pharrell Williams --- Pop --- happy
# Hey Barbara --- IV of Spades --- Funk --- happy
# Can't Stop the Feeling! --- Justin Timberlake --- Pop --- happy
# Ere --- Juan Carlos --- Pop --- sad
# Someone Like You --- Adele --- Pop --- sad
# The Scientist --- Coldplay --- Rock --- sad
# Kiss The Rain --- Yiruma --- Classical --- focused
# Runaway --- AURORA --- Pop --- focused
# Bad --- wave to earth --- Jazz --- focused
# Billie Jean --- Michael Jackson --- Pop --- party
# Enter Sandman --- Metallica --- Metal --- party
# Dancing Queen --- Abba --- Disco --- party
# Shape of You --- Ed Sheeran --- Pop --- chill
# Espresso --- Sabrina Carpenter --- Funk --- chill
# Golden Hour --- JVKE --- Pop --- chill

# MelodyHub: Terminal-based music manager and playlist maker

music_list = []

# Accepted genres and moods
VALID_GENRES = [
    "Pop", "Rock", "Rap", "Metal", "R&B", "Funk", "Jazz",
    "Blues", "Country", "Classical", "Reggae", "EDM", "Disco"
]
VALID_MOODS = ["happy", "sad", "focused", "party", "chill"]

def display_music(i, music):
    # Print music details
    print(f"{i}. {music['title']} by {music['artist']} - Genre: {music['genre']}, Mood: {music['mood']}")

def display_menu():
    # Show main menu
    print("\n[1] Add Music")
    print("[2] View Stored Music")
    print("[3] Generate Playlist")
    print("[4] Remove Music")
    print("[5] Exit")

def add_music():
    # Add music with input validation
    print("\n--- Add Music ---")
    title = input("Enter music title: ")
    artist = input("Enter artist name: ")

    print("- Choose genre (e.g., Pop, Rock, Jazz, etc.)")
    while True:
        genre_input = input("Enter genre: ").strip()
        if genre_input.lower() in [g.lower() for g in VALID_GENRES]:
            genre = next(g for g in VALID_GENRES if g.lower() == genre_input.lower())
            break
        else:
            print("Invalid genre. Try again.")

    while True:
        mood_input = input("Enter mood (happy, sad, focused, party, chill): ").strip()
        if mood_input.lower() in [m.lower() for m in VALID_MOODS]:
            mood = next(m for m in VALID_MOODS if m.lower() == mood_input.lower())
            break
        else:
            print("Invalid mood. Try again.")

    music = {"title": title, "artist": artist, "genre": genre, "mood": mood}
    music_list.append(music)
    print("\nMusic added!")

def view_stored_music():
    # Show all music sorted by title
    print("\n--- Stored Music ---")
    if music_list:
        sorted_music = sorted(music_list, key=lambda x: x['title'].lower())
        for i, music in enumerate(sorted_music, 1):
            display_music(i, music)
    else:
        print("No music stored.")

def generate_playlist():
    # Generate playlist by mood
    print("\n--- Generate Playlist ---")
    if not music_list:
        print("No music available.")
        return

    print("Select mood:")
    print("[1] Happy\n[2] Sad\n[3] Focused\n[4] Party\n[5] Chill")
    mood_map = {"1": "happy", "2": "sad", "3": "focused", "4": "party", "5": "chill"}
    selected_mood = mood_map.get(input("Choose a mood (1-5): "))

    if selected_mood:
        playlist = sorted(
            [m for m in music_list if m['mood'] == selected_mood],
            key=lambda x: x['title'].lower()
        )
        if playlist:
            print(f"\n--- {selected_mood.capitalize()} Playlist ---")
            for i, music in enumerate(playlist, 1):
                print(f"{i}. {music['title']} by {music['artist']} - Genre: {music['genre']}")
        else:
            print(f"\nNo music with mood: {selected_mood}")
    else:
        print("\nInvalid selection.")

def remove_music():
    # Remove music by number
    print("\n--- Remove Music ---")
    if music_list:
        for i, music in enumerate(music_list, 1):
            print(f"{i}. {music['title']} by {music['artist']}")
        try:
            choice = int(input("Enter number to remove: "))
            if 1 <= choice <= len(music_list):
                removed = music_list.pop(choice - 1)
                print(f"\nRemoved '{removed['title']}' by {removed['artist']}.")
            else:
                print("\nInvalid number.")
        except ValueError:
            print("\nPlease enter a number.")
    else:
        print("No music to remove.")

def main():
    # Main program loop
    print("\nWelcome to MelodyHub!")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_music()
        elif choice == "2":
            view_stored_music()
        elif choice == "3":
            generate_playlist()
        elif choice == "4":
            remove_music()
        elif choice == "5":
            print("\nThanks for using MelodyHub! Goodbye!\n")
            break
        else:
            print("Invalid option. Try 1-5.")

main()
