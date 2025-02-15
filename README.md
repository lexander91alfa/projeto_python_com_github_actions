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

## Como criar uma action

### 1. Crie um novo repositório no GitHub

Primeiro, você precisará criar um novo repositório onde a sua action será armazenada. Este repositório conterá o código da sua action.

### 2. Estrutura do projeto

A estrutura básica do seu repositório deve ser a seguinte:

```
your-action-repo/
├── action.yml
├── package.json
├── src/
│   └── run.js
└── tests/
    └── test.js
```

### 3. Definição da action (action.yml)

O arquivo `action.yml` é a definição da sua action. Ele define como a action será executada e quais entradas (inputs) e saídas (outputs) ela terá.

Aqui está um exemplo de `action.yml`:

```yaml
name: 'My Private Action'
description: 'Uma action privada para o meu fluxo de CI'
inputs:
  name:
    description: 'O nome a ser impresso'
    required: true
    default: 'Mundo'
outputs:
  resultado:
    description: 'O resultado da operação'
runs:
  using: 'node16'
  main: 'src/run.js'
```

### 4. Implementação da action (run.js)

O arquivo `run.js` é onde você implementa a lógica da sua action. Aqui está um exemplo simples:

```javascript
const { GitHub, context } = require('@actions/core');

async function run() {
  try {
    const name = GitHub.getInput('name');
    const result = `Olá, ${name}!`;
    
    // Saída para usar em outros steps
    GitHub.setOutput('resultado', result);
    
    // Exemplo de como usar commands para interagir com o workflow
    GitHub.getOctokit().rest.issues.createComment({
      owner: context.repo.owner,
      repo: context.repo.repo,
      issue_number: 1,
      body: result
    });
  } catch (error) {
    GitHub.setFailed(error.message);
  }
}

run();
```

### 5. Configuração do package.json

Crie um arquivo `package.json` na raiz do seu projeto:

```json
{
  "name": "my-private-action",
  "version": "1.0.0",
  "description": "Uma action privada para o meu fluxo de CI",
  "main": "src/run.js",
  "scripts": {
    "build": "tsc",
    "test": "node tests/test.js"
  },
  "keywords": [],
  "author": "Seu Nome",
  "license": "MIT",
  "devDependencies": {
    "@types/node": "^16.0.0",
    "typescript": "^4.5.0"
  }
}
```

### 6. Publicando a action

Para usar a action em seus workflows, você precisará publicá-la no GitHub Marketplace. Para isso:

1. Vá para o seu repositório no GitHub.
2. Navegue até a seção "Actions" no menu lateral.
3. Clique em "New action" e siga as instruções para publicar sua action.

### 7. Usando a action em seu workflow

Agora que a action está publicada, você pode usá-la em seus workflows. Aqui está um exemplo de como usá-la:

```yaml
name: Meu Workflow

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Executar a minha action privada
        uses: seu-usuario/your-action-repo@v1
        id: minha-action
        with:
          name: 'Meu Projeto'
      
      - name: Usar a saída da action
        run: |
          echo "Resultado: ${{ steps.minha-action.outputs.resultado }}"
```

### 8. Dicas e Práticas

- **Testes:** Sempre escreva testes para a sua action. Você pode usar o pacote `@actions/core` para simular o ambiente do GitHub Actions.
- **Versionamento:** Use versionamento semântico para as versões da sua action.
- **Documentação:** Mantenha a documentação da sua action atualizada para que outros desenvolvedores saibam como usá-la.