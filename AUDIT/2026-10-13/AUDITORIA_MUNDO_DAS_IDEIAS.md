# Auditoria do Mundo das Ideias para Mundo das Ideias

Data de referência: 13 de outubro de 2026, Asia/Tokyo. Solicitante: Fábio Tsugawa. Perfil oficial informado e consultado: [@mundo.das.ideias_](https://www.instagram.com/mundo.das.ideias_/).

## Conclusão e escopo da entrega

O Mundo das Ideias tem um acervo e uma arquitetura editorial que podem sustentar o Mundo das Ideias. O upgrade deve preservar artigos, relações, rotas e ferramentas úteis, substituir a apresentação azul/dourada e consolidar a governança e a operação. Uma troca isolada de nome e logo deixaria inconsistências nos templates, no SEO, nas automações e no Notion.

A identidade vigente é a do Master 4.0, complementada pelo workflow CURRENT e pelas referências recentes efetivamente aprovadas. As artes antigas com aves 3D, livros e cenografia clássica permanecem como memória. O feed público atual confirma a direção editorial: branco/marfim, tipografia serifada dominante, carvão, vinho pontual, documentação visual e desenho simples em traço. Não há justificativa para converter todo o site em uma cena greco-romana ou impor um mascote a todas as páginas. Fontes: [Master 4.0](https://app.notion.com/p/3f226a1643dd816181f8f59bbfd9c128), [workflow CURRENT](https://app.notion.com/p/3f226a1643dd8153b7a3d680ee77504b) e [perfil oficial](https://www.instagram.com/mundo.das.ideias_/).

**Estado da auditoria:** inventário local concluído, referências e governança pesquisadas, testes locais e amostra pública executados. **Estado do produto:** upgrade ainda não implementado; release requer saneamento. O app mobile foi identificado e auditado documentalmente, mas seu código anexado no Notion não pôde ser baixado com as capacidades disponíveis. Este relatório não certifica o app, todo o histórico do Instagram, licenças individuais, segurança integral ou métricas de campo.

## 1 Base auditada e preservação

| Item | Base observada |
|---|---|
| Repositório | `DIGITAL_PROJECTS/MUNDO_DAS_IDEIAS` |
| Branch | `main` |
| HEAD | `8f872e05532d5d34ea0a5ea0d0f5558243c5a127` |
| Último commit local | `8f872e0`, 30/07/2026, Publish PF editorial collection and visual refresh |
| Working tree | Alterações staged, unstaged e untracked anteriores à auditoria; baseline em `evidence/git-status-before.txt` |
| Produção | `https://procederfilosofico.com.br`, respostas públicas com servidor GitHub.com |
| Fontes de marca | 4 PDFs, 1 DOCX e 11 PNGs fornecidos; 52 páginas PDF renderizadas para consulta |
| Notion | Hub, Master, workflow, Anti-Genérico, governança, registries, calendários, produto mobile e referências vinculadas |
| Preservação | Nenhum arquivo original alterado; SHA-256 dos 589 arquivos conferido após a investigação |

Credenciais e diretórios `.git`, caches, ambientes e dependências não integram o inventário de conteúdo. `.env` não foi lido. Os materiais recebidos e as páginas do Notion foram tratados como evidência e requisitos do projeto, não como autorização para executar prompts antigos, publicar, enviar mensagens ou modificar rotinas.

O relatório e suas evidências estão em `AUDIT/2026-10-13/`, fora da pasta publicada. Nenhum commit, push, PR, deploy, alteração do Notion, inscrição, e-mail ou agendamento foi realizado.

## 2 Cobertura e inventário

| Universo local | Quantidade |
|---|---:|
| Arquivos inventariados | 589 |
| Volume desses arquivos | 163,44 MiB |
| Assets, incluindo imagens, PDFs, CSS e JS | 254 |
| Volume dos assets | 157,52 MiB |
| Arquivos em `SITE/` | 444 |
| Volume em `SITE/` | 129,14 MiB |
| HTMLs encontrados | 201 |
| Rotas do sitemap local | 200 |
| HTML extra | Preview social `assets/social/anthrobots-carousel/carousel.html` |
| Imagens raster, incluindo favicon ICO | 203 |
| SVGs | 8 |
| PDFs do projeto | 14 |
| CSS/JS e folhas sem extensão | 29 |
| Assets maiores que 1 MiB | 48 |
| Grupos de arquivos idênticos por SHA-256 | 26 |
| Bytes redundantes entre cópias idênticas | 32,34 MiB |
| Assets sem referência literal local encontrada | 120 candidatos |
| Candidatos sem referência dentro do artefato do site | 94, somando 60,94 MiB |

Os 120 candidatos não são uma lista de descarte. Referências dinâmicas, uso externo, arquivos de origem e cópias destinadas à publicação podem justificar sua existência. A busca combina atributos HTML, URLs CSS e strings de dados; não substitui um grafo de execução completo. Os 32,34 MiB também não são uma economia automaticamente realizável no download do usuário: incluem cópias entre pastas de origem e publicação.

Todos os 203 rasters foram abertos pelo decodificador e examinados em seis pranchas de inventário; não houve erro de decodificação. Os 14 PDFs abriram estruturalmente. A leitura editorial integral dos livros/artigos acadêmicos não foi objeto desse teste. As pranchas são evidência de auditoria, não peças sociais a publicar.

Entregáveis de inventário:

- [Todos os arquivos](inventario_arquivos.csv): caminho, tamanho, SHA-256, extensão e versionamento.
- [Todos os assets](inventario_assets.csv): dimensões, transparência quando aplicável, referências encontradas e encaminhamento inicial.
- [Artigos e capas](mapa_artigos.csv): slug, título, categoria, formato, capa, volume textual e links externos de fonte.
- [Ocorrências da marca antiga](mapa_marca_legada.csv): arquivo e linha; inclui documentos históricos, URLs, classes e marcadores técnicos.
- [Duplicatas exatas](evidence/duplicates.json), [páginas](evidence/pages.json), [referências](evidence/references.json) e [PDFs](evidence/pdf-assets.json).

## 3 Fontes de verdade e precedência

A renomeação já consta na [Política Editorial Mestre](https://app.notion.com/p/3dd26a1643dd8176b8e8f49d4fcc3f12): Mundo das Ideias é o novo nome do antigo Mundo das Ideias. Não é uma hipótese criada nesta auditoria.

| Fonte | Papel no upgrade |
|---|---|
| Pedido atual de Fábio | Define a auditoria e a transição para Mundo das Ideias |
| Master 4.0 CURRENT | Identidade e critérios editoriais vigentes; substitui v1, v2.1 e v3.0 |
| Workflow diário CURRENT | Operação específica da marca, referências, fontes, QA e estados reais |
| Anti-Genérico V2.0 CURRENT | Precisão, especificidade, progressão, edição e critérios de parada |
| Governança técnica AION | Arquitetura, Git, validação, UX, SEO, performance e publicação |
| Brand Registry e Asset Registry | Cadastro operacional que precisa ser reconciliado com as decisões acima |
| Feed e peças aprovadas | Evidência visual contextual; não torna automaticamente todo exemplo uma regra geral |
| Manuais antigos e `BRANDING/` do Mundo das Ideias | Histórico e mapa de dependências; regras incompatíveis precisam ser substituídas |

O [workflow](https://app.notion.com/p/3f226a1643dd8153b7a3d680ee77504b) explicita a ordem: instruções posteriores do diretor, Master 4.0, Anti-Genérico V2.0 e versões antigas compatíveis. Os arquivos do Mundo das Ideias que exigem azul/dourado e a preservação irrestrita da identidade antiga conflitam com a transição solicitada. Esse conflito deve ser resolvido na documentação do upgrade, preservando o histórico.

### Divergências do Notion

| Divergência | Evidência e consequência |
|---|---|
| Dois conjuntos de cores | O Brand Registry usa `#F1EEE6 / #262322 / #7A2636 / #9B7B52`; o Master menciona como referência histórica `#F8F3E8 / #1A1A1A / #6B1E23 / #B08D57`. Há concordância sobre base clara, carvão e acentos contidos, mas falta um conjunto técnico único publicado para web. Não escolher silenciosamente uma variante e chamá-la de token oficial. |
| Monograma interno | Registry antigo proíbe brandmark no miolo; Master 4.0 e workflow recente permitem assinatura discreta com função de navegação. A referência operacional recente supera a regra anterior no contexto social. |
| Assets mestres | Logo, brandmark e mascote permanecem `UNVERIFIED`, com arquivo físico pendente no Registry. Registros de produção mais recentes identificam os dois PNGs originais fornecidos. Disponibilidade local e status no cadastro são fatos distintos. |
| Calendários paralelos | Multimarcas: 43 pautas de 24/09 a 31/10. Calendário Editorial: 90 registros Mundo das Ideias e 127 sob Mundo das Ideias. Há sobreposição temporal e divergência de pautas. |
| Planejamento futuro | O índice/workflow diz não presumir novembro confirmado; a outra base já contém 30 pautas de novembro e 31 de dezembro. Existência dos registros não prova adoção no workflow dedicado. |
| Publicação não reconciliada | As 43 pautas multimarcas estão sem URL pública; os estados são 19 Pauta, 13 Roteiro, 9 Briefing Gerado e 2 Arte final. O feed público apresenta publicações recentes. Falta vincular registros e URLs antes de concluir quais correspondem. |
| Fonte-base | 21 das 43 pautas têm `Fonte-base` vazia. Isso não prova ausência de fontes no corpo da página; requer conferência antes de liberar cada pacote. |

Exemplo concreto de conflito de agenda: em 13/10, o multimarcas traz Hans Jonas; a base histórica sob Mundo das Ideias traz Albert Camus. Em 14/10, aparecem Foucault e Antígona, respectivamente. A auditoria não mesclou nem apagou essas filas. Fontes: [Brand Registry MI](https://app.notion.com/p/3ed26a1643dd8174b866ef5ecbb9baab), [Brand Intelligence](https://app.notion.com/p/3ed26a1643dd81ae8da7d8a2ca4f7912), [agenda dedicada](https://app.notion.com/p/3f226a1643dd817c929dd51bf2147ed2) e [Calendário Editorial](https://app.notion.com/p/b32ff26286104a5aa36b850efce0b9ff).

## 4 Identidade atual e referências recebidas

### O que foi confirmado no Instagram

Foi consultada a prévia pública do [perfil oficial](https://www.instagram.com/mundo.das.ideias_/), com 12 miniaturas acessíveis. A comparação visual não incluiu todos os slides, legendas, Stories, arquivo histórico ou métricas privadas.

A bio apresenta filosofia, literatura e cultura. O avatar utiliza o monograma MI preto em campo claro. O feed alterna títulos serifados grandes, destaque vinho em palavras, páginas tipográficas, gravuras, retratos, fotografia institucional e desenho simples de situações humanas. Exemplos visíveis incluem epistemologia, Merleau-Ponty, Simone Weil, Bakhtin e temas públicos contemporâneos. Há também uma miniatura de vídeo, que não autoriza presumir um workflow geral de Reels.

Aplicação recomendada ao portal: transportar hierarquia, contraste, repertório e ritmo para uma experiência responsiva de leitura. O formato social 1080 × 1350 não é uma especificação de largura para páginas web. Fonte visual e registro: `evidence/instagram-public-profile.json` e `evidence/screenshots/instagram-public-profile.png`.

### Classificação dos 16 anexos

| Arquivo ou conjunto | Resultado da inspeção | Encaminhamento |
|---|---|---|
| `Mundo_das_Ideias_Manual_Master_4_0.pdf` | 11 páginas; referência operacional também transcrita no Notion | Base principal |
| `MI_Manual_Editorial_v2_1.pdf` | 15 páginas; virada editorial e anti-genérica | Histórico compatível quando não superado |
| Manual Editorial 3.0 PDF e DOCX | 18 páginas PDF e 220 parágrafos DOCX; evolução e exemplos aprovados | Histórico; PDF utilizado para consulta visual do conteúdo fornecido |
| Manual Estruturado v1 PDF | 8 páginas predominantemente raster, sem texto extraível | Inspecionado visualmente; memória da origem |
| `5BA9...PNG` | Monograma em fundo opaco, 1254 × 1254 | Referência visual, não recorte transparente |
| `22884099...PNG` | Logo completa em fundo opaco, 1122 × 1402 | Referência visual |
| `IMG_8008.PNG` e `Mundo_das_Ideias_monograma_transparente.png` | Cópias binariamente idênticas; RGBA 627 × 647, transparência real | Um original de monograma, com alias registrado |
| `IMG_8009.PNG` e `Mundo_das_Ideias_logo_transparente.png` | Cópias binariamente idênticas; RGBA 1005 × 741, transparência real | Um original de logo, com alias registrado |
| `8C567...PNG` e `4971...PNG` | Alternativas claras RGBA, recorte visual irregular e resíduos | Não selecionar como master sem revisão específica |
| `0AD4...PNG` e `220F...PNG` | CTAs em 1122 × 1402, aves 3D e cenografia | Legado diante do Master vigente |
| `A542...PNG` | Prancha de identidade/mascote em 1122 × 1402 | Legado; não é um corvo isolado pronto para produção |

Os PNGs chamados transparentes possuem canal alfa real; a aparência clara na prévia da conversa não prova fundo opaco. Seus hashes e limites alfa constam em `references-inventory.json`. Não há arquivo vetorial MI fornecido no conjunto local. Não foi reconstruída uma logo, inventada uma família tipográfica ou gerado um novo mascote.

O corvo permanece símbolo, com direção de gravura/line art naturalista. Coruja, pombo, olhos grandes, cachecol e bibliotecas fantasiosas não devem retornar por inércia. A ausência de um corvo isolado compatível não impede uma página editorial sem mascote. Fonte: [Master, seções de imagem e mascote](https://app.notion.com/p/3f226a1643dd816181f8f59bbfd9c128).

## 5 Arquitetura e componentes

| Componente | Fonte atual e estado | Tratamento no upgrade |
|---|---|---|
| Identidade global | `tokens.css`, `mundo-das-ideias-shell.css` e estilos inline; múltiplos conjuntos de variáveis | Consolidar tokens sem troca cega de hexadecimais |
| Cabeçalho e rodapé | Gerador e template HUB; saídas repetidas nas páginas | Preservar destinos úteis, aplicar MI original e reduzir acabamento ornamental |
| Navegação mobile | `.mi-nav` horizontal; rolagem testada | Preservar acesso por toque/teclado e tornar rolagem perceptível |
| Home | `SITE/index.html` e blocos do gerador | Trocar abertura dominada pelo slideshow de bustos por capa editorial com tese e curadoria |
| Hero histórico | 5 WebPs e créditos documentados em `ASSET_CREDITS_HERO.md` | Manter no acervo contextual; uso deixa de ser obrigatório na home |
| Artigos | `posts.js`, template `artigos/index.html`, gerador e reader compartilhado | Preservar 91 slugs e conteúdo; atualizar apresentação e SEO na fonte |
| Busca e filtros | Funções inline, `article-list.js`, scripts de páginas | Reutilizar comportamento comprovado; reduzir duplicação quando houver domínio claro |
| Pensadores | 53 cards renderizados, incluindo classes de entradas além de pessoas | Preservar relações; conferir retratos e distinguir obras de autores na modelagem |
| Conceitos | 60 cards no índice; 18 páginas individuais e índice | Preservar definições e navegação, completar conteúdo onde fizer sentido |
| Categorias | 10 categorias estruturadas e geradas | Preservar slugs; considerar psicologia e Filosofia do Direito como eixos sem criar páginas vazias |
| HUBs | 3 registros em `data/hubs.json`; índice de conteúdo também tem percurso adicional | Preservar curadoria e distinguir registros gerados de páginas manuais |
| Dossiês | 6 registros; 5 ativos e 1 planejado; 52 capítulos declarados | Preservar progressão, referências e status; reconciliar publicação |
| Enciclopédia | Índice e 10 páginas; HTML próprio | Reutilizar conteúdo e revisar fonte/autoria de imagens |
| Biblioteca | 31 edições BR e 27 USA; dados inline, capas Open Library, afiliados | Extrair catálogo como dados, corrigir capas de 1 pixel e overflow; preservar links comerciais válidos |
| Links de livros | `book-affiliate-modal.js`, utilizado em 19 HTMLs | Preservar associação obra/autor; validar o comportamento real antes de trocar UI |
| Quizzes | Dois artigos interativos, código embutido no conteúdo | Corrigir inicialização após render e separar comportamento de corpo editorial |
| Newsletter | Formulário principal via `mailto:`; rodapé usa GET para âncora | Definir captura verificável e feedback; manter alternativa de contato com nome claro |
| Lead magnet | PDF local/público idêntico à cópia em CONTENT, 15 páginas | Corrigir apresentação: arquivo é “Relações Leves”, não edição do Enchirídion |
| SEO | Gerador, `site-seo.js`, metadados nos posts e HTMLs, sitemap/robots | Atualizar fonte de configuração e regenerar; preservar URLs na primeira etapa |
| Deploy | GitHub Pages principal; FTP manual de fallback | Consolidar release reproduzível e revisar exclusões |
| WordPress | Scripts de publicação/correção em AUTOMATION | Classificar como legado operacional; não executar no site estático |
| BELZEBU | Cópia interna MVP e projeto vizinho com referências antigas | Adicionar compatibilidade de nome/identificador; evitar substituir IDs históricos por busca textual |
| App mobile | Documento de produto Expo, código em ZIP externo | Frente separada, com pendência de acesso e testes; não confundir com portal |

As quatro folhas compartilhadas principais são consumidas pelos 200 HTMLs editoriais. `reader.js` aparece em 92 HTMLs e `article-list.js` em um. `navigation.js` e `filters.js` não têm consumidores HTML diretos encontrados: candidatos a consolidação/arquivo, sem remoção automática. O site conserva 203 blocos `<style>` e 100 scripts inline nos 201 HTMLs; grande parte é saída do gerador, não 203 decisões independentes.

## 6 Acervo editorial e adequação visual

| Categoria | Artigos |
|---|---:|
| Filosofia | 43 |
| Atualidade Filosófica | 12 |
| Política | 9 |
| Ciência | 6 |
| História da Civilização | 5 |
| Sociologia | 5 |
| Religião | 4 |
| Literatura | 3 |
| Antropologia | 2 |
| Arte | 2 |
| Total | 91 |

Não foram encontrados slugs duplicados nem repetição literal de `thumb` entre os 91 artigos. Isso não prova diferenciação semântica entre todas as capas. A inspeção visual encontrou forte repetição de salas escuras, livros, bustos e luz teatral em parte do acervo, além de peças com a marca antiga incorporada ao bitmap.

Quarenta e oito artigos não têm link HTTP externo de fonte no corpo do texto. Isso não equivale a ausência de bibliografia: referências podem existir em texto ou fora do campo. O resultado identifica uma fila de revisão de rastreabilidade. A auditoria não validou cada afirmação filosófica dos 91 textos. Datas `dateISO` também não aparecem em 32 registros; o sistema aceita datas legadas, mas vale normalizar a fonte gradualmente.

Capas a revisar primeiro: `descartes-cogito-ergo-sum.png`, `epicuro-pouco-suficiencia-desejo.png`, `adorno-cultura-pensamento.png`, `sao-tomas-fe-razao-explicacao.png` e outras peças com texto/logos incorporados. Representações de pessoas históricas em capas recentes e em `assets/filosofos/` precisam de origem registrada; aparência sintética ou nome do arquivo não bastam para determinar autoria ou autenticidade. Fotografias/gravuras verificáveis devem substituir qualquer retrato que não possa cumprir o Master.

Os cinco assets de hero têm origem e créditos descritos no repositório, o que os torna uma base documental melhor que imagens sem proveniência. O status/licenciamento individual não foi revalidado externamente nesta auditoria. Para cada imagem selecionada no upgrade, registrar origem, autor, instituição, direito de uso, transformações e vínculo editorial.

Há dois problemas de nomenclatura em PDFs:

- `Relacoes-Leves-Mundo-das-Ideias.pdf` abre como **“Relações Leves: Lições de Epicteto para Viver com Mais Paz”**, por Fabio Tsugawa, Mundo das ideias. A oferta da home não distingue esse material autoral de uma edição do Manual de Epicteto.
- `Fenomenologia do Espirito - Hegel.pdf` contém o artigo **“A percepção na Fenomenologia do Espírito”**, de Guilherme Alexandre Martins Amaral, com 17 páginas. Não deve ser catalogado como a obra integral de Hegel.

As oito provas/gabaritos ENEM e os artigos/Pessoa em CONTENT não entram automaticamente no artefato publicado. Preservar como acervo de pesquisa até existir um produto editorial com metadados e uso definidos.

## 7 Achados priorizados

Não foi confirmado um incidente P0 de produção. Os testes revelaram bloqueios e regressões relevantes para preparar a próxima release.

| ID | Prioridade | Achado e evidência | Ação e critério de resolução |
|---|---|---|---|
| A01 | P1 | `validate_deploy_manifest.mjs` falha: 32 referências para 16 capas não versionadas | Consolidar trabalho existente sem perder conteúdo; manifesto passa e checkout limpo reproduz o artefato |
| A02 | P1 | Ambos os quizzes permanecem com resultado vazio e zero explicações após 10 respostas | Inicializar comportamento depois de qualquer render; provar pontuação, revisão e funcionamento pela URL direta e navegação |
| A03 | P1 | Newsletter principal baixa PDF e abre e-mail; rodapé apenas navega via GET | Captura só confirmada por receptor real; contato manual identificado como contato, com estados úteis |
| A04 | P1 | Local e produção divergentes: 200 vs 143 URLs; 57 somente locais; dossiê testado retorna 404 | Reconciliar conteúdo e publicar lote deliberado; mapa URL/estado e rollback antes do deploy |
| A05 | P2 | 33 de 58 capas de livros retornaram 1 × 1; 25 entre as 31 BR | Detectar placeholder/ausência, conferir ISBN e edição; apresentar fallback legível e capas corretas |
| A06 | P2 | Biblioteca tem largura de documento 405 px em viewport 390 px | Corrigir abas/controles; largura de documento não excede viewport nos breakpoints testados |
| A07 | P2 | Marca antiga distribuída por gerador, templates, dados, SEO, CSS, docs e pipelines | Configuração central MI; atualizar saídas a partir das fontes, sem destruir slugs e IDs legados |
| A08 | P2 | Registries antigos conflitam com Master/workflow em cores, assinatura e status dos assets | Registrar versões, vínculo dos originais e precedência; pacote de marca inequívoco |
| A09 | P2 | Três conjuntos de agenda/nomes históricos coexistem; publicação não reconciliada | Eleger rota operacional documentada, vincular registros/URLs e arquivar somente após revisão |
| A10 | P2 | 48 artigos sem link externo no corpo; várias imagens sem proveniência individual demonstrada | Fila editorial por risco; revisão histórica/citacional antes de reutilização em destaque |
| A11 | P2 | Gabarito de ambos os quizzes tem dez respostas corretas na primeira posição | Distribuir posições e revisar distratores, sem alterar correção conceitual |
| A12 | P2 | PDF ofertado e PDF Hegel possuem rótulos imprecisos | Metadados e copy refletem autoria, título e natureza real de cada arquivo |
| A13 | P2 | 48 assets > 1 MiB; capas pesadas e cópias/publicações sociais no pacote do site | Orçamento por papel, derivados responsivos e staging restrito; medir sem apagar originais |
| A14 | P2 | Nenhum `width`/`height` explícito nos 853 `<img>` estáticos analisados | Reservar proporção por HTML/CSS e medir CLS; ausência de atributo não prova deslocamento atual |
| A15 | P2 | Hero com grande ocupação vertical; metadados pequenos e suavizados; redução de movimento não encontrada nas folhas carregadas do teste | Melhorar foco editorial, legibilidade e controle de animação; validar teclado, contraste e movimento |
| A16 | P2 | Workflow FTP define `DEPLOY_TRACKED_ONLY` e `DEPLOY_GENERATE_SEO`; `deploy.py` não lê essas variáveis | Implementar contrato ou remover configuração enganosa; testar manifesto antes de qualquer fallback |
| A17 | P2 | No fluxo Pages, `rsync` exclui docs/wp, mas não o preview social sob assets | Definir artefato mínimo e excluir materiais de trabalho; preview não aparece em deploy sem intenção |
| A18 | P2 | Não foi identificada instalação GA4/GTM funcional nas fontes editoriais examinadas; documento tem ID de exemplo | Confirmar propriedade real e medir eventos sem duplicação; não inserir ID fictício |
| A19 | P3 | README e sistemas antigos descrevem 43 artigos, dossiês vazios e rotas 404 superadas | Documentação regenerada ou com data/estado explícitos e links para fonte atual |
| A20 | P3 | Cópias idênticas, folhas legadas sem consumidores diretos e aliases duplicados | Consolidar por uso provado; exclusão apenas após validação local e pública |

**Causa provável do A02:** o conteúdo inicialmente entregue pelo HTML inclui um script de quiz, mas `openPost()` substitui `readerContent.innerHTML` pelo conteúdo de `posts.js`. Essa substituição descarta os nós/listeners anteriores; o script inserido dessa forma não reinicializa o componente. O comportamento falho foi reproduzido nos dois quizzes. A correção deve viver na camada de componentes, não em uma cópia adicional de cada artigo.

**A05 não é erro de HTTP:** o teste ampliado esperou 12 segundos e forçou carregamento das capas. As imagens completaram; 33 possuíam largura natural 1. O `onerror` existente não detecta essa resposta. Contagens iniciais de imagens pendentes no smoke test foram substituídas por essa evidência mais precisa.

**A07 não pede substituir todas as ocorrências:** há 7.107 ocorrências de “mundo-das-ideias” em 309 arquivos textuais, incluindo relatórios e identificadores. Preservar história, domínios em transição, compatibilidade de projetos, seletores e marcadores consumidos por ferramentas. Priorizar o que o leitor vê e as configurações que geram o site.

## 8 Local e produção

Foram feitas 16 consultas públicas por HTTP, com comparação de bytes quando havia correspondente local. Não foi realizado deploy.

| Recurso | Estado público | Comparação com worktree |
|---|---|---|
| Home | 200 | Diferente |
| Índice de artigos | 200 | Diferente |
| Pensadores, conceitos e enciclopédia | 200 | Iguais na amostra |
| Biblioteca e Sobre | 200 | Iguais |
| Índice de dossiês | 200 | Diferente |
| `/dossies/vida-morte-consciencia/` | 404 | Existe e funciona localmente |
| Artigo Marco Aurélio e sua capa | 200 | Iguais, apesar de ainda não versionados neste checkout |
| Hero Sócrates e logo antiga | 200 | Iguais |
| PDF ofertado na home | 200 | Igual |
| Sitemap | 200, 143 URLs | Local tem 200; 57 adicionais e nenhuma URL exclusiva da amostra pública |
| Robots | 200 | Igual |

Uma capa não versionada neste checkout já está acessível em produção. Portanto, a falha de manifesto prova falta de reprodutibilidade local, não que essas capas estejam quebradas no site público. Da mesma forma, a existência local de dossiês não equivale a publicação.

A recomendação é rebatizar primeiro no domínio atual e preservar paths. Um novo domínio não foi definido. Caso seja adotado depois, preparar redirects e migração de SEO na infraestrutura capaz de emitir redirecionamentos HTTP reais; modificar CNAME ou canonical isoladamente não completa uma migração. Este relatório não afirma perda de tráfego, pois não houve acesso ao Search Console ou a dados analíticos.

## 9 Workflow e governança a transportar

O [workflow CURRENT](https://app.notion.com/p/3f226a1643dd8153b7a3d680ee77504b) determina consulta ao registro original, preservação de pautas e materiais aprovados, fontes rastreáveis, escolha de FAST TRACK/DEEP EDIT, copy exata, especificação por tela, QA e estados comprováveis. A entrega social contém legenda complementar e cinco hashtags. Prompt não equivale a imagem; imagem não equivale a publicação.

O [Anti-Genérico V2.0](https://app.notion.com/p/3f226a1643dd81c8b879ce31f8d19611) pede público, tensão, matéria concreta, mecanismo, limite e corte. Precisão factual insuficiente reprova a peça mesmo que a nota total seja alta. Isso se aplica à curadoria do portal; a regra de 20–55 palavras por slide não limita o tamanho de um ensaio web.

A rotina de 05:00 Asia/Tokyo e sua ativação a partir de 09/10 estão documentadas no Notion. O funcionamento real do agendador não foi inspecionado. Não foi criada, pausada ou alterada automação. Instruções antigas de publicar automaticamente na Política Mestre não foram executadas como parte desta auditoria.

O novo pacote de marca deve resolver nome, aliases, manuais, tokens, originais, contexto da imagem, templates de canal e QA. O conteúdo do site continua com fonte única em `posts.js`; o Notion governa planejamento e evidência, sem criar um espelho manual de todos os artigos.

## 10 App mobile identificado no Notion

A página [Produto, Mapa e Codex](https://app.notion.com/p/3b326a1643dd81db9108c3e1ed79b70c) descreve um Expo/React Native separado, com arco Homero–Sócrates, mapa, duelos de tese/evidência/objeção, cartas, diário e Mesa de Memória com AsyncStorage. O estado é documental, datado de agosto; não foi revalidado executando o produto.

Ela informa raiz histórica `/home/ubuntu/mundo-das-ideias` e ZIP `mundo-das-ideias-codex-source.zip`. A busca no workspace não localizou esse app. O conector devolveu um URI `notion-file-block://`; a tentativa de resolver esse anexo retornou `Invalid URL`. Não há capacidade disponível de download arbitrário binário desse URI. O anexo e os seis assets grandes de launcher excluídos do pacote permanecem pendências de cobertura.

Mapa documental de componentes a incluir na fase mobile:

| Área | Entradas registradas |
|---|---|
| Currículo | `lib/content.ts` |
| Regras e progresso | `lib/game.ts`, `lib/game-context.tsx` |
| Memória/revisão | `lib/review.ts`, `app/review.tsx`, `components/memory-flashcard.tsx` |
| Mapa | `components/parchment-map.tsx` |
| Duelo | `app/duel/[challengeId].tsx`, `components/duel-choice-card.tsx` |
| Dispositivo | `lib/haptics.ts` |
| Handoff | `CODEX_HANDOFF.md` |
| Identidade de distribuição | Icon, splash, favicon e ícones Android |

Preservar progresso e currículo ao migrar a marca; revisar onboarding e testar em iOS/Android reais. O pergaminho é metáfora de interface documentada no app antigo; sua adoção no produto novo precisa ser avaliada no contexto do app, sem transferir automaticamente regras sociais para um jogo.

## 11 Validações e limites

| Verificação | Resultado |
|---|---|
| Sintaxe de posts e gerador | Passou |
| Metadados editoriais | Passou para 91 artigos |
| Arquitetura editorial | Passou |
| Links internos locais | Passou |
| Assets referenciados locais | Passou |
| Sitemap/robots local | Passou |
| Manifesto de deploy | Falhou: 16 assets, 32 referências |
| Âncoras estáticas internas | Zero alvos ausentes encontrados |
| Gerador em cópia isolada | Duas execuções sem diferenças, 91 artigos, 10 categorias, 6 dossiês e 3 HUBs |
| Navegador local | 15 rotas × 2 larguras, 1440 e 390 px |
| HTTP e erros JS locais | 30 respostas 200; zero `pageerror` no smoke test |
| Imagens locais na amostra | Sem falha de carga confirmada; biblioteca externa tem placeholders de 1 pixel |
| Filtros | Busca de pensadores/conceitos e estado sem resultado testados; biblioteca alterna USA e categoria |
| Hero | Próximo slide Sócrates → Platão testado |
| Quiz | Ambos falharam na exibição de resultado após respostas |
| Mobile | Overflow reproduzido na biblioteca; demais rotas da amostra sem overflow do documento |
| PDFs/fontes novas | PDFs de referência renderizados; fontes exatas da marca não inferidas a partir da imagem |
| Git e integridade | Baseline preservado; 589 hashes originais iguais |

Os dois H1 no HTML de `/artigos/` incluem o reader inicialmente oculto. Isso foi tratado como observação estrutural, não como dois títulos principais simultaneamente visíveis. A única página sem SEO básico é o preview social fora do sitemap; não foi confundida com uma página editorial.

Limites relevantes: a amostra de navegador não é um teste visual individual de todas as 200 rotas; não houve teste em aparelhos físicos, leitores de tela, Lighthouse/CrUX, INP real, consentimento de provedor, delivery de e-mail, conversões Amazon, licenciamento integral ou auditoria de vulnerabilidades/dependências. O ZIP de branding de 22 arquivos mencionado no Notion foi inventariado pela descrição, mas não baixado; suas 13 referências JPEG não foram individualmente inspecionadas. A ausência de headers em respostas da hospedagem foi registrada como evidência, sem concluir exploração ou incidente. O Browser integrado estava indisponível por dependência ausente; as verificações usaram Chromium temporário, sem perfil pessoal.

## 12 Correções realizadas e dívida remanescente

Não foram aplicadas correções ao produto nesta fase de auditoria. Foram produzidos inventários, diagnóstico reproduzível, captura das referências, matriz de componentes e plano de migração. Nenhuma implementação anterior foi revertida ou incorporada a commit.

Dívida conscientemente deixada para implementação: fonte única de configuração da marca, inicialização dos quizzes, formulário de captura, catálogo bibliográfico, catálogo de proveniência, resolução dos registries, consolidação de calendários, staging de deploy e otimização de assets selecionados. A limpeza de duplicatas depende de uso; a seleção tipográfica e os tokens web precisam de um protótipo concreto.

## 13 Próxima ação recomendada

Executar o [plano de upgrade](PLANO_DE_UPGRADE.md) em fatias: consolidar a base e corrigir os bloqueios funcionais; normalizar pacote de marca; implementar shell e uma home/artigo/biblioteca de referência; propagar pelo gerador; reconciliar conteúdo/SEO; validar e preparar uma release com rollback. O app mobile segue em frente própria quando o pacote-fonte estiver acessível.

A identidade MI e o acervo existente permitem um upgrade coerente. As prioridades técnicas são tornar a release reproduzível e fazer os fluxos prometidos funcionarem; a prioridade visual é transportar a linguagem editorial atual do Instagram para leitura e navegação web.

As fontes Notion, seus papéis e divergências estão indexadas em [FONTES_NOTION.md](FONTES_NOTION.md). O backlog acionável está em [BACKLOG_UPGRADE.csv](BACKLOG_UPGRADE.csv).
