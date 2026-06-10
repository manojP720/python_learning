import turtle

def draw_heart(color="red", pen_size=2):
    """Draws a heart shape using turtle graphics."""
    screen = turtle.Screen()
    screen.title("Heart Shape with Python Turtle")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.color(color)
    pen.pensize(pen_size)
    pen.speed(2)

    # Move to starting position
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()

    # Draw heart shape
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

    # Keep window open until closed by user
    screen.mainloop()

if __name__ == "__main__":
    try:
        # Optional: Let user choose color
        user_color = input("Enter heart color (default red): ").strip().lower()
        if not user_color:
            user_color = "red"
        draw_heart(user_color)
    except turtle.Terminator:
        print("Turtle graphics window closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
