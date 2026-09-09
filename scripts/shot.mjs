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

for (const [name, width, height] of [['desktop', 1400, 900], ['mobile', 390, 844]]) {
  const page = await browser.newPage({ viewport: { width, height } });
  page.on('request', r => {
    const host = new URL(r.url()).host;
    if (host && host !== `localhost:${PORT}`) foreign.add(host);
  });
  await page.goto(`http://localhost:${PORT}/`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  const missing = await page.evaluate(() =>
    ['Manrope', 'IBM Plex Sans'].filter(f => !document.fonts.check(`700 17px "${f}"`)));
  if (missing.length) { console.error(`FEHLER ${name}: Schrift nicht geladen: ${missing.join(', ')}`); failed = true; }

  await page.screenshot({ path: `shots/${name}.png`, fullPage: true });
  await page.close();
}

await browser.close();
server.close();

if (foreign.size) { console.error(`FEHLER: Request an Drittanbieter: ${[...foreign].join(', ')}`); failed = true; }
if (failed) process.exit(1);
console.log('shots/desktop.png, shots/mobile.png  ·  keine Fremd-Requests, Schriften geladen');
