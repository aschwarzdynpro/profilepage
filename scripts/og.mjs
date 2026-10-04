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
