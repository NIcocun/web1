import { useState } from "react";
import { Github, Mail, Youtube, BookOpen, Instagram, Globe, Sun, Moon, ExternalLink } from "lucide-react";

const info = {
  name: "Nicolas Perez",
  tag: "Writer • Filmmaker • Yoga Teacher",
  bio: `I make films and write about travel, books, and building an unconventional life. Currently wandering through Portugal and the Azores.`,
  email: "nicocun03@gmail.com",
  socials: [
    { label: "YouTube", href: "https://youtube.com/@yourchannel", icon: Youtube },
    { label: "Instagram", href: "https://instagram.com/yourhandle", icon: Instagram },
    { label: "Newsletter", href: "https://yournewsletter.com", icon: BookOpen },
    { label: "Now", href: "/now", icon: Globe },
  ],
  projects: [
    {
      title: "Project GOAT",
      about: "A year of worldschooling: films, essays, and lessons from the road.",
      link: "https://youtube.com/@Nicocun25",
    },
    {
      title: "Teaching Yoga on the Road",
      about: "Classes and breathwork wherever I land — from Kenya to Portugal.",
      link: "#",
    },
  ],
  highlights: [
    "200-hr Yoga Teacher (Rishikesh)",
    "Taught writing & breathwork in Kenya",
    "Writer of 100+ weekly letters",
  ],
};

export default function PersonalSite() {
  const [dark, setDark] = useState(true);
  return (
    <div className={dark ? "dark" : ""}>
      <div className="min-h-screen bg-zinc-50 text-zinc-900 transition-colors dark:bg-zinc-900 dark:text-zinc-100">
        <SiteHeader dark={dark} setDark={setDark} />
        <main className="mx-auto max-w-4xl px-4 pb-20 pt-10 sm:pt-16">
          <Hero />
          <About />
          <Projects />
          <Links />
          <Footer />
        </main>
      </div>
    </div>
  );
}

function SiteHeader({ dark, setDark }) {
  return (
    <header className="sticky top-0 z-10 backdrop-blur supports-[backdrop-filter]:bg-white/50 dark:supports-[backdrop-filter]:bg-zinc-900/50">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3">
        <div className="flex items-center gap-2">
          <span className="h-3 w-3 rounded-full bg-emerald-500" />
          <span className="font-medium">{info.name}</span>
        </div>
        <div className="flex items-center gap-3">
          <a
            href="#contact"
            className="rounded-xl border border-zinc-300 px-3 py-1 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"
          >
            Contact
          </a>
          <button
            onClick={() => setDark((d) => !d)}
            className="rounded-xl border border-zinc-300 p-2 hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"
            aria-label="Toggle theme"
          >
            {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </button>
        </div>
      </div>
    </header>
  );
}

function Hero() {
  return (
    <section className="mb-10">
      <div className="flex flex-col items-start gap-6 rounded-3xl border border-zinc-200 bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-950">
        <div className="flex w-full flex-col items-start justify-between gap-6 sm:flex-row sm:items-center">
          <div className="flex items-center gap-4">
            <div className="h-16 w-16 shrink-0 rounded-2xl bg-gradient-to-br from-emerald-400 to-teal-600" />
            <div>
              <h1 className="text-2xl font-semibold sm:text-3xl">{info.name}</h1>
              <p className="text-zinc-600 dark:text-zinc-400">{info.tag}</p>
            </div>
          </div>
          <div className="flex flex-wrap items-center gap-2">
            {info.socials.map((s) => (
              <a
                key={s.label}
                href={s.href}
                className="inline-flex items-center gap-2 rounded-xl border border-zinc-200 bg-zinc-50 px-3 py-2 text-sm hover:bg-zinc-100 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800"
              >
                <s.icon className="h-4 w-4" /> {s.label}
              </a>
            ))}
          </div>
        </div>
        <p className="max-w-prose text-zinc-700 dark:text-zinc-300">{info.bio}</p>
        <div className="flex flex-wrap gap-2">
          {info.highlights.map((h) => (
            <span
              key={h}
              className="rounded-full border border-zinc-300 px-3 py-1 text-xs text-zinc-700 dark:border-zinc-700 dark:text-zinc-300"
            >
              {h}
            </span>
          ))}
        </div>
      </div>
    </section>
  );
}

function About() {
  return (
    <section className="mb-10 grid gap-6 sm:grid-cols-3">
      <div className="rounded-3xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-950">
        <h2 className="mb-2 text-lg font-semibold">Now</h2>
        <p className="text-sm text-zinc-700 dark:text-zinc-300">
          Traveling the world — writing, filming, teaching yoga, and learning from every stop.
        </p>
      </div>
      <div className="rounded-3xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-950">
        <h2 className="mb-2 text-lg font-semibold">Focus</h2>
        <p className="text-sm text-zinc-700 dark:text-zinc-300">
          Creating meaningful YouTube films and stories while studying for the SAT and writing daily.
        </p>
      </div>
      <div className="rounded-3xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-950">
        <h2 className="mb-2 text-lg font-semibold">Reading</h2>
        <p className="text-sm text-zinc-700 dark:text-zinc-300">
          I read constantly — check out my <a href="https://goodreads.com" className="text-emerald-600 hover:underline">Goodreads</a> to see what I’m into lately.
        </p>
      </div>
    </section>
  );
}

function Projects() {
  return (
    <section className="mb-10">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Projects</h2>
        <a href="#" className="text-sm text-emerald-600 hover:underline">
          View all
        </a>
      </div>
      <div className="grid gap-4 sm:grid-cols-2">
        {info.projects.map((p) => (
          <a
            key={p.title}
            href={p.link}
            className="group rounded-3xl border border-zinc-200 bg-white p-5 transition-shadow hover:shadow-md dark:border-zinc-800 dark:bg-zinc-950"
          >
            <div className="mb-2 flex items-center justify-between">
              <h3 className="text-base font-medium">{p.title}</h3>
              <ExternalLink className="h-4 w-4 opacity-60 group-hover:opacity-100" />
            </div>
            <p className="text-sm text-zinc-700 dark:text-zinc-300">{p.about}</p>
          </a>
        ))}
      </div>
    </section>
  );
}

function Links() {
  return (
    <section id="contact" className="mb-10">
      <div className="rounded-3xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-950">
        <h2 className="mb-2 text-lg font-semibold">Get in touch</h2>
        <p className="mb-4 text-sm text-zinc-700 dark:text-zinc-300">
          Want to collaborate, book a class, or riff on ideas? Shoot me an email or ping me on socials.
        </p>
        <div className="flex flex-wrap items-center gap-2">
          <a
            href={`mailto:${info.email}`}
            className="inline-flex items-center gap-2 rounded-xl border border-zinc-300 bg-zinc-50 px-4 py-2 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:bg-zinc-900 dark:hover:bg-zinc-800"
          >
            <Mail className="h-4 w-4" /> {info.email}
          </a>
          {info.socials.map((s) => (
            <a
              key={s.label}
              href={s.href}
              className="inline-flex items-center gap-2 rounded-xl border border-zinc-300 bg-zinc-50 px-4 py-2 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:bg-zinc-900 dark:hover:bg-zinc-800"
            >
              <s.icon className="h-4 w-4" /> {s.label}
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="mt-10 text-center text-xs text-zinc-500 dark:text-zinc-400">
      <p>
        © {new Date().getFullYear()} {info.name}. Built with React & Tailwind. No fluff.
      </p>
    </footer>
  );
}
