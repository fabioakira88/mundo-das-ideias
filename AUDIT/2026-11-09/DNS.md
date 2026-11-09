# Regularização do domínio

Estado observado: raiz e www apontam para CDN Hostinger, com certificado expirado. O Pages do repositório já está configurado para procederfilosofico.com.br e possui certificado aprovado. HTTPS obrigatório foi ativado.

Configuração alvo do site estático, conforme documentação oficial GitHub Pages:

- A @ → 185.199.108.153
- A @ → 185.199.109.153
- A @ → 185.199.110.153
- A @ → 185.199.111.153
- CNAME www → fabioakira88.github.io

Antes de mudar: exportar/registrar DNS atual; preservar MX/TXT de e-mail e subdomínios administrativos. Remover somente A/AAAA/ALIAS conflitantes para raiz/www. Desativar CDN Hostinger para o domínio se ela reescrever esses registros. Não remover backups nem instalação WordPress. Confirmar impacto em wp-admin: o conteúdo público passará a seguir o repositório, e WordPress deve manter acesso administrativo próprio se ainda necessário.

Validar dig da raiz/www, certificado HTTPS sem ignorar erros, redirecionamento HTTP e www, resposta da Home e de artigo e hashes do deploy.

Fonte: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
