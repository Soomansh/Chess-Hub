"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { Chess, type Move, type Square } from "chess.js";
import { Chessboard } from "react-chessboard";

type ToolId =
  | "home" | "opening-explorer" | "chess-quiz" | "guess-elo"
  | "board-visualizer" | "play-ai" | "chess-review"
  | "puzzles" | "learn-endgames";

type Opening = {
  name: string; side: string; level: string; style: string; moves: string[];
  overview: string; plans: string[]; strengths: string[]; weaknesses: string[];
};

const NAV: { id: ToolId; label: string; icon: string; group: string }[] = [
  { id: "home", label: "Home", icon: "⌂", group: "Workspace" },
  { id: "opening-explorer", label: "Opening Explorer", icon: "♞", group: "Learn" },
  { id: "chess-quiz", label: "Opening Quiz", icon: "✦", group: "Learn" },
  { id: "guess-elo", label: "Guess The Elo", icon: "◎", group: "Play" },
  { id: "board-visualizer", label: "Board Visualizer", icon: "▦", group: "Play" },
  { id: "play-ai", label: "Play vs AI", icon: "⚔", group: "Play" },
  { id: "chess-review", label: "Chess Review", icon: "⌁", group: "Analyze" },
  { id: "puzzles", label: "Endgame Puzzles", icon: "♜", group: "Train" },
  { id: "learn-endgames", label: "Learn Endgames", icon: "◈", group: "Train" },
];

const OPENINGS: Opening[] = [
  { name: "Italian Game", side: "White", level: "Easy", style: "Attacking", moves: ["e4","e5","Nf3","Nc6","Bc4","Bc5","c3","Nf6","d4","exd4"], overview: "A classical opening built around rapid development, central control, and pressure on the f7-square. It is an excellent place to learn sound attacking fundamentals.", plans: ["Develop the kingside pieces quickly","Prepare d4 when the center is ready","Castle early and coordinate the rooks","Use c3 to support a central d4 push"], strengths: ["Natural development","Clear attacking plans","Useful at every rating"], weaknesses: ["Black can counterattack in the center","Premature attacks can backfire"] },
  { name: "Vienna Game", side: "White", level: "Medium", style: "Flexible", moves: ["e4","e5","Nc3","Nf6","f4","d5","fxe5","Nxe4"], overview: "A flexible 1.e4 opening that can lead to aggressive kingside play or a central fight. White keeps several plans available.", plans: ["Develop the knight to c3","Consider f4 when tactically sound","Prepare d4 to challenge the center"], strengths: ["Creative attacking chances","Flexible move orders"], weaknesses: ["Can neglect central control","Requires good timing"] },
  { name: "Scotch Game", side: "White", level: "Medium", style: "Open and tactical", moves: ["e4","e5","Nf3","Nc6","d4","exd4","Nxd4","Bc5"], overview: "White challenges the center early and opens lines for active piece play. Open positions reward calculation and development.", plans: ["Open the center with d4","Develop pieces with tempo","Target central weaknesses"], strengths: ["Direct development","Open tactical positions"], weaknesses: ["Early exchanges can help Black equalize","Tactics matter immediately"] },
  { name: "London System", side: "White", level: "Easy", style: "Positional", moves: ["d4","d5","Bf4","Nf6","e3","c5","c3","Nc6"], overview: "A reliable setup based on d4, Bf4, e3, and c3. White develops in a familiar structure before choosing a middlegame plan.", plans: ["Develop the light-squared bishop to f4","Support the center with e3 and c3","Develop Nf3 and castle","Choose a kingside or central plan based on Black's setup"], strengths: ["Consistent setup","Good strategic practice"], weaknesses: ["Can become passive without a plan","Black can challenge the center early"] },
  { name: "Queen's Gambit", side: "White", level: "Medium", style: "Positional", moves: ["d4","d5","c4","e6","Nc3","Nf6","Bg5","Be7"], overview: "White offers a flank pawn to challenge Black's central pawn on d5. The opening teaches central control, development, and long-term pressure.", plans: ["Challenge the d5-pawn with c4","Develop knights and bishops","Build pressure on the center"], strengths: ["Strong central influence","Rich strategic positions"], weaknesses: ["Requires patience","Some lines involve precise pawn structures"] },
  { name: "Sicilian Defense", side: "Black", level: "Advanced", style: "Counterattacking", moves: ["e4","c5","Nf3","d6","d4","cxd4","Nxd4","Nf6"], overview: "Black fights for the center asymmetrically and often creates counterplay on the queenside. It can lead to sharp, unbalanced games.", plans: ["Challenge White's center with ...c5","Develop actively and watch d4","Look for queenside counterplay"], strengths: ["Winning chances with Black","Dynamic positions"], weaknesses: ["Large amount of theory","Can be tactically demanding"] },
  { name: "Caro-Kann Defense", side: "Black", level: "Easy", style: "Solid", moves: ["e4","c6","d4","d5","Nc3","dxe4","Nxe4","Bf5"], overview: "A sturdy response to 1.e4. Black prepares ...d5 and often aims for a sound pawn structure and reliable development.", plans: ["Prepare ...d5 with ...c6","Develop the light-squared bishop actively","Finish development before counterattacking"], strengths: ["Solid structure","Clear defensive ideas"], weaknesses: ["Can be cramped in some lines","Needs accurate piece development"] },
  { name: "French Defense", side: "Black", level: "Medium", style: "Counterattacking", moves: ["e4","e6","d4","d5","Nc3","Nf6","Bg5","Be7"], overview: "Black challenges White's center with ...d5 and often counterattacks against the pawn chain. Understanding pawn breaks is essential.", plans: ["Challenge the center with ...d5","Prepare ...c5","Develop the light-squared bishop carefully"], strengths: ["Clear counterplay","Strong central structure"], weaknesses: ["Light-squared bishop may be restricted","Pawn chains need accurate handling"] },
  { name: "King's Indian Defense", side: "Black", level: "Advanced", style: "Aggressive", moves: ["d4","Nf6","c4","g6","Nc3","Bg7","e4","d6"], overview: "Black allows White a broad center, then aims to undermine it with ...e5 or ...c5 and often attack on the kingside.", plans: ["Fianchetto the bishop on g7","Challenge the center at the right moment","Coordinate a kingside attack"], strengths: ["Dynamic attacking play","Rich strategic themes"], weaknesses: ["Space disadvantage can be uncomfortable","Requires timing and calculation"] },
  { name: "Pirc Defense", side: "Black", level: "Medium", style: "Hypermodern", moves: ["e4","d6","d4","Nf6","Nc3","g6","Nf3","Bg7"], overview: "Black develops flexibly and pressures White's center from a distance. It is a hypermodern approach that invites White to advance pawns.", plans: ["Fianchetto the bishop","Pressure the center with pieces","Choose ...e5 or ...c5 when ready"], strengths: ["Flexible setup","Counterattacking chances"], weaknesses: ["White may gain a large center","Requires good positional judgment"] },
];

