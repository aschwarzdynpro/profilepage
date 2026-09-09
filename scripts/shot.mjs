// Screenshots (Desktop 1400px, Mobil 390px) plus zwei Zusicherungen:
// 1. Kein Request an einen Drittanbieter-Host (DSGVO, selbst gehostete Fonts).
// 2. Manrope und IBM Plex Sans sind tatsaechlich geladen, nicht nur deklariert.
// Serviert ueber HTTP, weil Chromium @font-face ueber file:// blockiert.
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { serve } from './server.mjs';

const PORT = 8123;
const server = await serve(PORT);

mkdirSync('shots', { recursive: true });
const browser = await chromium.launch();
const foreign = new Set();
let failed = false;

const PAGES = [['start', '/'], ['konsole', '/solution-admin-console.html'], ['impressum', '/impressum.html'], ['datenschutz', '/datenschutz.html']];
const VIEWPORTS = [['desktop', 1400, 900], ['mobile', 390, 844]];
const written = [];

for (const [slug, path] of PAGES) {
  for (const [view, width, height] of VIEWPORTS) {
    const page = await browser.newPage({ viewport: { width, height } });
    page.on('request', r => {
      const host = new URL(r.url()).host;
      if (host && host !== `localhost:${PORT}`) foreign.add(host);
    });
    const res = await page.goto(`http://localhost:${PORT}${path}`, { waitUntil: 'networkidle' });
    if (res.status() !== 200) { console.error(`FEHLER ${path}: HTTP ${res.status()}`); failed = true; }
    await page.evaluate(() => document.fonts.ready);

    const missing = await page.evaluate(() =>
      ['Manrope', 'IBM Plex Sans'].filter(f => !document.fonts.check(`700 17px "${f}"`)));
    if (missing.length) { console.error(`FEHLER ${slug}/${view}: Schrift nicht geladen: ${missing.join(', ')}`); failed = true; }

    const file = `shots/${slug}-${view}.png`;
    await page.screenshot({ path: file, fullPage: true });
    written.push(file);
    await page.close();
  }
}

await browser.close();
server.close();

if (foreign.size) { console.error(`FEHLER: Request an Drittanbieter: ${[...foreign].join(', ')}`); failed = true; }
if (failed) process.exit(1);
console.log(`${written.length} Screenshots  ·  keine Fremd-Requests, Schriften geladen`);
console.log(written.join('\n'));
