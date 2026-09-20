// Build with `python -m pelican content -s publishconf.py`, serve output/, then:
// PLAYWRIGHT_MODULE=/path/to/playwright/index.mjs node tests/lightbox.mjs http://localhost:8000
import assert from 'node:assert/strict';
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome', headless: true });
try {
  for (const viewport of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport });
    page.setDefaultTimeout(5000);
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${process.argv[2]}/testing-jev-as-a-gate-for-agent-submitted-knowledge-f6a56d11.html`);
    const image = page.locator('.article-content img').first();
    await image.scrollIntoViewIfNeeded();
    await image.evaluate(img => img.decode());
    assert.equal(await image.getAttribute('tabindex'), '0', 'zoom must be keyboard accessible');
    const thumbnail = await image.boundingBox();
    await image.focus();
    await page.keyboard.press('Enter');
    const dialog = page.getByRole('dialog');
    await dialog.waitFor({ state: 'visible' });
    const enlarged = dialog.locator('img');
    await enlarged.evaluate(img => img.decode());
    const bounds = await enlarged.boundingBox();
    if (viewport.width > 1000) assert(bounds.width > thumbnail.width, 'desktop overlay must enlarge image');
    await page.screenshot({ path: `/tmp/blog-lightbox-${viewport.width}.png` });
    assert(bounds.x >= 0 && bounds.y >= 0 && bounds.x + bounds.width <= viewport.width + 1 && bounds.y + bounds.height <= viewport.height + 1, 'enlarged image must fit viewport');
    await page.keyboard.press('Tab');
    assert(await page.evaluate(() => !!document.activeElement.closest('dialog')), 'focus must stay in lightbox');
    await enlarged.click();
    await dialog.waitFor({ state: 'hidden' });
    assert(await image.evaluate(img => document.activeElement === img), 'closing returns focus');
    await page.keyboard.press('Space');
    await dialog.waitFor({ state: 'visible' });
    await page.keyboard.press('Escape');
    await dialog.waitFor({ state: 'hidden' });
    await image.click();
    await dialog.waitFor({ state: 'visible' });
    await enlarged.click();
    await dialog.waitFor({ state: 'hidden' });
    assert.equal(await page.evaluate(() => document.body.style.overflow), '');
    // Small images must open too, including when wrapped in a link.
    const small = page.locator('.article-content img').nth(1);
    await small.scrollIntoViewIfNeeded();
    await small.click();
    await dialog.waitFor({ state: 'visible' });
    assert.equal(await enlarged.getAttribute('src'), await small.evaluate(img => img.currentSrc || img.src));
    await enlarged.click();
    await dialog.waitFor({ state: 'hidden' });
    await page.route('**/testing-jev-as-a-gate-for-agent-submitted-knowledge-f6a56d11.html', async route => {
      const response = await route.fetch();
      const html = await response.text();
      const linked = html.replace(/(<img[^>]*b6affa18[^>]*>)/, '<a href="https://example.com/">$1</a>');
      assert.notEqual(linked, html, 'fixture must include the small image wrapped in a link');
      await route.fulfill({ response, body: linked });
    });
    await page.reload();
    await small.scrollIntoViewIfNeeded();
    const before = page.url();
    await small.click();
    await dialog.waitFor({ state: 'visible' });
    assert.equal(page.url(), before, 'image click must open viewer rather than follow link');
    await enlarged.click();
    await dialog.waitFor({ state: 'hidden' });
    assert.deepEqual(errors, []);
    await page.close();
  }
  console.log('PASS: desktop/mobile click, keyboard, focus, viewport and Escape');
} finally { await browser.close(); }
