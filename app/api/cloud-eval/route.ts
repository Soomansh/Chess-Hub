import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  const fen = request.nextUrl.searchParams.get("fen");
  if (!fen || fen.length > 250) {
    return NextResponse.json({ error: "A valid FEN query parameter is required." }, { status: 400 });
  }

  const upstream = new URL("https://lichess.org/api/cloud-eval");
  upstream.searchParams.set("fen", fen);
  upstream.searchParams.set("multiPv", "1");

  try {
    const response = await fetch(upstream.toString(), {
      headers: { "User-Agent": "ChessHub/1.0 (educational chess project)" },
      cache: "no-store",
      signal: AbortSignal.timeout(8000),
    });

    if (!response.ok) {
      return NextResponse.json(
        { error: response.status === 404 ? "Lichess has no cached evaluation for this position." : `Lichess returned ${response.status}.` },
        { status: response.status === 404 ? 404 : 502 }
      );
    }

    const data = await response.json();
    return NextResponse.json(data, {
      headers: { "Cache-Control": "public, s-maxage=60, stale-while-revalidate=300" },
    });
  } catch {
    return NextResponse.json({ error: "Cloud evaluation is temporarily unavailable." }, { status: 502 });
  }
}
