import turtle

CARD_WIDTH = 100
CARD_HEIGHT = 150


class Card:
    def __init__(self, x, y, front_image, back_image, screen):
        """
        Initializes a Card object with specific attributes.
        
        Args:
            x (int): The x-coordinate of the card's position.
            y (int): The y-coordinate of the card's position.
            front_image (str): Path to the image displayed when the card is face-up.
            back_image (str): Path to the image displayed when the card is face-down.
            screen (turtle.Screen): The screen object where the card is displayed.
        """
        self.x = x
        self.y = y
        self.front_image = front_image
        self.back_image = back_image
        self.screen = screen
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.screen.addshape(front_image)
        self.screen.addshape(back_image)
        self.turtle.shape(front_image)
        self.is_face_down = True
        self.stamp_id = None
        self.is_hidden = False
        
        
    def is_click_inside(self, x, y):
        """Checks if a card click is within the boundaries of the card"""
        left = self.x - CARD_WIDTH // 2
        right = self.x + CARD_WIDTH // 2
        bottom = self.y - CARD_HEIGHT // 2
        top = self.y + CARD_HEIGHT // 2
        if (left <= x <= right) == False:
            return False
        if (bottom <= y <= top) == False:
         return False
        return True

    def flip(self):
        """Flips the card's state between face-up and face-down, By modifiying the `is_face_down` attribute."""
        if self.is_face_down == True:  
            self.is_face_down = False  
        else:
            self.is_face_down = True

    def draw(self):
        """Draw the current card, based on it being facedown. The stamp is what adds it to the list."""
        if self.is_face_down == True:
            self.turtle.shape(self.front_image)
        else:
            self.turtle.shape(self.back_image)
        if self.stamp_id is None:
            self.stamp_id = self.turtle.stamp()
            return
        self.turtle.clearstamp(self.stamp_id)
        self.stamp_id = self.turtle.stamp()

    def flip_and_draw(self):
        "Flips and redraws the card,used for a flip"
        if self.is_hidden == True:
            return
        self.flip()
        self.draw()

    def hide(self):
        """Removes the stamp from the card and the from the gameboard"""
        self.turtle.clearstamps()
        self.stamp_id = None
        self.is_hidden = True

    def is_same_card(self, other):
        "Sees if cards match basedon back image"
        return self.back_image == other.back_image


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("lightblue")
    card = Card(200, 200, "Cards/card_back.gif", "Cards/2_of_clubs.gif", screen)
    card.draw()

    screen.ontimer(card.flip_and_draw, 5000)

    # Run the game loop
    screen.mainloop()


if __name__ == "__main__":
    main()
