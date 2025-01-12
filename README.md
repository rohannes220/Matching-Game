
# Memory Match Game: README

## Overview

This Python project implements a **Memory Match** game using the **Turtle** graphics library, where the player matches pairs of cards by flipping them over and remembering their positions. The game includes a user-friendly GUI that allows players to interact with the game using mouse clicks. The objective is to match all pairs in as few guesses as possible.

## Project Structure

The project is organized into the following files and folders:

1. **Memory_Game.py**: The main Python file that runs the game, containing the `main()` function and game logic.
2. **Cards/**: A folder that holds all the card images used in the game (e.g., front-facing card images).
3. **Memory_Game_Images/**: A folder containing images for UI elements like the "Quit" button, error messages, etc.
4. **leaderboard.txt**: A text file used for storing and retrieving the leaderboard, keeping track of the top players and their statistics.
5. **Cards.py**: A Python file that contains the logic for flipping and matching cards during the game.

### Game Play

- **User Input**: The player can enter their name through a pop-up window at the start of the game.
- **Card Selection**: The player selects cards by clicking on them with the mouse. If two selected cards match, they remain face up; otherwise, they flip back down after a brief delay.
- **Game Options**: The player can choose between 8, 10, or 12 cards. If an invalid number is entered, the program will either auto-correct the input or prompt the user to enter a valid value.
- **Leaderboard**: The game tracks the player's number of guesses and matches, saving the leaderboard between sessions in **leaderboard.txt**.
- **Quit Option**: A "Quit" button allows the player to exit the game early. Players who quit do not have their statistics added to the leaderboard.
- **Victory**: When all pairs are matched, a victory message is displayed, and the game ends.

## How to Run

1. **Install Dependencies**:
   - This project uses Python 3.x and the **Turtle** graphics library. No additional installation is required for **Turtle** since it’s part of Python’s standard library.

2. **Running the Game**:
   - Open **Memory_Game.py** in your Python environment (e.g., IDLE).
   - Run the file, and the game will prompt for the player's name and card selection.

3. **Game Controls**:
   - The player can select the number of cards (8, 10, or 12).
   - Click on the cards to flip them and try to match pairs.

4. **End of Game**:
   - When all pairs are matched, the player wins, and a victory message is displayed.

## File Descriptions

### **Memory_Game.py**  
- The main file that runs the entire game. It contains the game loop and overall logic.

### **Cards/**  
- A folder that contains the card images for the game. These images are used to represent the front of the cards.

### **Memory_Game_Images/**  
- A folder containing images for UI elements such as the "Quit" button, error messages, and other interface graphics.

### **leaderboard.txt**  
- A text file used for storing and retrieving the leaderboard data. It keeps track of the top players and their statistics, such as the number of guesses and matches.

### **Cards.py**  
- This file contains the logic for card flipping and matching. It handles the interactions that allow the game to track the player's guesses and determine when two selected cards match.


### Key Features:
- **Card Images**: The game loads card images from the **Cards/** folder, allowing for easy customization of the deck.
- **Leaderboard**: The leaderboard persists between game sessions, storing player names, guesses, and matches.
- **Cross-Platform Compatibility**: The program is written in a way that ensures compatibility across Windows, Linux, and macOS.

## Conclusion

This project provides an interactive and visually appealing implementation of the classic Memory Match game. By using **Turtle** graphics, it offers a unique approach to implementing games in Python while maintaining cross-platform compatibility. The game is flexible, allowing players to customize the card deck, and keeps track of the leaderboard across sessions.
