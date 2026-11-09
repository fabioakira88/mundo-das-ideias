(function () {
  // Article routes are real documents. Preserve native links, browser history,
  // opening in another tab, and the statically generated taxonomy/related reads.
  if (location.pathname !== '/artigos/' && location.pathname !== '/artigos/index.html') return;
  var input = document.getElementById('articleSearch');
  var grid = document.getElementById('articlesGrid');
  if (!input || !grid) return;
  var cards = Array.from(grid.querySelectorAll('.article-card'));
  var status = document.createElement('p');
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  status.className = 'mi-search-status';
  input.insertAdjacentElement('afterend', status);
  var empty = document.createElement('p');
  empty.textContent = 'Nenhuma matéria encontrada. Tente outro autor ou assunto.';
  empty.hidden = true;
  grid.insertAdjacentElement('afterend', empty);
  function normalize(value) {
    return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }
  var searchable = cards.map(function (card) { return normalize(card.textContent); });
  function filter() {
    var query = normalize(input.value.trim());
    var count = 0;
    cards.forEach(function (card, index) {
      card.hidden = query !== '' && !searchable[index].includes(query);
      if (!card.hidden) count++;
    });
    status.textContent = count + (count === 1 ? ' matéria encontrada.' : ' matérias encontradas.');
    empty.hidden = count !== 0;
  }
  input.value = new URLSearchParams(location.search).get('q') || '';
  input.addEventListener('input', function () {
    filter();
    var url = new URL(location.href);
    if (input.value.trim()) url.searchParams.set('q', input.value.trim());
    else url.searchParams.delete('q');
    history.replaceState(null, '', url.pathname + url.search + url.hash);
  });
  filter();
  var legacySlug = new URLSearchParams(location.search).get('post');
  if (legacySlug && cards.some(function (card) {
    return card.getAttribute('href') === '/artigos/' + encodeURIComponent(legacySlug) + '/';
  })) location.replace('/artigos/' + encodeURIComponent(legacySlug) + '/');
})();