const LESSONS = [
  { name: "Opposition", fen: "8/8/8/3k4/8/3K4/8/8 w - - 0 1", objective: "Use king opposition to gain access to critical squares.", text: "Opposition occurs when kings face one another with one square between them. In king-and-pawn endings, the side that gains the opposition can often force the opposing king away from important squares." },
  { name: "Key Squares", fen: "8/8/8/8/8/8/4P3/4K3 w - - 0 1", objective: "Recognize squares that help a pawn promote.", text: "Key squares are squares the attacking king needs to reach to force promotion. Knowing them can save you from calculating every possible line." },
  { name: "Lucena Position", fen: "8/2P5/2K5/8/8/8/3R4/3k4 w - - 0 1", objective: "Understand the rook-bridge winning technique.", text: "In the classic Lucena technique, the attacking side uses the rook as a shield against checks so the king can escape and the pawn can promote. Real positions require careful move-order calculation." },
  { name: "Philidor Defense", fen: "8/8/3r4/8/3k4/8/3P4/3RK3 w - - 0 1", objective: "Learn a key defensive idea in rook endgames.", text: "The Philidor setup uses an active rook and rank control to prevent the stronger side from making progress. Exact drawing methods depend on the position." },
  { name: "Triangulation", fen: "8/8/8/3k4/8/2K5/8/8 w - - 0 1", objective: "Understand how to lose a tempo deliberately.", text: "Triangulation returns a king to a similar position with the move order changed. This can force the opponent into zugzwang, where any legal move worsens their position." },
];

function parseUci(game: Chess, uci: string): Move | null {
  const from = uci.slice(0, 2) as Square;
  const to = uci.slice(2, 4) as Square;
  const promotion = uci.slice(4, 5) as "q" | "r" | "b" | "n" | "";
  try { return game.move({ from, to, ...(promotion ? { promotion } : {}) }); } catch { return null; }
}
function makeGame(fen?: string) { return fen ? new Chess(fen) : new Chess(); }
function classifyLoss(loss: number | null) {
  if (loss === null) return { label: "NOT RATED", tone: "muted" };
  if (loss <= 5) return { label: "BEST", tone: "good" };
  if (loss <= 20) return { label: "EXCELLENT", tone: "good" };
  if (loss <= 50) return { label: "GREAT", tone: "good" };
  if (loss <= 100) return { label: "GOOD", tone: "muted" };
  if (loss <= 200) return { label: "INACCURACY", tone: "warn" };
  if (loss <= 400) return { label: "MISTAKE", tone: "warn" };
  return { label: "BLUNDER", tone: "bad" };
}
function cpFromData(data: any): number | null {
  const line = data?.pvs?.[0];
  if (!line) return null;
  if (typeof line.cp === "number") return line.cp;
  if (typeof line.mate === "number") return line.mate > 0 ? 1000 : -1000;
  return null;
}
async function cloudEval(fen: string) {
  const response = await fetch(`/api/cloud-eval?fen=${encodeURIComponent(fen)}`);
  if (!response.ok) return null;
  return response.json();
}

function ChessBoard({ fen, width = 520, orientation = "white", onDrop, disabled = false, lightColor = "#e8e8d9", darkColor = "#77966d" }: {
  fen: string; width?: number; orientation?: "white" | "black";
  onDrop?: (source: string, target: string) => boolean; disabled?: boolean;
  lightColor?: string; darkColor?: string;
}) {
  const onPieceDrop = useCallback(({ sourceSquare, targetSquare }: { sourceSquare: string; targetSquare: string | null }) => {
    if (!targetSquare || disabled || !onDrop) return false;
    return onDrop(sourceSquare, targetSquare);
  }, [disabled, onDrop]);
  return <div className="board-wrap" style={{ width: Math.min(width, 620), maxWidth: "100%", margin: "0 auto" }}>
    <Chessboard options={{
      position: fen,
      boardOrientation: orientation,
      allowDragging: !disabled && Boolean(onDrop),
      onPieceDrop,
      darkSquareStyle: { backgroundColor: darkColor },
      lightSquareStyle: { backgroundColor: lightColor },
      animationDurationInMs: 140,
    }} />
  </div>;
}

export default function ChessHub() {
  const [tool, setTool] = useState<ToolId>("home");
  const [mobileMenu, setMobileMenu] = useState(false);
  const current = NAV.find(n => n.id === tool) ?? NAV[0];
  return <div className="shell">
    <header className="topbar">
      <a className="brand" href="#" onClick={(e) => { e.preventDefault(); setTool("home"); }}>
        <span className="brand-mark">♞</span><span>ChessHub</span>
      </a>
      
    </header>
    <div className="layout">
      <aside className="sidebar">
        {["Workspace", "Learn", "Play", "Analyze", "Train"].map(group => <div key={group}>
          <div className="nav-label">{group}</div>
          {NAV.filter(n => n.group === group).map(n => <button key={n.id} className={`nav-button ${tool === n.id ? "active" : ""}`} onClick={() => { setTool(n.id); setMobileMenu(false); }}>
            <span className="nav-icon">{n.icon}</span>{n.label}
          </button>)}
        </div>)}
      </aside>
      <main className="main">
        {tool === "home" && <Home onOpen={setTool} />}
        {tool === "opening-explorer" && <OpeningExplorer />}
        {tool === "chess-quiz" && <ChessQuiz onOpen={setTool} />}
        {tool === "guess-elo" && <GuessElo />}
        {tool === "board-visualizer" && <BoardVisualizer />}
        {tool === "play-ai" && <PlayAI />}
        {tool === "chess-review" && <ChessReview />}
        {tool === "puzzles" && <PuzzleTrainer />}
        {tool === "learn-endgames" && <LearnEndgames />}

      </main>
    </div>
  </div>;
}

