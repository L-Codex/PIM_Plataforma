# PIM Platform - Plataforma de Revisão e Avaliação

Uma plataforma CLI para registro de alunos, revisão de conteúdos e avaliações em diversas disciplinas.

## 📋 Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Execução](#execução)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Guia de Contribuição](#guia-de-contribuição)

## Sobre

O PIM Platform é uma plataforma de revisão e autoavaliação que permite aos alunos:
- Registrar-se no sistema
- Revisar conteúdos de diversas disciplinas
- Realizar avaliações
- Acompanhar suas notas e estatísticas (média, mediana, moda)

## Funcionalidades

- **Registro de Alunos**: Cadastro com nome, email e senha
- **Sistema de Login**: Autenticação segura por email e senha
- **Revisão de Conteúdos**: Material de estudo para 8 disciplinas
- **Avaliações**: Questionários de múltipla escolha por disciplina
- **Estatísticas**: Cálculo automático de média, mediana e moda das notas
- **Persistência de Dados**: Armazenamento em JSON com caminho configurável

### Disciplinas Disponíveis

1. Infraestrutura Computacional
2. TIC (Tecnologia da Informação e Comunicação)
3. Pensamento Lógico
4. LGPD (Lei Geral de Proteção de Dados)
5. Cibersegurança
6. Ética
7. Direitos Humanos
8. Matemática e Estatística

## Instalação

### Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/L-Codex/PIM_Plataforma.git
cd PIM_Plataforma
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. (Opcional) Instale o pacote em modo de desenvolvimento:
```bash
pip install -e .
```

## Execução

### Usando o script (Unix/Linux/macOS)

```bash
./scripts/run.sh
```

### Usando Python diretamente

```bash
# No diretório raiz do projeto
PYTHONPATH=src python -m pim.cli
```

### Usando como módulo instalado

Se você instalou o pacote com `pip install -e .`:
```bash
pim
```

### Configuração do Caminho de Dados

Por padrão, os dados são salvos em `data/alunos.json`. Você pode configurar um caminho diferente usando a variável de ambiente:

```bash
export PIM_DATA_PATH=/caminho/personalizado/alunos.json
```

## Testes

### Executar todos os testes

```bash
pytest
```

### Executar com cobertura

```bash
pytest --cov=pim --cov-report=html
```

### Executar testes específicos

```bash
# Testes do módulo core
pytest tests/test_core.py

# Testes do módulo IO
pytest tests/test_io.py

# Testes do CLI
pytest tests/test_cli.py
```

## Estrutura do Projeto

```
PIM_Plataforma/
├── src/
│   └── pim/
│       ├── __init__.py     # Exportações do pacote
│       ├── cli.py          # Interface de linha de comando
│       ├── core.py         # Funções de cálculo estatístico
│       ├── data.py         # Dados (disciplinas, conteúdos, perguntas)
│       └── io.py           # Carregamento e salvamento de dados
├── tests/
│   ├── conftest.py         # Configurações de teste
│   ├── test_cli.py         # Testes do CLI
│   ├── test_core.py        # Testes de cálculos
│   └── test_io.py          # Testes de IO
├── scripts/
│   └── run.sh              # Script de execução
├── docs/
│   └── README.md           # Este arquivo
├── data/                   # Diretório de dados (criado automaticamente)
├── pyproject.toml          # Configuração do projeto
├── requirements.txt        # Dependências
├── CHANGELOG.md            # Histórico de mudanças
└── PIM.py                  # Arquivo original (legado)
```

## Guia de Contribuição

### Configuração para Desenvolvimento

1. Fork o repositório
2. Clone seu fork:
```bash
git clone https://github.com/seu-usuario/PIM_Plataforma.git
```

3. Instale as dependências de desenvolvimento:
```bash
pip install -e ".[dev]"
```

### Estilo de Código

- Siga o PEP 8
- Use Black para formatação:
```bash
black src tests
```

- Use type hints em todas as funções

### Executando Verificações

```bash
# Formatação
black --check src tests

# Testes
pytest

# Type checking (opcional)
mypy src
```

### Submetendo Mudanças

1. Crie uma branch para sua feature:
```bash
git checkout -b feature/minha-feature
```

2. Faça seus commits (mensagens claras e descritivas)
3. Execute os testes e verificações
4. Abra um Pull Request

### Reportando Bugs

Ao reportar bugs, inclua:
- Versão do Python
- Sistema operacional
- Passos para reproduzir
- Comportamento esperado vs. atual

## Licença

Este projeto está sob a licença existente no repositório original.
