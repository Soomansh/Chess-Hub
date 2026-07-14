import streamlit as st

st.title("♟️ Opening Explorer")
st.write("A full chess learning database for openings, ideas, and strategies.")

# -------------------------------------------------------------------------------------------------------------------------------------------
# FULL OPENING DATABASE :>
# ----------------------------------------------------------------------------------------------------------------- -----------------
 
openings = {

# ===========================================================================================================================
# ITALIAN GAME
# ===========================================================================================================================================
"Italian Game": {
    "overview": """
The Italian Game is one of the most fundamental and instructive chess openings ever created.

It appears in thousands of beginner and master games because it follows the most important chess principle:
develop quickly, control the center, and keep your king safe.

The position becomes a mix of strategy and tactics very early, especially around the f7 square.
""",

    "why": """
You play the Italian Game because it teaches you how real chess is supposed to work.

Instead of memorizing long theory, you learn:
- how to develop pieces naturally
- how to coordinate attacks
- how to punish weak squares like f7

It is one of the cleanest ways to learn attacking chess without chaos.
""",

    "idea": """
White builds a quick development advantage while aiming at Black’s weakest early square, f7.

The bishop on c4 creates pressure, the knight controls the center, and White prepares to castle fast.

If Black is slow, White can launch a direct attack very early.
""",

    "plans": """
- Develop knights before moving the queen
- Place bishop on c4 to pressure f7
- Castle early to protect the king
- Prepare d4 to control the center
- Launch attacks only after development is complete
- Keep pieces active and coordinated
""",

    "strengths": """
- Teaches core chess fundamentals in the clearest way possible
- Very natural development flow, so you do not feel lost
- Early attacking ideas appear without needing deep theory
- Strong training opening for tactics and calculation
- Works at beginner and intermediate levels very easily
- Good opening for learning how to punish slow development
""",

    "weaknesses": """
- At higher levels, opponents know how to neutralize early threats
- If you attack too early, you can lose your advantage
- Can become equal if you do not keep playing energetically
- Some lines become tactical very quickly, which can be dangerous
""",

    "mistakes": """
- Bringing the queen out too early instead of developing pieces
- Attacking f7 before completing development
- Ignoring Black’s counterplay in the center
- Moving pawns without a plan
- Forgetting to castle and leaving the king in the middle
""",

    "punishment": """
If White plays the Italian incorrectly, Black can often counter in the center with moves like ...d5.

If White rushes the attack without development, the attack falls apart and Black gets the better position.
""",

    "best_for": "Players who want to learn real attacking chess and strong fundamentals",
    "difficulty": "Easy",
    "moves": "1. e4 e5 2. Nf3 Nc6 3. Bc4",
    "famous_players": "Fischer, Kasparov, Carlsen"
},

# ============================================================================================================================
# VIENNA GAME
# ========================================================================================================================================
"Vienna Game": {
    "overview": """
The Vienna Game is a flexible and creative opening that gives White a lot of freedom.

White does not rush into the center immediately. Instead, White develops quietly and keeps options open for an early attack or a strong center.

That is what makes it dangerous. Black often does not know exactly which plan White will choose.
""",

    "why": """
You choose the Vienna Game when you want flexibility.

It teaches:
- how to attack with f4 ideas
- how to control the center indirectly
- how to choose the right plan instead of forcing one move every game

It is a very useful opening for creative players.
""",

    "idea": """
White develops the knight early and keeps options open.

Later White can push f4 for a kingside attack or play d4 to take over the center.

The opening is built around flexibility, surprise, and good timing.
""",

    "plans": """
- Develop Nc3 quickly
- Prepare f4 for attacking chances
- Push d4 when the center is ready
- Keep the position flexible early
- Attack based on Black’s reaction
- Use piece activity to create pressure
""",

    "strengths": """
- Flexible positions with many choices
- Less theory compared to main openings
- Good surprise weapon in real games
- Can become very aggressive quickly
- Lets White choose between attacking and positional play
""",

    "weaknesses": """
- Not forcing, so you must understand the ideas
- Can become passive if you do nothing
- Less structured than some main openings
- If White delays too much, Black equalizes comfortably
""",

    "mistakes": """
- Playing without a clear plan
- Ignoring the center too long
- Not developing pieces fast enough
- Moving pawns without preparing the attack
""",

    "punishment": """
If White plays too slowly, Black can equalize easily by taking control of the center.

If White does not create pressure, the Vienna becomes just a quiet developing opening.
""",

    "best_for": "Players who like creative and flexible chess",
    "difficulty": "Medium",
    "moves": "1. e4 e5 2. Nc3",
    "famous_players": "Modern grandmasters"
},

# ===============================================================================================================================================================
# SCOTCH GAME
# ===================================================================================================================================================
"Scotch Game": {
    "overview": """
The Scotch Game is one of the most direct openings in chess.

Instead of building slowly, White immediately challenges the center and forces the game to open.

This creates fast development and sharp positions very early in the game.
""",

    "why": """
You choose the Scotch Game when you want action immediately.

It teaches:
- how to open the center at the right moment
- how to use active pieces
- how to calculate early tactics

It is an excellent opening for players who want direct play.
""",

    "idea": """
White pushes d4 early and forces the center open.

This removes central tension quickly and gives both sides open lines for their pieces.

Because the center opens early, tactics become very important.
""",

    "plans": """
- Open the center with d4
- Develop pieces quickly
- Use open lines for attacks
- Target weak central pawns
- Keep the king safe during early tactics
- Use active piece placement from the start
""",

    "strengths": """
- Very active and tactical positions
- Fast development for both sides
- Clear plans in open positions
- Good for learning calculation and tactics
- Often leads to exciting games
""",

    "weaknesses": """
- Requires accurate calculation
- Mistakes are punished immediately
- Can become sharp and risky
- White can lose control of the center if careless
""",

    "mistakes": """
- Losing control of the center too early
- Moving too many pawns instead of pieces
- Ignoring king safety during attacks
- Forgetting that open positions need calculation
""",

    "punishment": """
If White misplays the center, Black takes control quickly and can get the better game.

If White opens the position without enough development, the Scotch becomes dangerous for White.
""",

    "best_for": "Aggressive tactical players who like open positions",
    "difficulty": "Medium",
    "moves": "1. e4 e5 2. Nf3 Nc6 3. d4",
    "famous_players": "Kasparov"
},

# ==========================================================================================================================================
# LONDON SYSTEM
# =================================================================================================================================================
"London System": {
    "overview": """
The London System is a very solid and structured opening system.

It is not based on memorizing sharp lines. Instead, it uses a setup that works against almost everything.

This makes it popular for players who want stability and safety.
""",

    "why": """
You play the London System when you want consistency.

It teaches:
- how to build a strong pawn structure
- how to develop pieces in a safe order
- how to avoid early tactical danger

It is useful for players who want reliable games every time.
""",

    "idea": """
White builds a stable structure with pawns and develops the bishop early.

The position is usually closed or semi-closed, which makes it easier to control.

White slowly improves the position instead of attacking immediately.
""",

    "plans": """
- Build solid pawn structure with d4, e3, and c3 ideas
- Develop bishop to f4 early
- Castle quickly for safety
- Keep structure strong and stable
- Attack later when the position is ready
- Use pieces to slowly increase pressure
""",

    "strengths": """
- Very easy to learn and repeat
- Stable positions in almost every game
- Low risk of early defeat
- Good for learning general chess ideas
- Very useful for players who want comfort and consistency
""",

    "weaknesses": """
- Can become passive if you never attack
- Less tactical chance early
- Strong players can sometimes neutralize it
- If White only sets up and never acts, Black can take the initiative
""",

    "mistakes": """
- No plan after setup
- Never trying to expand or attack
- Ignoring center activity
- Playing too slowly and letting Black get comfortable
""",

    "punishment": """
If White plays too passively, Black can take space in the center and become more active.

The London works best when White keeps the position under control but still looks for activity.
""",

    "best_for": "Beginners who want safe and consistent games",
    "difficulty": "Easy",
    "moves": "1. d4 2. Bf4 3. e3",
    "famous_players": "Carlsen occasionally"
},

# ========================================================================================================================================================
# QUEEN'S GAMBIT
# =============================================================================================================================================================================================
"Queen's Gambit": {
    "overview": """
The Queen’s Gambit is one of the most important positional openings in chess history.

It focuses on long-term central control and strategic planning.

This opening is famous because it teaches you how to pressure the center without rushing.
""",

    "why": """
You play the Queen’s Gambit when you want long-term control.

It teaches:
- how to dominate the center
- how pawn structures affect the game
- how to create pressure slowly and correctly

It is a deep strategic opening and one of the best for improvement.
""",

    "idea": """
White offers a pawn on c4 to gain control of the center.

Even if Black accepts or declines, White aims to dominate central squares and create long-term pressure.

The position often becomes a battle of structure, space, and patience.
""",

    "plans": """
- Control central squares d4 and e5
- Maintain pawn tension in the center
- Develop knights naturally
- Create long-term pressure on d5
- Keep the position flexible
- Use development to support central play
""",

    "strengths": """
- Extremely strong positional foundation
- Used at all levels including top grandmasters
- Teaches deep strategic thinking
- Gives White stable pressure and space
- Helps players learn how to play with long-term plans
""",

    "weaknesses": """
- Slower attacking chances
- Requires positional understanding
- Less immediate tactics than open games
- If played too passively, White’s pressure can disappear
""",

    "mistakes": """
- Trading pawns too early without reason
- Ignoring central tension
- Playing without long-term plan
- Developing pieces without supporting the center
""",

    "punishment": """
If White misplays, Black can equalize and remove White’s space advantage.

If White does not keep the center active, the Queen’s Gambit becomes much less powerful.
""",

    "best_for": "Positional and strategic players",
    "difficulty": "Medium",
    "moves": "1. d4 d5 2. c4",
    "famous_players": "Carlsen, Karpov"
},

# ===========================================================================================================================
# SICILIAN DEFENSE
# =============================================================================================================================================================================================
"Sicilian Defense": {
    "overview": """
The Sicilian Defense is the most aggressive and complex defense against 1.e4.

Instead of copying White, Black immediately creates imbalance and fights for winning chances.

This is one of the main reasons it is so popular at high levels.
""",

    "why": """
You choose the Sicilian because you want to win with Black, not just survive.

It creates sharp positions where both sides must think carefully from the start.

It is one of the best openings for players who want fighting chess.
""",

    "idea": """
Black plays c5 to fight the center indirectly.

This creates asymmetrical positions where both sides have different plans.

The position becomes tactical and flexible at the same time.
""",

    "plans": """
- Fight the center with c5 immediately
- Avoid symmetrical positions
- Create imbalance early
- Counterattack on the queenside
- Punish slow development from White
- Use active pieces instead of passive defense
""",

    "strengths": """
- Extremely sharp and dynamic
- High winning chances for Black
- Used at top professional level
- Creates complex middlegames
- Forces White to think carefully from the first moves
""",

    "weaknesses": """
- Heavy theory required
- Very sharp and risky positions
- One mistake can lose the game quickly
- Hard to learn deeply without practice
""",

    "mistakes": """
- Playing passive moves
- Ignoring development
- Not knowing basic theory ideas
- Allowing White full control of the center
""",

    "punishment": """
If Black misplays, White gets a strong center and attacking initiative quickly.

The Sicilian is powerful, but if Black is careless, White can take over the game.
""",

    "best_for": "Aggressive counterattacking players",
    "difficulty": "Hard",
    "moves": "1. e4 c5",
    "famous_players": "Fischer, Kasparov"
},

# =========================================================================================================================================
# CARO-KANN DEFENSE
# ===========================================================================================================================
"Caro-Kann Defense": {
    "overview": """
The Caro-Kann Defense is one of the most solid and reliable defenses in chess.

Black builds a strong structure and avoids early weaknesses while preparing a stable counterattack.

It is one of the best choices for players who want safety without becoming weak.
""",

    "why": """
You play the Caro-Kann because you want a safe but strong position with Black.

It teaches:
- how to build a hard-to-break pawn structure
- how to defend patiently
- how to punish overextension

This opening is very practical and very stable.
""",

    "idea": """
Black immediately supports the center with c6 and d5, creating a strong pawn structure.

Unlike aggressive gambits, Black does not rush attacks. Instead, Black waits for the right moment to strike back.

The goal is to absorb White’s center and then punish weakness later.
""",

    "plans": """
- Build a strong pawn chain with c6 and d5
- Challenge White’s center early
- Develop safely behind the structure
- Wait for White to overextend
- Counterattack once the center becomes weak
- Keep your position solid and difficult to break
""",

    "strengths": """
- Extremely solid and hard to break
- Strong pawn structure that protects key squares
- Low risk of early losing positions
- Excellent for learning defensive technique
- Very reliable in real games
- Good opening for practical tournament play
""",

    "weaknesses": """
- Less aggressive than other defenses
- Can feel slow or passive if you do not counterattack
- Requires patience before activity appears
- Sometimes White can get easy space if Black is too quiet
""",

    "mistakes": """
- Playing too passively without counterplay
- Ignoring White’s central expansion
- Developing pieces without supporting the center
- Never challenging White’s pawn structure
- Forgetting to look for active breaks later
""",

    "punishment": """
If Black plays the Caro-Kann incorrectly, White can slowly build a strong center and space advantage.

The opening works best when Black stays solid but still watches for active counterplay.
""",

    "best_for": "Players who want safe and structured Black games",
    "difficulty": "Medium",
    "moves": "1. e4 c6 2. d4 d5",
    "famous_players": "Carlsen, Karpov"
},

# ===================================================================================================================================
# FRENCH DEFENSE
# ======================================================================================================================================
"French Defense": {
    "overview": """
The French Defense is a strategic opening built around a strong pawn chain.

It creates counterattacking chances in a closed structure, which means the battle is often about timing and pawn breaks rather than quick tactics.
""",

    "why": """
You play the French Defense because you want a position where structure matters more than immediate attacks.

It teaches:
- how to build a strong pawn chain
- how to attack the center later
- how to play patient defensive chess with a purpose

It is a classic strategic defense.
""",

    "idea": """
Black builds a pawn chain and then tries to break the center later with moves like c5 or f6.

White usually gets more space early, but Black gets a solid shape that can become very powerful if timed correctly.
""",

    "plans": """
- Build the pawn chain with e6 and d5
- Break the center later with c5
- Watch for White’s overextension
- Develop pieces behind the pawn chain
- Keep the position under control
- Counterattack when the center becomes weak
""",

    "strengths": """
- Strong and reliable structure
- Good counterplay if played correctly
- Strategic depth and long-term ideas
- Very useful for learning closed positions
- Can become strong in the middlegame
""",

    "weaknesses": """
- Can feel cramped if Black is passive
- Requires good timing
- White can sometimes use space advantage
- If Black never breaks the center, the position becomes uncomfortable
""",

    "mistakes": """
- Passive development behind the pawn chain
- No counterattack plan
- Incorrect timing on c5 or f6
- Letting White attack freely without response
""",

    "punishment": """
If Black misplays, White can use the space advantage to attack before Black becomes active.

The French is strong, but only if Black knows when to break the center.
""",

    "best_for": "Strategic Black players",
    "difficulty": "Medium",
    "moves": "1. e4 e6 2. d4 d5",
    "famous_players": "Botvinnik"
},

# =============================================================================================================================
# KING'S INDIAN DEFENSE
# ==============================================================================================================================
"King's Indian Defense": {
    "overview": """
The King’s Indian Defense is a hypermodern and aggressive defense for Black.

Black allows White to build a center and then attacks it later with strong counterplay.

This opening is famous for wild, sharp middlegames where both sides often attack.
""",

    "why": """
You play the King’s Indian because you want sharp, fighting chess with Black.

It teaches:
- how to allow space but remain dangerous
- how to counterattack at the right moment
- how to launch kingside attacks

It is one of the most exciting defenses in chess.
""",

    "idea": """
Black fianchettoes the bishop and prepares to hit White’s center later.

White often gets more space early, but Black tries to turn that space into a target by attacking it with pawn breaks and piece pressure.
""",

    "plans": """
- Fianchetto bishop on g7
- Castle early
- Attack the center later with pawn breaks
- Use kingside pressure
- Keep pieces ready for counterattack
- Strike when White overextends
""",

    "strengths": """
- Very aggressive and dynamic
- Strong counterplay chances
- Creates exciting positions
- Great for players who like tactical battles
- Can become dangerous very quickly
""",

    "weaknesses": """
- White gets space early
- Requires good timing
- Risky positions if Black attacks too soon
- Not ideal for players who want calm games
""",

    "mistakes": """
- Early attacks without preparation
- Ignoring center pressure
- Slow development
- Starting the attack before the position is ready
""",

    "punishment": """
If Black plays the King’s Indian badly, White can use the space advantage to build a strong attack.

The opening works best when Black stays patient and strikes at the right moment.
""",

    "best_for": "Aggressive counterattacking players",
    "difficulty": "Hard",
    "moves": "1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6",
    "famous_players": "Kasparov, Nakamura"
},

# ===========================================================================================================================================
# PIRC DEFENSE
# ===================================================================================================================================
"Pirc Defense": {
    "overview": """
The Pirc Defense is a flexible hypermodern opening for Black.

Black allows White to take space early and then tries to challenge the center later.

It is less forcing than the King’s Indian, but it gives Black freedom.
""",

    "why": """
You play the Pirc Defense when you want a flexible counterattacking game.

It teaches:
- patience
- flexible development
- how to strike the center at the right time

It is a good choice for creative players.
""",

    "idea": """
Black develops slowly and prepares counterplay against White’s center later.

Instead of challenging early with pawns, Black waits and uses piece placement to stay active.
""",

    "plans": """
- Develop pieces flexibly
- Castle early
- Allow White to build center
- Attack the center later
- Avoid passive positions
- Keep the board open for counterplay
""",

    "strengths": """
- Very flexible
- Creative counterattacking chances
- Can surprise opponents
- Good for players who like dynamic structures
- Less rigid than some defenses
""",

    "weaknesses": """
- White gets space early
- Requires patience
- Can become passive if Black waits too long
- Needs good understanding of timing
""",

    "mistakes": """
- Delaying counterattack too long
- Passive development
- Ignoring White’s central control
- Waiting without a plan
""",

    "punishment": """
If Black is too slow, White can build a huge center and take control of the game.

The Pirc works best when Black stays flexible but active.
""",

    "best_for": "Creative Black players",
    "difficulty": "Medium",
    "moves": "1. e4 d6 2. d4 Nf6",
    "famous_players": "Modern grandmasters"
}

}

# --------------------------------------------------------------------------------------------------------------------------------------------
# UI
# --------------------------------------------------------------------------------------------------------------------------------

opening = st.selectbox("Choose an opening", list(openings.keys()))
data = openings[opening]

st.subheader(opening)

st.markdown("### Overview")
st.write(data.get("overview", "No overview available."))

st.markdown("### Why play this opening?")
st.write(data.get("why", "No explanation available."))

st.markdown("### Core Idea")
st.write(data.get("idea", "No idea explanation available."))

st.markdown("### Plans (How you actually play it)")
st.write(data.get("plans", "No plans available."))

st.markdown("### Strengths")
st.write(data.get("strengths", "No strengths listed."))

st.markdown("### Weaknesses")
st.write(data.get("weaknesses", "No weaknesses listed."))

st.markdown("### Common Mistakes")
st.write(data.get("mistakes", "No mistakes listed."))

st.markdown("### Best For")
st.write(data.get("best_for", "No info available."))

st.markdown("### Difficulty")
st.write(data.get("difficulty", "Unknown"))

st.markdown("### Example Moves")
st.code(data.get("moves", "No moves available"))

st.markdown("### Famous Players")
st.write(data.get("famous_players", "Not listed"))
