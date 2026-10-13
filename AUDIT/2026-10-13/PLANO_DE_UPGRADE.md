# Plano de upgrade para Mundo das Ideias

Proposta de implementação baseada na auditoria de 13/10/2026. O nome e a transição foram solicitados pelo diretor; os detalhes de execução abaixo são recomendações, não decisões de produto já publicadas.

## Resultado pretendido

Um portal cultural Mundo das Ideias reconhecível como parte de [@mundo.das.ideias_](https://www.instagram.com/mundo.das.ideias_/), com acervo preservado, leitura confortável, navegação consistente e produção rastreável. Artigos, categorias, conceitos, pensadores, dossiês e biblioteca continuam com funções próprias. A identidade aparece na composição e na hierarquia, além da aplicação dos originais MI.

## Fase 1 Consolidar a base e os fluxos

1. Preservar um snapshot do estado atual, incluindo staged, unstaged e untracked. Separar o que já existe do trabalho novo, sem reset ou exclusão em massa.
2. Reconciliar as 16 capas não versionadas e os artigos correspondentes com a origem da release já pública. Conferir diffs antes de formar um commit reproduzível.
3. Corrigir os dois quizzes com um inicializador compartilhado chamado após cada render do reader. Retirar comportamento executável do corpo editorial, mantendo perguntas, gabaritos e explicações como dados. Variar posições corretas e revisar distratores.
4. Corrigir a biblioteca: abas responsivas, detecção de imagens 1 × 1, fallback textual e associação ISBN/edição. Carregar apenas as capas necessárias ao estado ativo.
5. Alinhar a newsletter com sua função real. Captura exige provedor/receptor e confirmação; contato por e-mail pode permanecer claramente identificado. O rodapé não deve fingir inscrição por navegar para uma âncora.
6. Corrigir nome e descrição do PDF de Epicteto e catalogar corretamente o artigo sobre Hegel.

Aceite: validadores passam, checkout limpo contém tudo que o site referencia, quiz mostra pontuação/explicações por URL direta e navegação, biblioteca não transborda em 390 px, capas ausentes têm fallback e a interface comunica o resultado real da captura/contato.

## Fase 2 Formalizar o pacote de marca

Produzir uma configuração central do site com nome público Mundo das Ideias, perfil oficial, domínio atual, metadados da organização, contato existente e caminhos de assets. Manter aliases do identificador Mundo das Ideias onde são necessários à compatibilidade.

O manifesto de assets deve apontar aos dois originais transparentes fornecidos, com SHA-256, dimensões e aliases IMG_8008/IMG_8009. Não reconstruir o desenho. O cadastro do Notion deve refletir a disponibilidade real dos binários após sua vinculação; não marcar um arquivo como verificado apenas porque um nome foi encontrado.

Direção visual consolidada:

| Papel | Direção |
|---|---|
| Fundo de leitura | Branco editorial ou marfim frio, sem textura amarelada automática |
| Texto | Carvão com contraste e entrelinha confortáveis |
| Acento | Vinho em ênfase editorial; bronze mínimo em detalhe funcional |
| Título | Serif editorial de alto contraste, consistente entre componentes |
| Apoio e navegação | Sans discreta e legível |
| Imagem | Fonte documental, gravura, fotografia ou ilustração conceitual identificável |
| Mascote | Opcional; apenas original compatível e com função, sem aves 3D automáticas |
| Forma | Linha, campo, recorte ou comparação com função editorial |

O Master não identifica uma família tipográfica exata para implementação. Testar as famílias existentes como candidatas e registrar a escolha; não afirmar que o logo foi desenhado em Playfair. Os hexadecimais dos dois registries/manuais devem ser reconciliados num conjunto web identificado por versão. Exemplos recentes usam `#F8F3E8`, `#1A1A1A`, `#6B1E23`, `#B08D57`; isso é uma referência documentada, não uma declaração de que todos os pixels da marca têm esses valores.

Aceite: uma versão rastreável do pacote, originais preservados, conflitos de Registry documentados e nenhuma nova identidade proprietária gerada.

## Fase 3 Implementar três páginas de referência

Criar uma fatia local do novo shell, home, artigo e biblioteca antes de propagar para todo o acervo. Produzir capturas reais em desktop, tablet e celular para tornar a solução revisável.

**Home:** masthead Mundo das Ideias, destaque editorial com pergunta/tese concreta, duas ou três entradas secundárias, navegação por temas e um percurso/dossiê. O bloco de abertura deve permitir ver o conteúdo e a publicação, sem ser dominado por um busto em quase toda a primeira tela.

**Artigo:** título, apoio, autoria institucional ou autor real, data, categoria, imagem quando acrescenta contexto, texto em largura confortável, fontes e leituras relacionadas. Preservar o corpo e os slugs. Manter citação, nota e contraponto visualmente distintos sem microtexto decorativo.

**Biblioteca:** catálogo e edições separados de layout; capa real ou fallback honesto, título/autor/edição, motivo da recomendação e destino afiliado. A identidade editorial deve permanecer coerente com a leitura do portal.

Aceite: sistema identificável como MI sem depender do logo, texto legível, navegação por teclado, foco, estados vazios/erro, movimento reduzido e leitura longa confortável. A proposta não precisa copiar literalmente as peças quadradas/verticais do Instagram.

## Fase 4 Propagar a partir das fontes

Atualizar o gerador, o template HUB e os módulos compartilhados. Gerar artigos, categorias, HUBs e dossiês a partir das fontes existentes. Adaptar páginas manuais de pensadores, conceitos, enciclopédia e Sobre ao shell consolidado.

Substituir marca pública e metadados também em `posts.js`, `site-seo.js`, títulos, descrições, publisher/author de JSON-LD, Open Graph, favicon e apple-touch-icon. Preservar identificadores técnicos que não precisam mudar. Não editar centenas de HTMLs derivados como fonte de verdade e não fazer replace global de “mundo-das-ideias”.

Aceite: geração determinística, navegação equivalente, títulos/canonicals corretos e ausência de referências visíveis à identidade aposentada fora de contextos históricos deliberados.

## Fase 5 Curadoria e operação

Revisar imagens de destaque primeiro, depois o restante por risco. Priorizar frases e rostos históricos, dados, saúde mental, direito e política. Registrar proveniência e separar ilustração de documento. Otimizar só os arquivos selecionados; preservar originais e manter um mapa de substituição.

Reconciliar Notion: manter a rota dedicada CURRENT, mapear os registros dos calendários paralelos e vincular URLs publicadas. Os 30 registros de novembro e 31 de dezembro em outra base exigem uma decisão de adoção no workflow; não criar uma terceira agenda. Vincular fontes completas aos itens originais sem rebaixar estados já comprovados.

O BELZEBU deve resolver nome público novo e identificador histórico de forma explícita, carregar o pacote CURRENT da marca e preservar as regras de fonte/QA. Os scripts WordPress devem ficar claramente classificados como legado, sem executar publicação contra a hospedagem atual por acidente.

Aceite: pauta, fonte, asset e estado são rastreáveis; um post com URL real pode ser reconciliado ao registro certo; prompts e arquivos finais são distinguidos.

## Fase 6 Preparar a release

Conferir as 57 URLs somente locais, revisar conteúdo e decidir o lote que integra a release. Fazer staging mínimo; excluir previews, pranchas e materiais de trabalho. Corrigir o contrato do fallback FTP ou mantê-lo indisponível para uso até ser validado.

Na primeira etapa, manter `procederfilosofico.com.br` e os paths existentes. A marca pública pode mudar antes do domínio. Um domínio futuro exige plano próprio de redirecionamento, canonical, sitemap, Search Console, contas e rollback. Preservar o nome do e-mail e a tag de afiliado até existir uma substituição operacional real.

Validar: sintaxe, dados, manifesto, links, imagens, sitemap/robots, geração determinística, funcionamento de quizzes/filtros/formulários, screenshots, console/rede e páginas públicas após o deploy autorizado. Medir performance com ferramentas apropriadas antes/depois; não usar métricas inventadas como sinal de sucesso.

Aceite: artefato reproduzível, rollback identificado e relatório que relaciona versão, commit, execução e URLs. A publicação é uma etapa separada de preparar o upgrade local.

## Frente mobile

Quando o ZIP-fonte for acessível, inventariar o app Expo e seus launchers, confirmar os testes documentados e comparar com o produto atual. Migrar nome/identidade preservando AsyncStorage, currículo, coleções e progresso. Não mudar identificadores de distribuição ou armazenamento sem estratégia de continuidade.

Entregas próprias: preview persistente, onboarding, revisão espaçada e testes reais em iOS/Android. A auditoria documental atual não aprova uma submissão às lojas.

## Ordem prática de execução

Base reproduzível e fluxos → pacote de marca → shell e páginas de referência → propagação pelo gerador → curadoria/Notion → release controlada. O [backlog](BACKLOG_UPGRADE.csv) fornece evidência e aceite por item. O app permanece em trilha separada, sem bloquear a melhoria do portal.
