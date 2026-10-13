const { chromium } = require('/Users/fabiotsugawa/Downloads/DIGITAL_PROJECTS/BELZEBU/node_modules/.pnpm/playwright@1.55.0/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
const root = '/Users/fabiotsugawa/Downloads/DIGITAL_PROJECTS';
const out = path.join(__dirname, 'qa-release');
fs.mkdirSync(out, {recursive:true});
(async () => {
  const browser = await chromium.launch({headless:true});
  const rows = [];
  for (const width of [390, 768, 1440]) {
    const page = await browser.newPage({viewport:{width,height:1000}});
    for (const [brand, port, routes] of [
      ['mi',8765,['/','/artigos/','/filosofos/','/conceitos/','/dossies/','/biblioteca.html','/sobre/']],
      ['jr',8766,['/','/ma-pausa-espaco-vida-japonesa/','/guias/','/nihongo/','/financas-no-japao/','/survival/']]
    ]) {
      for (const route of routes) {
        const errors=[];
        page.removeAllListeners('pageerror'); page.on('pageerror',e=>errors.push(e.message));
        const response = await page.goto(`http://127.0.0.1:${port}${route}`, {waitUntil:'load'});
        await page.waitForTimeout(200);
        const data = await page.evaluate(() => ({
          title:document.title, overflow:document.documentElement.scrollWidth > innerWidth,
          width:document.documentElement.scrollWidth,
          background:getComputedStyle(document.body).backgroundColor,
          visibleBroken:[...document.images].filter(i => i.complete && !i.naturalWidth && getComputedStyle(i).opacity !== '0' && i.getBoundingClientRect().width > 0).map(i=>i.src),
          h1s:[...document.querySelectorAll('h1')].map(e=>e.innerText)
        }));
        rows.push({brand,route,width,http:response.status(),errors,...data});
        await page.evaluate(()=>scrollTo(0,0));
        await page.screenshot({path:path.join(out,`${brand}-${route.replaceAll('/','_')}-${width}.png`)});
      }
    }
    await page.close();
  }
  const page = await browser.newPage({viewport:{width:390,height:900}});
  const quizzes=[];
  for(const slug of ['quiz-estoicismo-vida-pratica','quiz-justica-politica-filosofia']) {
    await page.goto(`http://127.0.0.1:8765/artigos/${slug}/`);
    await page.locator('.mi-quiz button').click();
    const incomplete=await page.locator('.mi-quiz-result').innerText();
    await page.evaluate(()=>document.querySelectorAll('.mi-quiz fieldset').forEach((q,i)=>q.querySelector(`input[value="${JSON.parse(q.closest('.mi-quiz').dataset.answers)[i]}"]`).click()));
    await page.locator('.mi-quiz button').click();
    const correct=await page.locator('.mi-quiz-result').innerText();
    await page.evaluate(()=>document.querySelectorAll('.mi-quiz fieldset').forEach((q,i)=>q.querySelector(`input[value="${(JSON.parse(q.closest('.mi-quiz').dataset.answers)[i]+1)%4}"]`).click()));
    await page.locator('.mi-quiz button').click();
    const wrong=await page.locator('.mi-quiz-result').innerText();
    quizzes.push({slug,incomplete,correct,wrong});
    if(!correct.includes('10/10') || !wrong.includes('0/10') || !incomplete.includes('todas')) throw Error('Quiz failed: '+slug);
  }
  await page.goto('http://127.0.0.1:8765/biblioteca.html');
  await page.route('https://covers.openlibrary.org/**',route=>route.abort());
  await page.locator('[data-tab="usa"]').click();
  await page.waitForTimeout(300);
  const library = await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,placeholders:document.querySelectorAll('#grid-usa .cover-ph').length,cards:document.querySelectorAll('#grid-usa .card').length}));
  await browser.close();
  const result={rows,quizzes,library};fs.writeFileSync(path.join(out,'result.json'),JSON.stringify(result,null,2));
  const failures=rows.filter(r=>r.http!==200||r.errors.length||r.overflow||r.visibleBroken.length);
  console.log(JSON.stringify({routes:rows.length,failures,quizzes,library},null,2));
  if(failures.length||library.overflow||library.placeholders!==library.cards) process.exitCode=1;
})();
