import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // The app uses a small API route to proxy Lichess Cloud Evaluation.
  // Large PGN and puzzle datasets are served as static files from /public/data.
};

export default nextConfig;
