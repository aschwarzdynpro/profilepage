import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
mkdirSync('shots', { recursive: true });
const url = 'file://' + resolve('index.html');
const browser = await chromium.launch();
for (const [name, w, h] of [['desktop', 1400, 900], ['mobile', 390, 844]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.goto(url); await page.waitForTimeout(800);
  await page.screenshot({ path: `shots/${name}.png`, fullPage: true });
  await page.close();
}
await browser.close();
console.log('shots/desktop.png, shots/mobile.png');