function Home({ onOpen }: { onOpen: (id: ToolId) => void }) {
  const cards: { id: ToolId; icon: string; title: string; desc: string; group: string }[] = [
    { id: "opening-explorer", icon: "♞", title: "Opening Explorer", desc: "Explore plans, strengths, weaknesses, and sample move lines.", group: "LEARN" },
    { id: "chess-quiz", icon: "✦", title: "Opening Quiz", desc: "Find openings that match your style, risk tolerance, and level.", group: "LEARN" },
    { id: "guess-elo", icon: "◎", title: "Guess The Elo", desc: "Review a real game and guess the players' rating range.", group: "PLAY" },
    { id: "board-visualizer", icon: "▦", title: "Board Visualizer", desc: "Step through opening lines on an interactive chessboard.", group: "PLAY" },
    { id: "play-ai", icon: "⚔", title: "Play vs AI", desc: "Play a game against the computer.", group: "PLAY" },
    { id: "chess-review", icon: "⌁", title: "Chess Review", desc: "Review a game from a PGN file or pasted moves.", group: "ANALYZE" },
    { id: "puzzles", icon: "♜", title: "Endgame Puzzles", desc: "Practice tactics from the included puzzle collection.", group: "TRAIN" },
    { id: "learn-endgames", icon: "◈", title: "Learn Endgames", desc: "Study opposition, key squares, and rook endgame concepts.", group: "TRAIN" },
  ];
  return <>
    <section className="hero">
      <div className="hero-mark">♞</div>
      <div className="hero-content">
        
        <h1>ChessHub</h1>
        <p className="lead">Explore openings, practice positions, solve puzzles, and review your games.</p>
        <div className="button-row"><button className="btn primary" onClick={() => onOpen("chess-review")}>Review a game ↗</button><button className="btn" onClick={() => onOpen("guess-elo")}>Play Guess The Elo</button></div>
      </div>
    </section>
    <div className="section-head"><h2>Chess tools</h2></div>
    <div className="grid">{cards.map(c => <button className="tool-card" key={c.id} onClick={() => onOpen(c.id)}>
      <div className="card-icon">{c.icon}</div><div className="eyebrow">{c.group}</div><h3>{c.title}</h3><p>{c.desc}</p><span className="card-link">Open →</span>
    </button>)}</div>
  </>;
}

function OpeningExplorer() {
  const [name, setName] = useState(OPENINGS[0].name);
  const [step, setStep] = useState(0);
  const opening = OPENINGS.find(o => o.name === name) ?? OPENINGS[0];
  const fen = useMemo(() => {
    const g = new Chess();
    try { opening.moves.slice(0, step).forEach(m => g.move(m)); } catch {}
    return g.fen();
  }, [opening, step]);
  const movePairs = opening.moves.reduce<string[]>((arr, m, i) => { const n = Math.floor(i / 2) + 1; if (i % 2 === 0) arr.push(`${n}. ${m}`); else arr[arr.length - 1] += ` ${m}`; return arr; }, []);
  return <>
    <div className="eyebrow">LEARN / OPENINGS</div><h1>Opening Explorer</h1><p className="lead">Understand the ideas behind common openings—not just the moves.</p>
    <div className="columns"><section className="panel">
      <div className="field"><label>Choose an opening</label><select value={name} onChange={e => { setName(e.target.value); setStep(0); }}>{OPENINGS.map(o => <option key={o.name}>{o.name}</option>)}</select></div>
      <div className="board-caption"><span>{opening.side} · {opening.level}</span><span>Move {step}/{opening.moves.length}</span></div>
      <ChessBoard fen={fen} />
      <div className="button-row"><button className="btn" disabled={step === 0} onClick={() => setStep(s => Math.max(0, s - 1))}>← Previous</button><button className="btn primary" disabled={step >= opening.moves.length} onClick={() => setStep(s => Math.min(opening.moves.length, s + 1))}>Next move →</button><button className="btn" onClick={() => setStep(0)}>Reset</button></div>
      <div className="section-head"><h3>Sample line</h3></div><div className="move-list">{movePairs.map((m, i) => <button className={`move-chip ${step > i*2 ? "selected" : ""}`} key={m} onClick={() => setStep(Math.min(opening.moves.length, i*2+1))}>{m}</button>)}</div>
    </section><section className="panel">
      <span className="tag">{opening.style}</span><h2 style={{marginTop:14}}>{opening.name}</h2><p className="muted">{opening.overview}</p>
      <h3>Plans to remember</h3><ul className="list">{opening.plans.map(x => <li key={x}>{x}</li>)}</ul>
      <h3>Strengths</h3><ul className="list">{opening.strengths.map(x => <li key={x}>{x}</li>)}</ul>
      <h3>Watch out for</h3><ul className="list">{opening.weaknesses.map(x => <li key={x}>{x}</li>)}</ul>
    </section></div>
  </>;
}

