# 🛠️ Processamento de Dados Automatizado

Este projeto processa automaticamente dados de um arquivo CSV de entrada, gera um arquivo de saída e atualiza o repositório via GitHub Actions.

## 📌 Funcionalidades

- **Processamento de Dados**: Executa um script Python para filtrar/transformar dados.
- **Automatização**: Roda a cada push ou pull request na branch `develop`.
- **Versionamento Automático**: Comite o arquivo gerado de volta ao repositório.

## 🚀 Pré-requisitos

- Python 3.11+
- Biblioteca pandas (`pip install pandas`)
- Conta no GitHub

## ⚙️ Configuração

1. **Variáveis do Repositório**:
   - Acesse `Settings > Secrets and variables > Actions > Variables` no GitHub.
   - Adicione:
     - `EMAIL_VAR`: Seu e-mail (ex: `user@example.com`).
     - `NOME`: Seu nome (ex: `João Silva`).

2. **Estrutura de Pastas**:
   ```
   seu-repositorio/
   ├── .github/
   │   └── workflows/
   │       └── processar_dados.yml
   ├── dados/
   │   ├── entrada.csv    # Arquivo de entrada
   │   └── script.py      # Script de processamento
   └── resultados/        # Pasta para o arquivo gerado
   ```

## 🔄 Como o Workflow Funciona

O GitHub Actions executa as seguintes etapas:

1. **Checkout do Código**: Baixa o repositório.
2. **Configura o Python**: Versão 3.11.
3. **Instala Dependências**: pandas.
4. **Executa o Script**: Processa `dados/entrada.csv` e gera `resultados/saida.csv`.
5. **Commit do Resultado**: Atualiza o repositório com o novo arquivo.

```yaml
# Trecho do Workflow (.github/workflows/processar_dados.yml)
- name: Commit do arquivo gerado
  env:
    EMAIL: ${{ vars.EMAIL_VAR }}
    NOME: ${{ vars.NOME }}
  run: |
    git config --global user.email "$EMAIL"
    git config --global user.name "$NOME"
    git add resultados/saida.csv
    git commit -m "Atualiza arquivo de saída"
    git push origin HEAD:develop
```

## 📂 Estrutura do Projeto

| Pasta/Arquivo          | Descrição                               |
|------------------------|-----------------------------------------|
| `.github/workflows/`   | Configuração do GitHub Actions          |
| `dados/entrada.csv`    | Dados brutos para processamento         |
| `dados/script.py`      | Script Python que processa os dados     |
| `resultados/`          | Arquivos gerados automaticamente        |

## 🐛 Solução de Problemas

**Erro: "Author identity unknown"**  
- Verifique se as variáveis `EMAIL_VAR` e `NOME` estão definidas corretamente em *Settings > Variables*.

**Erro: Permissão negada no `git push`**  
- Adicione `permissions: contents: write` ao workflow.
- Se persistir, [use um PAT](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## 🤝 Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

