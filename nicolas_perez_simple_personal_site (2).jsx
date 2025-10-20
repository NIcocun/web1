import { useState } from "react";
import { ArrowLeft, Sun, Moon } from "lucide-react";

export default function NowPage() {
  const [dark, setDark] = useState(true);
  return (
    <div className={dark ? "dark" : ""}>
      <div className="min-h-screen bg-zinc-50 text-zinc-900 transition-colors dark:bg-zinc-900 dark:text-zinc-100">
        <header className="sticky top-0 z-10 backdrop-blur supports-[backdrop-filter]:bg-white/50 dark:supports-[backdrop-filter]:bg-zinc-900/50">
          <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3">
            <a
              href="/"
              className="inline-flex items-center gap-2 rounded-xl border border-zinc-300 px-3 py-1 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"
            >
              <ArrowLeft className="h-4 w-4" /> Back
            </a>
            <button
              onClick={() => setDark((d) => !d)}
              className="rounded-xl border border-zinc-300 p-2 hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"
              aria-label="Toggle theme"
            >
              {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </button>
          </div>
        </header>

        <main className="mx-auto max-w-3xl px-4 pb-20 pt-12 sm:pt-16">
          <h1 className="mb-2 text-3xl font-semibold">Now</h1>
          <p className="mb-10 text-sm text-zinc-600 dark:text-zinc-400">This is what I’m currently focused on as of October 20, 2025 — inspired by Derek Sivers’ <a href="https://nownownow.com" className="text-emerald-600 hover:underline">now page</a> concept.</p>

          <section className="mb-8">
            <h2 className="mb-2 text-lg font-semibold">📍 Location</h2>
            <p className="text-zinc-700 dark:text-zinc-300">Currently traveling the world — recently in Ericeira, Portugal. Most days are a mix of surfing, filming, writing, and long morning runs along whatever coast I’m near.</p>
          </section>

          <section className="mb-8">
            <h2 className="mb-2 text-lg font-semibold">🎬 Projects</h2>
            <ul className="list-disc pl-6 text-zinc-700 dark:text-zinc-300">
              <li>Creating videos for YouTube and documenting the journey.</li>
              <li>Experimenting with short stories and refining my writing craft.</li>
              <li>Teaching yoga whenever possible along the way.</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="mb-2 text-lg font-semibold">📚 Reading</h2>
            <p className="text-zinc-700 dark:text-zinc-300">
              I spend a lot of my time reading — so if you want to keep up, follow my <a href="https://goodreads.com" className="text-emerald-600 hover:underline">Goodreads</a> instead.
            </p>
          </section>

          <footer className="mt-10 text-center text-xs text-zinc-500 dark:text-zinc-400">
            <p>Last updated: October 20, 2025</p>
          </footer>
        </main>
      </div>
    </div>
  );
}