function ChessQuiz({ onOpen }: { onOpen: (id: ToolId) => void }) {
  const [skill, setSkill] = useState("Intermediate"), [style, setStyle] = useState("Positional"), [color, setColor] = useState("White");
  const [aggression, setAggression] = useState(5), [time, setTime] = useState("Rapid"), [risk, setRisk] = useState("Medium"), [goal, setGoal] = useState("Strategy"), [show, setShow] = useState(false);
  const results = useMemo(() => {
    const scores: Record<string, number> = { "Italian Game": 0, "Queen's Gambit": 0, "Sicilian Defense": 0, "Scotch Game": 0, "Vienna Game": 0, "Caro-Kann Defense": 0, "French Defense": 0 };
    if (aggression >= 7) { scores["Italian Game"] += 3; scores["Scotch Game"] += 3; scores["Sicilian Defense"] += 3; scores["Vienna Game"] += 2; }
    else if (aggression >= 4) { scores["Queen's Gambit"] += 3; scores["Italian Game"] += 2; scores["Vienna Game"] += 2; }
    else scores["Queen's Gambit"] += 3;
    if (risk === "High") { scores["Sicilian Defense"] += 2; scores["Scotch Game"] += 2; }
    if (risk === "Low") { scores["Queen's Gambit"] += 2; scores["Italian Game"] += 1; scores["Caro-Kann Defense"] += 2; }
    if (style === "Defensive") { scores["Queen's Gambit"] += 2; scores["Caro-Kann Defense"] += 2; }
    if (style === "Aggressive") { scores["Sicilian Defense"] += 2; scores["Scotch Game"] += 2; }
    if (color === "White") { scores["Italian Game"] += 2; scores["Queen's Gambit"] += 2; }
    else { scores["Sicilian Defense"] += 2; scores["Caro-Kann Defense"] += 2; scores["French Defense"] += 2; }
    if (skill === "Beginner") { scores["Italian Game"] += 2; scores["Caro-Kann Defense"] += 1; }
    if (skill === "Advanced") { scores["Sicilian Defense"] += 2; scores["French Defense"] += 1; }
    if (goal === "Tactics") { scores["Scotch Game"] += 2; scores["Sicilian Defense"] += 1; }
    if (goal === "Endgames") scores["Queen's Gambit"] += 2;
    if (time === "Bullet") scores["Italian Game"] += 1;
    return Object.entries(scores).sort((a,b) => b[1]-a[1]).slice(0,3);
  }, [skill, style, color, aggression, time, risk, goal]);
  return <>
    <div className="eyebrow">LEARN / PERSONALIZED</div><h1>Opening Quiz</h1><p className="lead">Answer a few questions and get a practical shortlist of openings to explore.</p>
    <div className="columns"><section className="panel">
      <div className="grid two">
        <div className="field"><label>Skill level</label><select value={skill} onChange={e=>setSkill(e.target.value)}>{["Beginner","Intermediate","Advanced"].map(x=><option key={x}>{x}</option>)}</select></div>
        <div className="field"><label>Play style</label><select value={style} onChange={e=>setStyle(e.target.value)}>{["Defensive","Positional","Aggressive"].map(x=><option key={x}>{x}</option>)}</select></div>
        <div className="field"><label>Color</label><select value={color} onChange={e=>setColor(e.target.value)}>{["White","Black"].map(x=><option key={x}>{x}</option>)}</select></div>
        <div className="field"><label>Time control</label><select value={time} onChange={e=>setTime(e.target.value)}>{["Bullet","Blitz","Rapid","Classical"].map(x=><option key={x}>{x}</option>)}</select></div>
        <div className="field"><label>Risk preference</label><select value={risk} onChange={e=>setRisk(e.target.value)}>{["Low","Medium","High"].map(x=><option key={x}>{x}</option>)}</select></div>
        <div className="field"><label>Main goal</label><select value={goal} onChange={e=>setGoal(e.target.value)}>{["Tactics","Strategy","Endgames","Opening knowledge"].map(x=><option key={x}>{x}</option>)}</select></div>
      </div>
      <div className="field"><label>Aggression: {aggression}/10</label><input type="range" min="0" max="10" value={aggression} onChange={e=>setAggression(Number(e.target.value))}/></div>
      <button className="btn primary" onClick={()=>setShow(true)}>Get recommendations</button>
    </section><section className="panel">
      <div className="eyebrow">YOUR MATCHES</div><h2>Recommended openings</h2>
      {!show ? <p className="muted">Complete the quiz and click the button to see your results.</p> : results.map(([name, score], i) => <div className="tool-card" style={{marginBottom:10}} key={name}><span className="tag">MATCH {i+1}</span><h3 style={{marginTop:10}}>{name}</h3><p>{OPENINGS.find(o=>o.name===name)?.overview}</p><button className="btn" onClick={()=>onOpen("opening-explorer")}>Explore openings ↗</button></div>)}
      
    </section></div>
  </>;
}

