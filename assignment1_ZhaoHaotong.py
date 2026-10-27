import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Triangle Drawing")

t = turtle.Turtle()
t.speed(0)

colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF3"]

for i in range(100):
  t.pencolor(colors[i % len(colors)])
  t.forward(i * 3)
  t.left(120)
  t.width(i / 25 + 1)

t.hideturtle()
turtle.done()









while True:
  query = input("Ask me a question: ").lower()
  if query == "exit":
    break
  elif "hku" in query:
    print("HKU is the University of Hong Kong, a world-class institution.")
  elif "robot" in query:
    print(
        "Robots are programmable machines capable of carrying out complex"
        " actions."
    )
  elif "jetson" in query:
    print(
        "Jetson is a series of embedded computing board products from NVIDIA"
        " for AI at the edge."
    )
  elif "ai" in query:
    print(
        "AI stands for Artificial Intelligence, simulating human intelligence in"
        " machines."
    )
  elif "human" in query:
    print("Humans are biological beings capable of reasoning and emotion.")
  else:
    print("I don't understand that keyword. Try asking about HKU, robot, jetson, ai, or human.")
