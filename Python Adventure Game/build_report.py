# Script to make the project report PDF.
# Uses reportlab. Run: python build_report.py

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable,
)

OUTPUT = "Report.pdf"

# light blue colors for the title and headings
BLUE = colors.HexColor("#2F77B5")
LIGHT_BLUE = colors.HexColor("#9DC3E6")

styles = getSampleStyleSheet()

title_style = ParagraphStyle("t", parent=styles["Title"], fontSize=18, spaceAfter=4, textColor=BLUE)
sub_style = ParagraphStyle("s", parent=styles["Normal"], fontSize=11, spaceAfter=2)
name_style = ParagraphStyle("n", parent=styles["Normal"], fontSize=11, spaceAfter=2, textColor=BLUE)
h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=13, spaceBefore=12, spaceAfter=4, textColor=BLUE)
body = ParagraphStyle("b", parent=styles["Normal"], fontSize=11, leading=15, spaceAfter=6)

story = []


def p(text, style=body):
    story.append(Paragraph(text, style))


def bullets(items):
    flow = [ListItem(Paragraph(t, body)) for t in items]
    story.append(ListFlowable(flow, bulletType="bullet", leftIndent=14, spaceAfter=6))


# Header
p("Python Adventure Game - Project Report", title_style)
p("Course End Project: Building a Python Adventure Game with GitHub Copilot", sub_style)
p("Submitted by: Richard Wagner&nbsp;&nbsp;|&nbsp;&nbsp;Date: June 15, 2026", name_style)
p("Project file: adventure_game.py", sub_style)
p("Tool used: VS Code with the GitHub Copilot extension", sub_style)
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=2, color=LIGHT_BLUE))
story.append(Spacer(1, 8))

# Overview
p("Overview", h2)
p(
    "For this project I built a text based adventure game in Python called "
    "\"The Quest for the Legendary Treasure\". The player is an explorer who is "
    "looking for a treasure. The game asks for the player's name and then gives "
    "them choices to explore a dark forest or a mysterious cave. Each choice "
    "leads to another choice and the game ends in one of three ways: you win by "
    "finding the treasure, you lose by making a bad choice, or you can restart "
    "and play again."
)
p(
    "I split the game into functions like the project asked. start_game() shows "
    "the intro and the first choice, forest_path() and cave_path() handle the two "
    "main areas, and treasure_room() is the ending part. I also made a small "
    "helper called get_choice() so I didn't have to write the same input checking "
    "code over and over."
)

# How Copilot helped
p("How GitHub Copilot Helped", h2)
p("GitHub Copilot helped me a lot while I was writing the code. Here are the main ways it helped:")
bullets([
    "After I wrote a function name and a comment, Copilot would suggest the rest "
    "of the function, like the print statements and the input lines. This saved me "
    "a lot of typing.",
    "It was really good at writing the if/else parts. Once I did the first choice, "
    "it could guess the pattern for the next choices and suggest similar code.",
    "When I had the same input checking code copied in a few places, Copilot helped "
    "me turn it into the get_choice() function so the code was cleaner.",
    "It also helped me come up with some of the story text for the forest and the "
    "cave so I didn't have to think of every sentence myself.",
])

# Challenges
p("Challenges I Faced", h2)
bullets([
    "The hardest part was planning out all the different paths and making sure "
    "every choice actually leads to an ending and not a dead end. I had to draw it "
    "out on paper first before coding it.",
    "At first the game crashed if the player typed something that wasn't an option. "
    "I fixed this with the get_choice() function that keeps asking until you type a "
    "valid answer.",
    "Sometimes Copilot suggested code that looked right but didn't actually fit my "
    "game, like using a variable I hadn't made yet. So I had to read the suggestions "
    "carefully and test them instead of just accepting everything.",
])

# Enhancements
p("Things I Added or Changed", h2)
bullets([
    "I added more than one choice per path so each path has a few decisions instead "
    "of just one.",
    "I used a key (a True/False value) that you can pick up. The treasure_room() "
    "function checks if you have the key to decide what options you get at the end.",
    "I made both paths end in the same treasure_room() function so I didn't repeat "
    "the ending code twice.",
    "I added the get_choice() helper so the game doesn't crash on bad input.",
    "I put the whole game inside a while loop in main() so the player can keep "
    "playing again until they type n.",
])

# Conclusion
p("Conclusion", h2)
p(
    "This project helped me practice Python functions, conditionals, loops and "
    "lists by making something fun. GitHub Copilot made it faster to write the code "
    "because it handled a lot of the repeated parts and gave me suggestions, but I "
    "still had to design the game, fix the bugs, and check that everything worked. "
    "Overall I'm happy with how the game turned out and it would be easy to add more "
    "locations later."
)

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    topMargin=0.9 * inch, bottomMargin=0.9 * inch,
    leftMargin=1 * inch, rightMargin=1 * inch,
)
doc.build(story)
print("Report written to", OUTPUT)
