(function () {
      var form = document.getElementById('newsletterForm');
      if (form) {
        form.addEventListener('submit', function(e){
          e.preventDefault();
          var email = document.getElementById('newsletterEmail').value.trim();

          var link = document.createElement('a');
          link.href = '/Relacoes-Leves-Mundo-das-Ideias.pdf';
          link.download = 'Relacoes-Leves-Mundo-das-Ideias.pdf';
          link.style.display = 'none';
          document.body.appendChild(link);
          link.click();
          setTimeout(function(){ document.body.removeChild(link); }, 100);

          var subject = encodeURIComponent('Newsletter Mundo das Ideias');
          var body = encodeURIComponent('Quero receber a newsletter no e-mail: ' + email);
          window.location.href = 'mailto:procederfilosofico@gmail.com?subject=' + subject + '&body=' + body;
        });
      }

})();
