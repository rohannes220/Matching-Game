import os
import random
import turtle
from Card import Card 
LEADERBOARD_FILE = "leaderboard.txt"
CARDS_FOLDER = "Cards"
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 40
BUTTON_X = 400
BUTTON_Y = -350
class MemoryGame:
    def __init__(self, screen):
        
        """Initializes the game and and sets up the game screen along with leaderboard,scoreboard,and statusboard as well as the turtle objects. 
        It calls start game to essentially begin matching. 
        """
        
        self.screen = screen
        self.screen.onclick(self.handle_click)

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.status_board_turtle = turtle.Turtle()
        self.status_board_turtle.hideturtle()
        self.status_board_turtle.speed(0)
        self.leaderboard_turtle = turtle.Turtle()
        self.leaderboard_turtle.hideturtle()
        self.leaderboard_turtle.speed(0)
        self.popup_turtle = turtle.Turtle()
        self.popup_turtle.hideturtle()
        self.popup_turtle.speed(0)

        self.draw_game_board()
        self.draw_status_board()
        self.draw_leader_board()
        self.draw_button()

        self.start_game()

    def draw_game_board(self):
        
        "Draws the gameboard using turtle, this is where the cards are."
        board_width = 1000
        board_height = 600
        self.turtle.penup()
        self.turtle.goto(-750, 350)
        self.turtle.setheading(0)
        self.turtle.pensize(5)
        self.turtle.fillcolor("white")
        self.turtle.begin_fill()
        self.turtle.forward(board_width)
        self.turtle.right(90)
        self.turtle.forward(board_height)
        self.turtle.right(90)
        self.turtle.forward(board_width)
        self.turtle.right(90)
        self.turtle.forward(board_height)
        self.turtle.right(90)
        self.turtle.end_fill()

    def draw_status_board(self):
        "Draws the statusboard using turtle, this is where matches and guesses are."
        width = 150
        height = 100
        self.turtle.penup()
        self.turtle.goto(-375, -375)
        self.turtle.setheading(180)
        self.turtle.pendown()
        self.turtle.pensize(5)
        self.turtle.fillcolor("white")
        self.turtle.begin_fill()
        self.turtle.forward(width)
        self.turtle.right(90)
        self.turtle.forward(height)
        self.turtle.right(90)
        self.turtle.forward(width)
        self.turtle.right(90)
        self.turtle.forward(height)
        self.turtle.right(90)
        self.turtle.end_fill()

    def draw_leader_board(self):
        "Draws the leaderboard using turtle, this is where the scoreboard is."
        width = 200
        height = 500
        self.turtle.pensize(5)
        self.turtle.penup()
        self.turtle.goto(500, -200)
        self.turtle.pendown()

        self.turtle.forward(width)  # Side 1
        self.turtle.right(90)
        self.turtle.forward(height)  # Side 2
        self.turtle.right(90)
        self.turtle.forward(width)  # Side 3
        self.turtle.right(90)
        self.turtle.forward(height)  # Side 4
        self.turtle.right(90)
        self.turtle.setheading(90)

        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()

        self.turtle.penup()
        self.turtle.goto(400, 240)
        self.turtle.color("blue")
        self.turtle.write("Leaderboard", align="center", font=("Arial", 20, "bold"))
        self.turtle.pendown()

    def is_quit_button_clicked(self, x, y):
        "Checks to see if the quit button is clicked by seeing if x and y falls within the boundaries"
        button_left = BUTTON_X - BUTTON_WIDTH / 2
        button_right = BUTTON_X + BUTTON_WIDTH / 2
        button_top = BUTTON_Y + BUTTON_HEIGHT / 2
        button_bottom = BUTTON_Y - BUTTON_HEIGHT / 2
        return button_left <= x <= button_right and button_bottom <= y <= button_top

    def draw_button(self):
        "Draws quit button"
        path = "Memory_Game_Images/quitbutton.gif"
        self.screen.register_shape(path)
        self.turtle.shape(path)
        self.turtle.penup()
        self.turtle.goto(BUTTON_X, BUTTON_Y)
        self.turtle.stamp()
        self.turtle.pendown()

    def update_display(self):
        "Updates the leaderboard and statusboard by adding each score. It starts off by clearing everything"
        self.leaderboard_turtle.clear()
        for i, (name, guesses) in enumerate(self.leaderboard):
            self.leaderboard_turtle.penup()
            self.leaderboard_turtle.goto(400, 200 - i * 30)
            self.leaderboard_turtle.write(
                f"{name} : {guesses}", align="center", font=("Arial", 15, "bold")
            )

        self.status_board_turtle.clear()
        current_status = {"Guesses": self.num_guesses, "Matches": self.num_matches}
        for index, (status, value) in enumerate(current_status.items()):
            self.status_board_turtle.penup()
            self.status_board_turtle.goto(-450, -320 - index * 30)
            self.status_board_turtle.write(
                f"{status} : {value}", align="center", font=("Arial", 15, "bold")
            )
    def load_leaderboard(self):
        "Takes the leaderboard file and loads everything on to the scoreboard"
        self.leaderboard = []
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                for line in f:
                    name, score = line.strip().split(",")
                    self.leaderboard.append((name, int(score)))
        except:
            pass

    def get_num_cards_input(self):
        "Gets user input for cards and makes sure its a valid number. Returns the valid number"
        num_cards = self.screen.textinput(
            "Card Selection",
            "How many cards do you want? (8, 10, or 12 only):",
        )
        while True:
            try:
                num_cards = int(num_cards)
                if num_cards  == 8 or num_cards == 10 or num_cards == 12:
                    return num_cards
                else:
                    num_cards = self.screen.textinput(
                        "Invalid Selection",
                        "How many cards do you want? (8, 10, or 12 only):",
                    )
            except:
                num_cards = self.screen.textinput(
                    "Invalid Selection",
                    "How many cards do you want? (8, 10, or 12 only):",
                )

    def get_name_input(self):
        "Asks for your name"
        return self.screen.textinput(
            "Name",
            "Enter your name:",
        )

    def insert_into_leaderboard_and_save(self):
        "Adds the current players socres into the leaderboard and uses the sort method to sort by score using the score as a key"
        self.leaderboard.append((self.name, self.num_guesses))
        self.leaderboard.sort(key=self.sort_by_score)

        self.leaderboard = self.leaderboard[:8]

        with open(LEADERBOARD_FILE, "w") as f:
            for name, score in self.leaderboard:
                f.write(f"{name},{score}\n")

    def sort_by_score(self, item):
        """Sort the leaderboard by the score"""
        return item[1]

    def get_all_coordinates(self):
        "Based on user input creates the card coordinates and stores them in a list, which is later used"
        start_X = -375
        start_Y = 175
        if self.num_cards == 8:
            per_row = 4
        elif self.num_cards == 10:
            per_row = 5
        elif self.num_cards == 12:
            per_row = 4
        coordinates = []
        x = start_X
        y = start_Y
        card_count = 0
        for i in range(self.num_cards):
            coordinates.append((x, y))
            x += 100 
            card_count += 1
            if card_count == per_row: 
                x = start_X  
                y -= 150  
                card_count = 0
        return coordinates

    def get_all_back_image_paths(self):
        """Get the paths to all back image files."""
        total = self.num_cards // 2 
        all_back_images = []  
        current_card = 0
        for file in os.listdir(CARDS_FOLDER):  
            file_path = os.path.join(CARDS_FOLDER, file)  
            if ".DS_Store" in file_path:  #
                continue
            if "card_back.gif" in file_path:  
                continue
            current_card += 1
            all_back_images.append(file_path)
            all_back_images.append(file_path) 
            if current_card == total:
                break
        return all_back_images

    def run(self):
        """Starts the game officially by taking your input number and name. Uses a for loop to create the cards and coordinates"""
        self.num_cards = self.get_num_cards_input()
        self.name = self.get_name_input()
        self.update_display()

        back_image_paths = self.get_all_back_image_paths()
        random.shuffle(back_image_paths)
        coordinates = self.get_all_coordinates()
        for i in range(self.num_cards):
            x, y = coordinates[i]
            front_image_path = "Cards/card_back.gif"
            back_image_path = back_image_paths[i]
            card = Card(x, y, front_image_path, back_image_path, self.screen)
            self.cards.append(card)
        for card in self.cards:  # Draw all cards
            card.draw()

    def show_popup(self, path):
        "Shows the I quit message and other messages"
        self.screen.addshape(path)
        self.popup_turtle.shape(path)
        self.popup_turtle.penup()
        self.popup_turtle.goto(0, 0)
        self.popup_turtle.stamp()

    def handle_click(self, x, y):
        if self.is_quit_button_clicked(x, y):
            self.show_popup("Memory_Game_Images/quitmsg.gif")
            self.screen.ontimer(self.screen.bye, 5000)
            return

        """Handle the click event. Makes sure everytying matches and sees if the quit button is clicked"""
        for card in self.cards:
            if not card.is_hidden and card.is_click_inside(x, y):
                card.flip()
                card.draw()
                self.screen.ontimer(card.flip_and_draw, 1500)
                if self.card1 == None:
                    self.card1 = card
                    continue
                self.num_guesses += 1
                self.update_display()
                self.card2 = card
                if self.card1.is_same_card(self.card2):
                    self.num_matches += 1
                    self.update_display()

                    self.card1.hide()
                    self.card2.hide()

                    if self.is_game_done():
                        self.insert_into_leaderboard_and_save()
                        self.update_display()
                        self.show_popup("Memory_Game_Images/winner.gif")
                        self.screen.ontimer(self.restart_handler, 3000)
                        return

                self.card1 = None
                self.card2 = None

    def start_game(self):
        """Starts the game, not the SETUP but the GAME. It resets the leaderboard, cards, guesses, and matches.
        Updates the display to reflect the new game state."""
        self.load_leaderboard()
        self.cards = []
        self.num_cards = None
        self.card1 = None
        self.card2 = None
        self.num_guesses = 0
        self.num_matches = 0
        self.update_display()
    def restart_handler(self):
        "After you hit I quit or match all cards it removes popup and starts again"
        self.popup_turtle.clear()
        self.restart_game()

    def is_game_done(self):
        "Checks to see if all cards are gone"
        return self.num_matches == self.num_cards // 2

    def restart_game(self):
        "Starts the game all over again"
        self.start_game()
        self.run()
def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=800)
    screen.bgcolor("lightblue")
    game = MemoryGame(screen)
    game.run()
    screen.mainloop()
if __name__ == "__main__":
    main()
