# Auditoria de estabilização — Proceder Filosófico / Mundo das Ideias

Data: 09/11/2026, Asia/Tokyo. Repositório: fabioakira88/mundo-das-ideias. Marca atual preservada; domínio Proceder mantido por continuidade.

## Diagnóstico e correções

| Prioridade | Evidência | Correção |
|---|---|---|
| P0 infraestrutura | DNS público resolve Hostinger; certificado servido venceu em 30/07/2026. Pages possui certificado aprovado até 25/01/2027, mas HTTPS obrigatório estava desativado. | HTTPS obrigatório ativado no Pages. DNS depende de acesso confirmado à Hostinger; não confundir deploy GitHub com atualização do servidor antigo. |
| P1 funcionalidade | renderGrid substituía links estáticos por artigos com role=button. openPost sobrescrevia readerContent, descartando a navegação editorial gerada; leitura dependia de JS/histórico paralelo. | Busca filtra os links estáticos existentes. Rotas são documentos reais; retorno por link nativo. Mantidos taxonomia, leituras relacionadas, abertura em nova aba e histórico do navegador. |
| P1 acessibilidade | Slides invisíveis continuavam na árvore acessível; rotação automática sem pausa e sem respeitar reduced motion. H1 representava apenas Sócrates. | Um H1 estável para a revista; slides com inert/aria-hidden, controle de pausa, pausa por foco/hover e respeito a movimento reduzido. |
| P1 arquitetura | Gerador removia recursivamente qualquer diretório sob artigos. | Limpeza restrita a saídas identificadas pelo marcador do gerador. |
| P1 deploy | Fallback usava FTP sem TLS; flags declaradas no workflow não eram consumidas. | FTPS com validação do certificado, canal de dados cifrado, tracked-only padrão e geração SEO configurável. Fallback não executado contra produção. |
| P2 segurança de renderização | Área de estudos concatenava metadados sem escape e fallback de imagem podia repetir erros. | Escape na fronteira HTML, fallback de execução única e normalização do prefixo relativo de assets. Não equivale a sanitização de HTML editorial arbitrário. |
| P2 arquitetura de arquivos | Comportamento da Home e do índice duplicado em 91 páginas geradas; preview social incluído no staging. | Módulos externos home.js, hero-carousel.js e article-index.js; preview social excluído do Pages. CI de validação também em pull requests. |
| P2 navegação | Sem atalho para o conteúdo principal. Busca sem estado vazio anunciado. | Skip link, destino principal e feedback com região viva; busca persistida na URL. |

## Validação

Os seis validadores existentes e o novo validate_runtime_contracts.mjs passaram. Metadados dos 91 artigos, assets, links, manifesto de deploy, arquitetura editorial e sitemap/robots conferidos. Gerador executado duas vezes para conferir determinismo. posts.js e conteúdo editorial preservados.

Testes de navegador: carrossel troca de Sócrates para Platão mantendo só um slide acessível; busca sem resultados; busca sem acentos por Marco Aurelio; link real abre artigo com taxonomia preservada. Verificações responsivas registradas na entrega. Não houve envio de newsletter, compra ou execução de FTP.

## Limites e continuidade

Não foi realizada certificação global WCAG, pentest, revisão factual dos 91 textos nem auditoria de todos os plugins WordPress. O WordPress antigo e o frontend estático são sistemas diferentes: corrigir um não corrige automaticamente o outro. Não foram removidos originais ou assets legados em massa.

A regularização DNS/HTTPS precisa ser confirmada separadamente da publicação do código. Não expor credenciais em relatórios, Git, arquivos de ambiente versionados ou screenshots.
