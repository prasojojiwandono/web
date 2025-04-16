const { chromium } = require('playwright'); // You can also try firefox or webkit

(async () => {
  for (let i = 0; i < 50; i++) {
    const browser = await chromium.launch({ headless: false });
    const userAgent = `MyBot/${Math.random().toString().slice(2)}`;
    const context = await browser.newContext({userAgent,}); // Fresh context = new user session
    const page = await context.newPage();

    await page.goto('http://localhost:3000', { waitUntil: 'load' });
    console.log(`User ${i + 1} visited`);
    await page.waitForTimeout(3000); // Allow GA scripts to fire
    await context.clearCookies();

    await browser.close();
  }
})();
