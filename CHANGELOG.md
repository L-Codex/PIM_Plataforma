# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-01-XX

### Adicionado
- Estrutura modular do projeto com separação em módulos (`core`, `io`, `data`, `cli`)
- Type hints em todas as funções e classes
- Dataclass `Aluno` para representação de alunos
- Logging configurável com mensagens úteis para operações críticas
- Tratamento de erros com exceções específicas (`DataLoadError`, `DataSaveError`)
- Caminho configurável para arquivo de dados via variável de ambiente `PIM_DATA_PATH`
- Validação de entradas do usuário (nome, email, senha não vazios)
- Verificação de email duplicado no registro
- Testes unitários com pytest cobrindo:
  - Cálculos estatísticos (média, mediana, moda)
  - Operações de IO (carregar/salvar dados)
  - Funcionalidades do CLI
  - Tratamento de erros
- Documentação completa em `docs/README.md`
- Script de execução `scripts/run.sh`
- Configuração do projeto com `pyproject.toml`
- Arquivo `requirements.txt` com dependências

### Corrigido
- Cálculo de nota agora usa o número real de perguntas da disciplina
- Função `calcular_moda` agora retorna `Optional[Union[float, List[float]]]`
- Tratamento de listas vazias nas funções estatísticas (retornam `None`)
- Perguntas normalizadas e completas para todas as disciplinas

### Alterado
- Código refatorado de arquivo único (`PIM.py`) para estrutura modular em `src/pim/`
- Melhorada a persistência de dados com criação automática de diretórios
- Formato de saída das notas mantido compatível com versão anterior

### Removido
- Nenhuma funcionalidade foi removida; todas as features originais foram preservadas

## [0.1.0] - Versão Original

### Funcionalidades Iniciais
- Registro de alunos
- Sistema de login
- Revisão de conteúdos
- Avaliações por disciplina
- Visualização de notas com estatísticas