let gamesPgnCache: string | null = null;
let gamesPgnChunks: string[] | null = null;
type EloGame = { pgn: string; moves: string[]; avg: number; white: number; black: number; opening: string; result: string; event: string; time: string };
function GuessElo() {
  const [gameData, setGameData] = useState<EloGame | null>(null), [loading, setLoading] = useState(false), [error, setError] = useState("");
  const [moveIndex, setMoveIndex] = useState(0), [guess, setGuess] = useState("1200-1600"), [revealed, setRevealed] = useState(false);
  const [score, setScore] = useState(0), [questions, setQuestions] = useState(0);
  const loadGame = useCallback(async () => {
    setLoading(true); setError(""); setRevealed(false); setMoveIndex(0);
    try {
      let text = gamesPgnCache;
      if (!text) {
        const response = await fetch("/data/games.pgn");
        if (!response.ok) throw new Error("Could not load the included PGN dataset.");
        text = await response.text();
        gamesPgnCache = text;
      }
      if (!gamesPgnChunks) gamesPgnChunks = text.split(/(?=\[Event\s)/).filter(x => /^\[Event\s/m.test(x));
      const chunks = gamesPgnChunks;
      const candidates = chunks.length > 8000 ? Array.from({length:8000},()=>chunks[Math.floor(Math.random()*chunks.length)]) : chunks;
      let selected: EloGame | null = null;
      for (let attempt=0; attempt<Math.min(100,candidates.length); attempt++) {
        const pgn = candidates[Math.floor(Math.random()*candidates.length)];
        const header = (key: string) => pgn.match(new RegExp('^\\[' + key + '\\s+"([^"]*)"\\]', "m"))?.[1] ?? "";
        const white = Number(header("WhiteElo")), black = Number(header("BlackElo"));
        if (!white || !black) continue;
        try {
          const g = new Chess(); g.loadPgn(pgn);
          const moves = g.history();
          if (moves.length < 10) continue;
          selected = { pgn, moves, white, black, avg: Math.floor((white+black)/2), opening:header("Opening")||"Unknown", result:header("Result")||"*", event:header("Event")||"Unknown", time:header("TimeControl")||"Unknown" };
          break;
        } catch {}
      }
      if (!selected) throw new Error("No suitable rated game was found. Try loading a new game.");
      setGameData(selected);
    } catch (e) { setError(e instanceof Error ? e.message : "Could not load a game."); }
    finally { setLoading(false); }
  }, []);
  useEffect(() => { void loadGame(); }, [loadGame]);
  const fen = useMemo(() => { const g = new Chess(); if (gameData) gameData.moves.slice(0,moveIndex).forEach(m=>{try{g.move(m)}catch{}}); return g.fen(); }, [gameData,moveIndex]);
  const bucket = (elo:number) => elo<800?"400-800":elo<1200?"800-1200":elo<1600?"1200-1600":elo<2000?"1600-2000":"2000+";
  const timeType = (raw:string) => { const base=Number(raw.split("+")[0]); return !Number.isFinite(base)?"Unknown":base<180?"Bullet":base<600?"Blitz":base<1800?"Rapid":"Classical"; };
  return <>
    <div className="eyebrow">PLAY / CHALLENGE</div><h1>Guess The Elo</h1><p className="lead">Watch a game unfold, study the moves, then estimate the players' rating range.</p>
    {error && <div className="notice error">{error} <button className="btn" onClick={()=>void loadGame()}>Retry</button></div>}
    {loading && <div className="notice">Loading a game from the included PGN dataset… the first load may take a moment.</div>}
    {gameData && <div className="columns"><section className="panel">
      <div className="board-caption"><span>GAME REPLAY</span><span>{moveIndex} / {gameData.moves.length} plies</span></div>
      <ChessBoard fen={fen} />
      <div className="button-row"><button className="btn" onClick={()=>setMoveIndex(0)}>« Start</button><button className="btn" onClick={()=>setMoveIndex(i=>Math.max(0,i-1))}>← Prev</button><button className="btn primary" onClick={()=>setMoveIndex(i=>Math.min(gameData.moves.length,i+1))}>Next →</button><button className="btn" onClick={()=>setMoveIndex(gameData.moves.length)}>End »</button></div>
      <div className="board-caption"><span>MOVE LIST</span><span>{gameData.moves.length} plies</span></div><div className="move-list">{gameData.moves.map((m,i)=><button key={`${i}-${m}`} className={`move-chip ${moveIndex===i+1?"selected":""}`} onClick={()=>setMoveIndex(i+1)}>{Math.floor(i/2)+1}{i%2===0?".":"…"} {m}</button>)}</div>
    </section><section className="panel">
      <div className="eyebrow">MAKE YOUR GUESS</div><h2>What rating range?</h2><p className="muted">Use the game quality, tactics, and consistency to make your estimate.</p>
      <div className="field"><label>Estimated Elo</label><select value={guess} onChange={e=>setGuess(e.target.value)}>{["400-800","800-1200","1200-1600","1600-2000","2000+"].map(x=><option key={x}>{x}</option>)}</select></div>
      <button className="btn primary" disabled={revealed} onClick={()=>{setQuestions(q=>q+1);if(guess===bucket(gameData.avg))setScore(s=>s+1);setRevealed(true);}}>Submit guess</button>
      {revealed && <div className={`notice ${guess===bucket(gameData.avg)?"":"warn"}`}><strong>{guess===bucket(gameData.avg)?"Correct!":"Not quite."}</strong><br/>Actual range: {bucket(gameData.avg)}<br/>Average Elo: {gameData.avg}<br/>White: {gameData.white} · Black: {gameData.black}<br/>Opening: {gameData.opening}<br/>Result: {gameData.result}<br/>Event: {gameData.event}</div>}
      <div className="stat-row"><div className="stat"><div className="stat-label">SCORE</div><div className="stat-value">{score}</div></div><div className="stat"><div className="stat-label">ROUNDS</div><div className="stat-value">{questions}</div></div><div className="stat"><div className="stat-label">ACCURACY</div><div className="stat-value">{questions?Math.round(score/questions*100):0}%</div></div></div>
      <p className="muted">Time control: {timeType(gameData.time)}</p>
      <button className="btn" onClick={()=>void loadGame()}>New random game ↻</button>
    </section></div>}
  </>;
}

function BoardVisualizer() {
  const [name,setName]=useState(OPENINGS[0].name),[step,setStep]=useState(0);
  const [lightColor,setLightColor]=useState("#e8e8d9"),[darkColor,setDarkColor]=useState("#77966d"),[boardWidth,setBoardWidth]=useState(520);
  const opening=OPENINGS.find(o=>o.name===name)??OPENINGS[0];
  const fen=useMemo(()=>{const g=new Chess();opening.moves.slice(0,step).forEach(m=>{try{g.move(m)}catch{}});return g.fen()},[opening,step]);
  return <>
    <div className="eyebrow">PLAY / BOARD STUDY</div><h1>Board Visualizer</h1><p className="lead">Step through a prepared opening line and customize the board colors and size.</p>
    <div className="columns"><section className="panel"><div className="field"><label>Opening line</label><select value={name} onChange={e=>{setName(e.target.value);setStep(0)}}>{OPENINGS.map(o=><option key={o.name}>{o.name}</option>)}</select></div>
      <div className="grid two"><div className="field"><label>Light squares</label><input aria-label="Light square color" type="color" value={lightColor} onChange={e=>setLightColor(e.target.value)}/></div><div className="field"><label>Dark squares</label><input aria-label="Dark square color" type="color" value={darkColor} onChange={e=>setDarkColor(e.target.value)}/></div></div>
      <div className="field"><label>Board size: {boardWidth}px</label><input type="range" min="300" max="620" step="20" value={boardWidth} onChange={e=>setBoardWidth(Number(e.target.value))}/></div>
      <ChessBoard fen={fen} width={boardWidth} lightColor={lightColor} darkColor={darkColor}/><div className="board-caption"><span>PLY {step}</span><span>{opening.moves.length} PLIES IN LINE</span></div>
      <div className="button-row"><button className="btn" disabled={step===0} onClick={()=>setStep(s=>Math.max(0,s-1))}>← Back</button><button className="btn primary" disabled={step>=opening.moves.length} onClick={()=>setStep(s=>Math.min(opening.moves.length,s+1))}>Next →</button><button className="btn" onClick={()=>setStep(0)}>Reset</button></div>
    </section><section className="panel"><h2>{opening.name}</h2><p className="muted">{opening.overview}</p><h3>Moves</h3><div className="move-list">{opening.moves.map((m,i)=><button className={`move-chip ${step===i+1?"selected":""}`} key={`${m}-${i}`} onClick={()=>setStep(i+1)}>{Math.floor(i/2)+1}{i%2===0?".":"…"} {m}</button>)}</div><div className="notice">Tip: select any move to jump to that position, or use the controls to step through the line.</div></section></div>
  </>;
}

function PlayAI() {
  const [fen,setFen]=useState(new Chess().fen()),[history,setHistory]=useState<string[]>([]),[status,setStatus]=useState("White to move."),[thinking,setThinking]=useState(false),[level,setLevel]=useState("Intermediate");
  const userDrop=useCallback((from:string,to:string)=>{const g=new Chess(fen);let move:Move|null=null;try{move=g.move({from:from as Square,to:to as Square,promotion:"q"})}catch{return false}if(!move)return false;setFen(g.fen());setHistory(g.history());setStatus("Thinking…");setThinking(true);setTimeout(()=>{void (async()=>{try{const data=await cloudEval(g.fen());const uci=data?.pvs?.[0]?.moves?.split(" ")[0];let reply:Move|null=null;if(uci)reply=parseUci(g,uci);if(!reply){const legal=g.moves({verbose:true});if(legal.length)reply=g.move(legal[Math.floor(Math.random()*legal.length)]);}if(reply){setFen(g.fen());setHistory(g.history());setStatus(g.isCheckmate()?"Checkmate.":g.isDraw()?"Draw.":g.isCheck()?"Your king is in check.":"Your turn.");}else setStatus("Game over.");}catch{const legal=g.moves({verbose:true});if(legal.length){g.move(legal[Math.floor(Math.random()*legal.length)]);setFen(g.fen());setHistory(g.history());}setStatus("Your turn.");}finally{setThinking(false)}})()},150);return true;},[fen]);
  const reset=()=>{setFen(new Chess().fen());setHistory([]);setStatus("White to move.");setThinking(false)};
  return <>
    <div className="eyebrow">PLAY / PRACTICE</div><h1>Play vs AI</h1><p className="lead">Play a game as White.</p>
    <div className="columns"><section className="panel"><div className="board-caption"><span>YOU PLAY WHITE</span><span>{history.length} PLY</span></div><ChessBoard fen={fen} onDrop={userDrop} disabled={thinking}/><div className="button-row"><button className="btn" onClick={reset}>New game</button><button className="btn" disabled={!history.length||thinking} onClick={()=>{const g=new Chess();history.slice(0,Math.max(0,history.length-2)).forEach(m=>{try{g.move(m)}catch{}});setFen(g.fen());setHistory(g.history());setStatus("Move undone.");}}>Undo pair</button></div></section>
      <section className="panel"><h2>Game status</h2><div className="notice">{status}</div><div className="field"><label>Level</label><select value={level} onChange={e=>setLevel(e.target.value)}>{["Beginner","Intermediate","Advanced"].map(x=><option key={x}>{x}</option>)}</select></div><p className="muted">The opponent uses available position evaluations and legal moves.</p><h3>Move history</h3><div className="move-list">{history.map((m,i)=><span className="move-chip" key={`${i}-${m}`}>{Math.floor(i/2)+1}{i%2===0?".":"…"} {m}</span>)}</div>{thinking&&<div className="notice">Opponent is choosing a move…</div>}</section></div>
  </>;
}

type ReviewItem = { san:string; before:string; after:string; loss:number|null; tag:string; reason:string; pv:string[]; cp:number|null };
function ChessReview() {
  const [pgn,setPgn]=useState(""),[review,setReview]=useState<ReviewItem[]>([]),[idx,setIdx]=useState(0),[busy,setBusy]=useState(false),[progress,setProgress]=useState(""),[error,setError]=useState(""),[summary,setSummary]=useState({white:0,black:0});
  const loadFile=(file:File)=>{const reader=new FileReader();reader.onload=()=>setPgn(String(reader.result??""));reader.readAsText(file)};
  const analyze=async()=>{setError("");setReview([]);setBusy(true);setIdx(0);setProgress("Parsing PGN…");try{
    const game=new Chess();game.loadPgn(pgn);const moves=game.history({verbose:true});
    if(!moves.length)throw new Error("No valid moves were found. Check the PGN and try again.");
    const capped=moves.slice(0,40);const positions=[capped[0].before,...capped.map(m=>m.after)];
    const unique=[...new Set(positions)];const evaluations=new Map<string,any>();let done=0;
    for(let i=0;i<unique.length;i+=4){const batch=unique.slice(i,i+4);const values=await Promise.all(batch.map(async fen=>{try{return [fen,await cloudEval(fen)] as const}catch{return [fen,null] as const}}));values.forEach(([fen,data])=>evaluations.set(fen,data));done+=batch.length;setProgress(`Checking cached analysis: ${Math.min(done,unique.length)}/${unique.length} positions`);}
    const items:ReviewItem[]=capped.map((m,i)=>{const before=evaluations.get(m.before),after=evaluations.get(m.after);const cp1=cpFromData(before),cp2=cpFromData(after);const loss=cp1===null||cp2===null?null:Math.max(0,Math.abs(cp2-cp1));const cls=classifyLoss(loss);return {san:m.san,before:m.before,after:m.after,loss,tag:cls.label,reason:loss===null?"No cached evaluation for one or both positions; this move cannot be reliably classified.":cls.label==="BEST"?"The cached evaluations show very little change in the position.":`Approximate evaluation change: ${Math.round(loss)} centipawns. This is a rough heuristic, not an official accuracy metric.`,pv:after?.pvs?.[0]?.moves?.split(" ").slice(0,8)??[],cp:cp2};});
    setReview(items);const white=items.filter((_,i)=>i%2===0&&items[i].loss!==null),black=items.filter((_,i)=>i%2===1&&items[i].loss!==null);
    const acc=(arr:ReviewItem[])=>arr.length?Math.max(0,Math.min(100,100-arr.reduce((s,m)=>s+(m.loss??0),0)/arr.length/10)):0;
    setSummary({white:acc(white),black:acc(black)});setProgress(items.length<moves.length?`Showing first ${items.length} plies of ${moves.length}.`:"Review ready.");
  }catch(e){setError(e instanceof Error?e.message:"Could not analyze this PGN.");}finally{setBusy(false)}};
  const current=review[idx];const fen=current?current.before:new Chess().fen();
  return <>
    <div className="eyebrow">ANALYZE / GAME REVIEW</div><h1>Chess Review</h1><p className="lead">Paste or upload a PGN to step through the game and check Lichess cached evaluations where available.</p>
    <section className="panel">
      <div className="field"><label>Paste PGN</label><textarea value={pgn} onChange={e=>setPgn(e.target.value)} placeholder={'[Event "Casual Game"]\n[White "Player 1"]\n[Black "Player 2"]\n\n1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 *'} /></div>
      <div className="button-row"><label className="btn">Upload .pgn<input type="file" accept=".pgn,text/plain" style={{display:"none"}} onChange={e=>{const f=e.target.files?.[0];if(f)loadFile(f)}}/></label><button className="btn primary" disabled={busy||!pgn.trim()} onClick={()=>void analyze()}>{busy?"Analyzing…":"Analyze game"}</button></div>
      {busy&&<div className="notice">{progress}</div>}{progress&&!busy&&review.length>0&&<p className="muted">{progress}</p>}{error&&<div className="notice error">{error}</div>}
      <p className="muted">Some positions may not have an available evaluation.</p>
    </section>
    {review.length>0&&<><div className="stat-row"><div className="stat"><div className="stat-label">WHITE ACCURACY ESTIMATE</div><div className="stat-value">{summary.white.toFixed(1)}%</div></div><div className="stat"><div className="stat-label">BLACK ACCURACY ESTIMATE</div><div className="stat-value">{summary.black.toFixed(1)}%</div></div><div className="stat"><div className="stat-label">REVIEWED PLIES</div><div className="stat-value">{review.length}</div></div></div>
      <div className="columns"><section className="panel"><div className="board-caption"><span>POSITION BEFORE MOVE</span><span>{idx+1}/{review.length}</span></div><ChessBoard fen={fen}/><div className="button-row"><button className="btn" onClick={()=>setIdx(i=>Math.max(0,i-1))} disabled={idx===0}>← Previous</button><button className="btn primary" onClick={()=>setIdx(i=>Math.min(review.length-1,i+1))} disabled={idx>=review.length-1}>Next →</button></div><div className="section-head"><h3>Move insight</h3><span className="tag">{current?.tag}</span></div><p className="muted">Move played: <strong>{current?.san}</strong> · Centipawn swing: {current?.loss===null?"Unavailable":current?.loss}</p><h3>Evaluation meter</h3><div className="eval-meter"><div style={{width:`${Math.max(0,Math.min(100,50+(current?.cp??0)/20))}%`}} /></div><p className="muted">{current?.cp===null?"Evaluation unavailable for this position.":`Cached evaluation: ${current?.cp} centipawns (approximate).`}</p><p>{current?.reason}</p><h3>Best move / principal variation</h3><p className="muted">{current?.pv.length?`Suggested continuation: ${current.pv[0]} · Line: ${current.pv.join(" ")}`:"No cached principal variation for this position."}</p></section>
      <section className="panel"><h2>Move timeline</h2><div className="move-list">{review.map((m,i)=><button className={`move-chip ${idx===i?"selected":""}`} key={`${i}-${m.san}`} onClick={()=>setIdx(i)}>{Math.floor(i/2)+1}{i%2===0?".":"…"} {m.san} · {m.tag}</button>)}</div></section></div></>}
  </>;
}

type Puzzle = { id?:string; fen:string; moves:string[]; rating?:number; themes?:string|string[] };
function PuzzleTrainer() {
  const [puzzles,setPuzzles]=useState<Puzzle[]>([]),[puzzle,setPuzzle]=useState<Puzzle|null>(null),[fen,setFen]=useState(new Chess().fen()),[progress,setProgress]=useState(0),[playAs,setPlayAs]=useState("Auto"),[difficulty,setDifficulty]=useState("All"),[mode,setMode]=useState("All"),[input,setInput]=useState(""),[message,setMessage]=useState("Load a puzzle and enter a move in UCI format, such as e2e4."),[rating,setRating]=useState(800),[streak,setStreak]=useState(0),[correct,setCorrect]=useState(0),[total,setTotal]=useState(0);
  useEffect(()=>{void fetch("/data/puzzles.json").then(r=>r.json()).then((data:Puzzle[])=>{setPuzzles(data);if(data.length){const p=data[Math.floor(Math.random()*data.length)];setPuzzle(p);setFen(p.fen)}}).catch(()=>setMessage("Could not load puzzles.json."))},[]);
  const filtered=useMemo(()=>puzzles.filter(p=>{const r=Number(p.rating??1500);const themes=(Array.isArray(p.themes)?p.themes.join(" "):p.themes??"").toLowerCase();if(difficulty==="Easy"&&r>1400)return false;if(difficulty==="Medium"&&(r<1400||r>2000))return false;if(difficulty==="Hard"&&r<2000)return false;if(mode!=="All"&&!themes.includes(mode.toLowerCase()))return false;return true}),[puzzles,difficulty,mode]);
  const next=()=>{const list=filtered.length?filtered:puzzles;if(!list.length)return;const p=list[Math.floor(Math.random()*list.length)];setPuzzle(p);setFen(p.fen);setProgress(0);setInput("");setMessage("New puzzle loaded. Find the best move.");};
  const playMove=()=>{if(!puzzle)return;const g=new Chess(fen);let move:Move|null=null;try{move=parseUci(g,input.trim())}catch{}if(!move){setMessage("That move is illegal. Use UCI notation like e2e4.");return}setTotal(t=>t+1);const expected=puzzle.moves[progress];if(move.from+move.to+(move.promotion??"")===expected){setCorrect(c=>c+1);setStreak(s=>s+1);setRating(r=>r+10);let nextProgress=progress+1;const replyUci=puzzle.moves[nextProgress];if(replyUci){parseUci(g,replyUci);nextProgress++}setFen(g.fen());setProgress(nextProgress);setInput("");setMessage(nextProgress>=puzzle.moves.length?"Puzzle line completed! Great work.":"Correct move! Continue the line.");}else{setFen(g.fen());setStreak(0);setRating(r=>Math.max(100,r-5));setInput("");setMessage("Legal move, but not the expected puzzle move. Reset and try again.");}};
  return <>
    <div className="eyebrow">TRAIN / TACTICS</div><h1>Endgame & Puzzle Trainer</h1><p className="lead">Work through positions from the included puzzle collection. Enter moves in UCI format.</p>
    <div className="columns"><section className="panel">
      <div className="grid two"><div className="field"><label>Difficulty</label><select value={difficulty} onChange={e=>setDifficulty(e.target.value)}>{["All","Easy","Medium","Hard"].map(x=><option key={x}>{x}</option>)}</select></div><div className="field"><label>Puzzle type / theme</label><select value={mode} onChange={e=>setMode(e.target.value)}>{["All","Tactics","Endgame","Mate"].map(x=><option key={x}>{x}</option>)}</select></div><div className="field"><label>Play as</label><select value={playAs} onChange={e=>setPlayAs(e.target.value)}>{["Auto","White","Black"].map(x=><option key={x}>{x}</option>)}</select></div></div>
      <div className="board-caption"><span>PUZZLE RATING {puzzle?.rating??"—"}</span><span>{filtered.length} MATCHES</span></div><ChessBoard fen={fen} orientation={playAs==="Black"?"black":"white"}/>
      <div className="field"><label>Your move (UCI)</label><input value={input} onChange={e=>setInput(e.target.value)} placeholder="e2e4" onKeyDown={e=>{if(e.key==="Enter")playMove()}}/></div>
      <div className="button-row"><button className="btn primary" onClick={playMove} disabled={!puzzle}>Play move</button><button className="btn" onClick={()=>{if(puzzle){setFen(puzzle.fen);setProgress(0);setMessage("Position reset. Try again.")}}}>Reset</button><button className="btn" onClick={next}>Next puzzle ↗</button></div>
      <div className="notice">{message}</div><p className="muted">Puzzle line progress: {progress}/{puzzle?.moves.length??0}. Use “Next puzzle” to skip to another position.</p>
    </section><section className="panel"><h2>Your training stats</h2><div className="stat-row"><div className="stat"><div className="stat-label">RATING</div><div className="stat-value">{rating}</div></div><div className="stat"><div className="stat-label">STREAK</div><div className="stat-value">{streak}</div></div><div className="stat"><div className="stat-label">ACCURACY</div><div className="stat-value">{total?Math.round(correct/total*100):0}%</div></div></div><h3>Move format</h3><ul className="list"><li>Example: e2e4 moves a piece from e2 to e4.</li><li>For promotion, add the piece letter, such as e7e8q.</li><li>Moves are checked against the puzzle's stored solution line.</li></ul></section></div>
  </>;
}

function LearnEndgames() {
  const [name,setName]=useState(LESSONS[0].name);
  const lesson=LESSONS.find(l=>l.name===name)??LESSONS[0];
  return <>
    <div className="eyebrow">TRAIN / THEORY</div><h1>Learn Endgames</h1><p className="lead">Study foundational endgame ideas and how they help turn small advantages into results.</p>
    <div className="columns"><section className="panel"><div className="field"><label>Choose a lesson</label><select value={name} onChange={e=>setName(e.target.value)}>{LESSONS.map(l=><option key={l.name}>{l.name}</option>)}</select></div><ChessBoard fen={lesson.fen}/><div className="notice">Study position only. The board is a visual reference, not a fully guided engine lesson.</div></section><section className="panel"><span className="tag">ENDGAME CONCEPT</span><h2 style={{marginTop:14}}>{lesson.name}</h2><h3>Learning objective</h3><p className="muted">{lesson.objective}</p><h3>Explanation</h3><p>{lesson.text}</p><h3>Reflection question</h3><p className="muted">{lesson.name==="Opposition"?"Why can having the move sometimes be a disadvantage in king endgames?":lesson.name==="Key Squares"?"How can key squares help you evaluate a pawn ending without calculating every line?":lesson.name==="Lucena Position"?"Why is the rook bridge useful against repeated checks?":lesson.name==="Philidor Defense"?"How does an active rook help the defender hold a draw?":"How can deliberately losing a move create a winning opportunity?"}</p></section></div>
  </>;
}
