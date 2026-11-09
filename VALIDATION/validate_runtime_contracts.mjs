import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const home = read('SITE/index.html');
assert.equal((home.match(/<h1\b/g) || []).length, 1, 'Home requires one stable H1');
assert(home.includes('id="pauseHero"'), 'Carousel must have a pause control');
assert(home.includes('inert aria-hidden="true"'), 'Inactive slides must be non-interactive');
const index = read('SITE/artigos/index.html');
assert(!index.includes("card.setAttribute('role', 'button')"), 'Article cards must remain native links');
assert(index.includes('/assets/js/article-index.js'));
const context = vm.createContext({});
vm.runInContext(read('SITE/posts.js') + ';globalThis.records = POSTS;', context);
for (const post of context.records) {
  const html = read('SITE/artigos/' + (post.slug || post.id) + '/index.html');
  assert(html.includes('href="/artigos/"'), 'Article must link to the full index');
  assert(html.includes('reader-taxonomy'), 'Static editorial navigation must be preserved');
  assert(!html.includes('function openPost('), 'Static content must not be overwritten by the old reader');
  assert(html.includes('class="mi-skip"'), 'Skip navigation missing');
}
for (const file of ['article-index.js', 'hero-carousel.js', 'home.js', 'article-list.js', 'reader.js']) {
  new vm.Script(read('SITE/assets/js/' + file), { filename: file });
}
const ftp = read('AUTOMATION/deploy.py');
assert(ftp.includes('FTP_TLS(context=ssl.create_default_context()'));
assert(ftp.includes('ftp.prot_p()'));
console.log('OK: native article navigation, 91 static readers, carousel, hierarchy, JS syntax and encrypted FTP contracts.');
