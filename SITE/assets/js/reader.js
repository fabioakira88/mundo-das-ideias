(function () {
  function rewriteArticleContent(html) {
    return String(html || '')
      .replace(/(src|href)="assets\//g, '$1="/assets/')
      .replace(/href="\?post=([^"&]+)"/g, 'href="/artigos/$1/"');
  }

  window.MundoDasIdeiasReader = { rewriteArticleContent: rewriteArticleContent };

  // Article content is replaced when navigating. Delegate quiz interactions to
  // the document so controls remain live after every replacement.
  document.addEventListener('click', function (event) {
    var button = event.target.closest('.mi-quiz button');
    if (!button) return;
    var quiz = button.closest('.mi-quiz');
    var answers;
    try { answers = JSON.parse(quiz.dataset.answers); } catch (_) { return; }
    var questions = Array.from(quiz.querySelectorAll('fieldset'));
    var result = quiz.querySelector('.mi-quiz-result');
    if (!result || answers.length !== questions.length) return;
    var selections = questions.map(function (question) { return question.querySelector('input:checked'); });
    if (selections.some(function (input) { return !input; })) {
      result.textContent = 'Responda todas as perguntas para conferir o resultado.';
      return;
    }
    var score = 0;
    questions.forEach(function (question, index) {
      if (Number(selections[index].value) === answers[index]) score++;
      var explanation = question.querySelector('.mi-quiz-explanation');
      if (explanation) explanation.hidden = false;
    });
    result.textContent = 'Resultado: ' + score + '/' + answers.length + '. Confira as explicações de cada pergunta.';
  });

  function varyQuizOptions() {
    document.querySelectorAll('.mi-quiz-question:not([data-options-ordered])').forEach(function (question, index) {
      var labels = Array.from(question.querySelectorAll('label'));
      if (labels.length < 2) return;
      var offset = (index + 1) % labels.length;
      var explanation = question.querySelector('.mi-quiz-explanation');
      labels.slice(offset).concat(labels.slice(0, offset)).forEach(function (label) {
        question.insertBefore(label, explanation);
      });
      question.dataset.optionsOrdered = 'true';
    });
  }
  varyQuizOptions();
  var content = document.getElementById('readerContent');
  if (content) new MutationObserver(varyQuizOptions).observe(content, { childList: true });
})();
