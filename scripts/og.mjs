// Rendert assets/og.png (1200x630) aus scripts/og-card.html.
// Nur bei Änderungen an Karte oder Claim nötig: node scripts/og.mjs
import { chromium } from 'playwright';
import { resolve } from 'node:path';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
await page.goto('file://' + resolve('scripts/og-card.html'));
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: 'assets/og.png' });
await browser.close();
console.log('assets/og.png');
