(function () {
  function safeText(value) {
    return String(value || '').trim();
  }

  function hideUnavailableBooks() {
    document.querySelectorAll('[data-mi-book]').forEach(function (button) {
      var affiliate = safeText(button.dataset.bookAffiliate);
      if (affiliate) return;

      button.hidden = true;
      button.setAttribute('aria-hidden', 'true');

      var strip = button.closest('.mi-book-strip');
      if (strip && !strip.querySelector('[data-mi-book]:not([hidden])')) {
        strip.hidden = true;
      }
    });
  }

  document.addEventListener('click', function (event) {
    var button = event.target.closest('[data-mi-book]');
    if (!button) return;

    var affiliate = safeText(button.dataset.bookAffiliate);
    if (!affiliate) {
      event.preventDefault();
      return;
    }

    event.preventDefault();
    var opened = window.open(affiliate, '_blank', 'noopener,noreferrer');
    if (!opened) window.location.href = affiliate;
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', hideUnavailableBooks);
  } else {
    hideUnavailableBooks();
  }
})();
