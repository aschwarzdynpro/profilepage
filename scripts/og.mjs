// Rendert die OG-Vorschaukarten (1200x630) aus scripts/og-card.html, eine je Seite.
// Nur bei Änderungen an Karte oder Texten nötig: node scripts/og.mjs
import { chromium } from 'playwright';
import { resolve } from 'node:path';

const CARDS = [
  ['og.png', {}],
  ['og-health-check.png', {
    kicker: 'Festpreis-Angebot · 5 Tage',
    title: 'Wie gesund ist Ihr Dynamics 365?',
    sub: 'Unabhängiger Health Check für Dynamics 365 CE und Power Platform. Scorecard, Risikoliste und Maßnahmenplan. Festpreis 5.000 €.',
    tag: 'Health Check',
  }],
  ['og-blog.png', {
    kicker: 'Werkstattnotizen',
    title: 'Wie meine Werkzeuge für Dynamics 365 entstanden sind.',
    sub: 'Welches Problem dahinter stand, wie ich es vorher umgangen habe, was ich gebaut habe und was dabei schiefging.',
    tag: 'Blog',
  }],
  ['og-konsole.png', {
    kicker: 'Eigenes Produkt',
    title: 'Solution Administration Console',
    sub: 'Power Apps Code App für Dataverse-Solutions: Working Solutions, Merge, Release-Prüfung vor und nach dem Import, Betriebsansichten.',
    tag: 'Code App',
  }],
  ['og-studio.png', {
    kicker: 'Eigenes Produkt',
    title: 'Translation Studio',
    sub: 'Fehlende Übersetzungen von Dataverse-Beschriftungen sehen, in einer Matrix oder per CSV füllen und über den Standard-Import zurückspielen.',
    tag: 'Code App',
  }],
  // Englische Fassung unter /en/
  ['og-en.png', {
    kicker: 'Freelance · Nuremberg and DACH region',
    title: 'Solution Architect for Dynamics 365 Sales, Customer Service and Field Service.',
    sub: 'Architecture, ALM and code. 16 years in the Dynamics stack.',
    tag: 'Profile', who: 'Freelancer, Nuremberg',
  }],
  ['og-en-health-check.png', {
    kicker: 'Fixed-price offer · 5 days',
    title: 'How healthy is your Dynamics 365?',
    sub: 'Independent Health Check for Dynamics 365 CE and the Power Platform. Scorecard, risk list and action plan. Fixed price €5,000.',
    tag: 'Health Check', who: 'Freelancer, Nuremberg',
  }],
  ['og-en-blog.png', {
    kicker: 'Workshop notes',
    title: 'How my tools for Dynamics 365 came about.',
    sub: 'What problem was behind them, how I worked around it before, what I built and what went wrong.',
    tag: 'Blog', who: 'Freelancer, Nuremberg',
  }],
  ['og-en-konsole.png', {
    kicker: 'Own product',
    title: 'Solution Administration Console',
    sub: 'Power Apps Code App for Dataverse solutions: working solutions, merge, release checks before and after import, operations views.',
    tag: 'Code App', who: 'Freelancer, Nuremberg',
  }],
  ['og-en-studio.png', {
    kicker: 'Own product',
    title: 'Translation Studio',
    sub: 'See missing translations of Dataverse labels, fill them in a matrix or via CSV and import them back through the standard import.',
    tag: 'Code App', who: 'Freelancer, Nuremberg',
  }],
];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const [file, params] of CARDS) {
  const qs = new URLSearchParams(params).toString();
  await page.goto('file://' + resolve('scripts/og-card.html') + (qs ? '?' + qs : ''));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: 'assets/' + file });
  console.log('assets/' + file);
}
await browser.close();
