(function () {
  var hero = document.getElementById('inicio');
  if (!hero) return;
  var slides = Array.from(hero.querySelectorAll('.hero-slide'));
  var pause = document.getElementById('pauseHero');
  var previous = document.getElementById('prevHero');
  var next = document.getElementById('nextHero');
  if (!slides.length || !pause || !previous || !next) return;
  var index = 0;
  var timer;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var paused = reduced.matches;
  function show(value) {
    index = (value + slides.length) % slides.length;
    slides.forEach(function (slide, i) {
      var active = i === index;
      slide.classList.toggle('active', active);
      slide.inert = !active;
      slide.setAttribute('aria-hidden', String(!active));
    });
  }
  function sync() {
    clearInterval(timer);
    pause.textContent = paused ? 'Reproduzir destaques' : 'Pausar destaques';
    if (!paused && !document.hidden) timer = setInterval(function () { show(index + 1); }, 7000);
  }
  pause.addEventListener('click', function () { paused = !paused; sync(); });
  previous.addEventListener('click', function () { paused = true; show(index - 1); sync(); });
  next.addEventListener('click', function () { paused = true; show(index + 1); sync(); });
  hero.addEventListener('focusin', function () { paused = true; sync(); });
  hero.addEventListener('mouseenter', function () { paused = true; sync(); });
  document.addEventListener('visibilitychange', sync);
  reduced.addEventListener('change', function () { if (reduced.matches) paused = true; sync(); });
  show(0);
  sync();
})();
