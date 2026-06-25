# The Quest for the Legendary Treasure

A simple text based adventure game made in Python for the course end project
"Building a Python Adventure Game with GitHub Copilot".

## How to run it

```
python adventure_game.py
```

You play as an explorer looking for a treasure. The game asks your name and then
you make choices to explore a forest or a cave. Type the number of your choice
(like 1 or 2) and press Enter. The game ends when you win (find the treasure),
lose (make a bad choice), or you can choose to play again.

## Files

- `adventure_game.py` - the game
- `Report.pdf` - the report about using GitHub Copilot
- `build_report.py` - the script I used to make the report PDF

## Main functions

- `start_game()` - intro, asks for name, first choice (forest or cave)
- `forest_path()` - the forest part with its choices
- `cave_path()` - the cave part with its choices
- `treasure_room()` - the ending, checks if you have the key
- `get_choice()` - helper that keeps asking until you type a valid answer
- `main()` - runs the game in a loop so you can play again

Made with Python 3. The game only uses the standard library. The report script
needs reportlab (`pip install reportlab`).
