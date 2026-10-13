# Auditoria Mundo das Ideias

Auditoria de 13/10/2026 para a transição do Mundo das Ideias. Nenhum arquivo original foi alterado e nenhuma publicação ou alteração externa foi realizada.

## Entregas

- [Relatório completo](AUDITORIA_MUNDO_DAS_IDEIAS.md)
- [Plano de upgrade](PLANO_DE_UPGRADE.md)
- [Fontes e divergências do Notion](FONTES_NOTION.md)
- [Backlog com critérios de aceite](BACKLOG_UPGRADE.csv)
- [Inventário dos 589 arquivos](inventario_arquivos.csv)
- [Inventário dos 254 assets](inventario_assets.csv)
- [Inventário dos 16 anexos](inventario_referencias.csv)
- [Mapa de 91 artigos e capas](mapa_artigos.csv)
- [Mapa da marca legada](mapa_marca_legada.csv)

## Evidências e método

`evidence/` reúne snapshots de fontes Notion, resultados dos seis validadores, baseline Git, hashes, duplicatas, metadados HTML/PDF, diferenças entre sitemaps, consultas HTTP, testes de navegador e capturas. A pasta não pertence a `SITE/` e não entra no artefato de publicação atual.

As 201 páginas HTML incluem 200 rotas editoriais e um preview social. A navegação foi testada em 15 rotas, com larguras de 1440 e 390 pixels; os achados funcionais receberam verificações específicas. Referências visuais do Instagram foram consultadas na prévia pública de @mundo.das.ideias_. O app e o ZIP integral de branding do Notion têm limites de acesso descritos no relatório.

Os scripts `audit_*.py` e `audit_*.cjs` foram preservados para reprodução nesta máquina. Eles contêm caminhos deste workspace e das dependências de teste existentes; devem ser ajustados em outro ambiente. São scripts de auditoria, não de deploy. As leituras públicas precisam de rede; os testes locais precisam do servidor HTTP na porta 8765.

Dependências usadas para leitura: Python com Pillow, PyMuPDF e pypdf, instaladas em `/private/tmp/mi-audit-python`. Navegação: Playwright/Chromium já disponível no workspace BELZEBU, usando perfil temporário. Dependências não foram adicionadas aos projetos de produção.

Exemplos de reprodução local:

```bash
PYTHONPATH=/private/tmp/mi-audit-python python3 AUDIT/2026-10-13/audit_inventory.py
node AUDIT/2026-10-13/audit_editorial.cjs
node VALIDATION/validate_assets.mjs
node VALIDATION/validate_links.mjs
node VALIDATION/validate_deploy_manifest.mjs
```

O gerador foi executado exclusivamente numa cópia em `/private/tmp/mi-audit-generator`, duas vezes, sem diferenças. Não executar `AUTOMATION/deploy.py` para reproduzir esta auditoria: esse script publica em infraestrutura externa.
