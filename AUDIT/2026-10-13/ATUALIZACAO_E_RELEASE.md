# Mundo das Ideias — atualização de marca e release

Data: 13/10/2026, Asia/Tokyo. Escopo autorizado por Fábio: auditoria, governança no Notion, aplicação web, renomeação de Proceder, correções, commit e deploy. Reaproveitamento editorial em calendário social solicitado na sequência.

## Alterações

- Projeto local renomeado para `MUNDO_DAS_IDEIAS`; 25 caminhos internos e referências operacionais migrados. Logo e monograma originais fornecidos, com hashes registrados, aplicados ao site. Nomes de workflows, scripts, namespaces, SEO e documentos atualizados.
- Notion: governança web CURRENT criada; Master 4.0, workflow, Brand Registry, Asset Registry e governança compartilhada vinculados. Logo e monograma anexados e verificados; mascote continua pendente por asset.
- Calendário principal: 127 registros com canal antigo migrados. Total resultante: 217 pautas Mundo das Ideias. Datas, títulos e estados preservados. Projeto mobile renomeado; opções antigas removidas somente depois de confirmar ausência de registros.
- Tema web CURRENT: papel/marfim, branco, tinta, vinho e bronze; títulos Playfair Display e corpo Lato; logo original, assinatura “Filosofia · Cultura · Pensamento”, leitura a 18 px e foco visível.
- Quizzes: eventos delegados sobrevivem à navegação; perguntas incompletas têm feedback; opções variam de posição sem alterar o gabarito. Testes com 10/10 e 0/10 nos dois quizzes.
- Biblioteca: abas cabem no celular; capas remotas ausentes ou de 1 pixel dão lugar a fallback tipográfico. Capa válida preservada inteira; placeholders ficam disponíveis durante o carregamento.
- Solicitação de newsletter descrita como e-mail e download, conforme funcionamento real. Nome do PDF alinhado ao conteúdo “Relações Leves: Lições de Epicteto”. Nenhum serviço de assinatura foi inventado.
- Documentos de branding anteriores identificados como históricos quando incompatíveis com CURRENT. Evidências brutas e capturas permanecem locais.

## Continuidade e evidências

Domínio `procederfilosofico.com.br`, e-mail existente, tag Amazon e nomes de secrets FTP permanecem por continuidade operacional. Não foram fornecidos destinos substitutos. Slugs e URLs de matérias permanecem estáveis.

Backup anterior à renomeação em `/private/tmp/mi-rename-backup-20261013`; inclui worktree, índice e patches anteriores. O remoto tinha dois commits de artigos já presentes na base local; integrar seu histórico antes do push, sem force push.

Auditoria inicial: `AUDITORIA_MUNDO_DAS_IDEIAS.md`. Migração: `renomeacao/manifest.json` e `renomeacao/notion-migration.json`. QA de release: `qa_release.cjs`; resultados locais em `qa-release/result.json`. Amostra de 39 combinações página/largura nos dois projetos sem falhas de HTTP, JavaScript, overflow ou imagens visivelmente quebradas. Não equivale a certificação global de acessibilidade ou revisão factual integral do acervo.

Verificação pública, SHAs e planejamento social serão registrados após a publicação real. Não marcar um registro como “Publicado” ou “Agendado na rede” por estar datado no Notion.
