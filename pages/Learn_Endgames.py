import streamlit as st
import chess
import chess.svg

st.set_page_config(
    page_title="Learn Endgames", 
    layout="wide"
)
 
st.title("Learn Endgames")

LESSONS = {

    "Opposition": {
        "fen": "8/8/8/3k4/8/3K4/8/8 w - - 0 1",

        "highlight": [chess.D5, chess.D3],

        "objective": """
Understand how opposition allows one king to force the other king backward
and gain control of critical squares.
""",

        "text": """
Opposition is one of the most fundamental concepts in chess endgames. It occurs
when the two kings face one another with exactly one square separating them.

In king and pawn endgames, the ability to gain opposition often determines
whether a position is won, drawn, or lost. The side that successfully obtains
the opposition can force the opposing king to move away from important squares.

The concept becomes especially important when helping a pawn toward promotion.
If a king can use opposition to drive the enemy king backward, it often creates
a path for the pawn to advance safely.

Strong endgame players constantly evaluate who controls the opposition and how
it can be used to gain access to key squares.

"""
    },

    "Key Squares": {
        "fen": "8/8/8/8/8/8/4P3/4K3 w - - 0 1",

        "highlight": [
            chess.D4,
            chess.E4,
            chess.F4
        ],

        "objective": """
Learn how key squares determine whether a pawn can promote successfully.
""",

        "text": """
Key squares are special squares that guarantee promotion if the attacking king
can occupy one of them.

For many pawn endgames, calculating dozens of moves is unnecessary if you know
the key squares. Instead, you can immediately determine whether a position is
winning or drawing.

In this example, the highlighted squares represent critical targets for the
white king. If White can successfully place the king on one of these squares,
the pawn will usually be able to advance and promote.

Understanding key squares dramatically improves endgame calculation and helps
players make faster and more accurate decisions in practical games.

Many beginner and intermediate players overlook this concept, but advanced
players use it constantly when evaluating pawn endings.
"""
    },

    "Lucena Position": {
        "fen": "8/2P5/2K5/8/8/8/3R4/3k4 w - - 0 1",

        "highlight": [
            chess.D4,
            chess.D5,
            chess.D6
        ],

        "objective": """
Understand the most important winning technique in rook endgames.
""",

        "text": """
The Lucena Position is considered the most important winning rook endgame.

In this structure, the stronger side has a pawn that has advanced close to
promotion. Although the defending rook can often check repeatedly from the side,
the attacker can construct what is known as a bridge.

The bridge technique uses the rook as a shield to block checks while the king
escapes to safety. Once the king is protected, the pawn can continue advancing
toward promotion.

Because rook endgames occur frequently in practical chess, knowledge of the
Lucena Position is essential for tournament players.

The highlighted squares represent the area where the attacking rook often helps
create the bridge that secures the win.
"""
    },

    "Philidor Defense": {
        "fen": "8/8/3r4/8/3k4/8/3P4/3RK3 w - - 0 1",

        "highlight": [
            chess.D6,
            chess.E6,
            chess.F6
        ],

        "objective": """
Learn the most reliable defensive drawing method in rook endgames.
""",

        "text": """
The Philidor Defense is one of the most important defensive techniques in chess.

While the Lucena Position demonstrates how the stronger side wins, the Philidor
Position demonstrates how the defender can save a difficult game.

The defending rook remains active and prevents the attacking king from making
progress. By controlling critical ranks and files, the defender can force the
attacker into an unfavorable setup.

A player who understands the Philidor Defense can save many positions that might
appear lost to less experienced players.

The highlighted squares indicate the defensive zone that helps prevent the
attacking king from advancing effectively.
"""
    },

    "Triangulation": {
        "fen": "8/8/8/3k4/8/2K5/8/8 w - - 0 1",

        "highlight": [
            chess.C3,
            chess.C4,
            chess.D4
        ],

        "objective": """
Understand how a king can deliberately lose a move to create zugzwang.
""",

        "text": """
Triangulation is a sophisticated king maneuver used in endgames.

Normally, players try to improve their position with every move. In some
endgames, however, the strongest move is to return to a similar position while
changing whose turn it is.

A king can achieve this by moving in a triangular path. After completing the
triangle, the king often arrives back at nearly the same location, but the move
order has changed.

This seemingly simple idea can force the opponent into zugzwang, a situation
where every legal move worsens their position.

Triangulation appears frequently in advanced king and pawn endings and is one
of the clearest demonstrations of how move order can determine the outcome of
an endgame.

The highlighted squares illustrate a common triangular route used to lose a
tempo and place the opponent under pressure.
"""
    }
}

lesson_name = st.selectbox(
    "Select an Endgame Topic",
    list(LESSONS.keys())
)

lesson = LESSONS[lesson_name]
board = chess.Board(lesson["fen"])

# Change highlighted squares to red
fill = {
    square: "#ff6b6b"
    for square in lesson["highlight"]
}

left, right = st.columns([3, 2])

with left:

    svg = chess.svg.board(
        board=board,
        size=700,
        fill=fill
    )

    st.components.v1.html(
        svg,
        height=720
    )

with right:

    st.subheader("Learning Objective")
    st.write(lesson["objective"])

    st.subheader("Explanation")
    st.write(lesson["text"])

st.divider()

st.subheader("Important Squares")

square_names = [
    chess.square_name(square).upper()
    for square in lesson["highlight"]
]

st.write(", ".join(square_names))

st.divider()

st.subheader("Practical Application")

applications = {
    "Opposition":
        "Used to force the enemy king away from critical squares in king and pawn endgames.",

    "Key Squares":
        "Used to determine whether a pawn can promote without calculating long variations.",

    "Lucena Position":
        "Used to convert winning rook endgames into a full point.",

    "Philidor Defense":
        "Used to hold difficult rook endgames and secure a draw.",

    "Triangulation":
        "Used to create zugzwang and gain the opposition through move-order manipulation."
}

st.write(applications[lesson_name])

st.divider()

st.subheader("Reflection Question")

questions = {
    "Opposition":
        "Why does having the move sometimes become a disadvantage in king endgames?",

    "Key Squares":
        "How can key squares help you evaluate a pawn ending without calculating every move?",

    "Lucena Position":
        "Why is the bridge technique necessary for converting many rook endgames?",

    "Philidor Defense":
        "How does an active rook help the defender hold a draw?",

    "Triangulation":
        "Why can deliberately losing a move create a winning opportunity?"
}

st.write(questions[lesson_name])
