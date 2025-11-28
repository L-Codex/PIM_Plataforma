"""
Data module containing disciplines, content, and questions for the PIM platform.
"""

from typing import Dict, List, TypedDict


class Pergunta(TypedDict):
    """Type definition for a question."""

    pergunta: str
    opcoes: List[str]
    resposta: str


disciplinas: List[str] = [
    "Infraestrutura Computacional",
    "TIC",
    "Pensamento Lógico",
    "LGPD",
    "Cibersegurança",
    "Ética",
    "Direitos Humanos",
    "Matemática e Estatística",
]

conteudos: Dict[str, str] = {
    "Infraestrutura Computacional": "Um sistema operacional gerencia hardware e permite uso de programas.",
    "TIC": "Tecnologias que permitem comunicação e acesso à informação.",
    "Pensamento Lógico": "Raciocínio para resolver problemas usando programação.",
    "LGPD": "Lei que protege dados pessoais e garante privacidade.",
    "Cibersegurança": "Práticas para proteger sistemas contra ataques.",
    "Ética": "Uso consciente da tecnologia com respeito social e ambiental.",
    "Direitos Humanos": "Garantias de liberdade, igualdade e inclusão digital.",
    "Matemática e Estatística": "Ferramentas para análise de dados, como média, moda e mediana.",
}

perguntas: Dict[str, List[Pergunta]] = {
    "Infraestrutura Computacional": [
        {
            "pergunta": "Quem é considerado o pai do computador?",
            "opcoes": [
                "A) Charles Babbage",
                "B) Alan Turing",
                "C) Bill Gates",
                "D) Steve Jobs",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é memória RAM?",
            "opcoes": [
                "A) Armazenamento permanente",
                "B) Processador",
                "C) Memória de acesso aleatório",
                "D) Disco rígido",
            ],
            "resposta": "C",
        },
        {
            "pergunta": "O que é armazenamento de longo prazo?",
            "opcoes": [
                "A) Memória RAM",
                "B) Processador",
                "C) Hard Disk ou SSD",
                "D) Cache",
            ],
            "resposta": "C",
        },
        {
            "pergunta": "O que significa CPU?",
            "opcoes": [
                "A) Unidade Central de Processamento",
                "B) Memória de Vídeo",
                "C) Sistema Operacional",
                "D) Fonte de energia",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Para que serve o sistema operacional?",
            "opcoes": [
                "A) Controlar hardware e software",
                "B) Armazenar dados",
                "C) Aumentar memória",
                "D) Melhorar velocidade",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é gerenciamento de processos?",
            "opcoes": [
                "A) Controle de tarefas executadas",
                "B) Backup",
                "C) Armazenamento em nuvem",
                "D) Segurança",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é hardware?",
            "opcoes": [
                "A) Programas",
                "B) Componentes físicos",
                "C) Aplicativos",
                "D) Banco de dados",
            ],
            "resposta": "B",
        },
        {
            "pergunta": "O que é software?",
            "opcoes": [
                "A) Placa-mãe",
                "B) Conjunto de programas",
                "C) Processador",
                "D) Disco rígido",
            ],
            "resposta": "B",
        },
        {
            "pergunta": "Principais componentes de hardware?",
            "opcoes": [
                "A) Teclado, mouse, monitor",
                "B) Word e Excel",
                "C) Aplicativos",
                "D) PDF",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é memória cache?",
            "opcoes": [
                "A) Memória auxiliar ao processador",
                "B) Armazenamento na nuvem",
                "C) Banco de dados",
                "D) Backup",
            ],
            "resposta": "A",
        },
    ],
    "TIC": [
        {
            "pergunta": "O que significa TIC?",
            "opcoes": [
                "A) Tecnologia da Informação e Comunicação",
                "B) Transporte Internacional Comercial",
                "C) Técnica Integrada de Computadores",
                "D) Terminal de Informação Coletiva",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é a internet?",
            "opcoes": [
                "A) Rede mundial de computadores",
                "B) Sistema de arquivos",
                "C) Programa de segurança",
                "D) Sistema operacional",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Década do surgimento da internet comercial?",
            "opcoes": ["A) 1970", "B) 1980", "C) 1990", "D) 2000"],
            "resposta": "C",
        },
        {
            "pergunta": "Para que serve o Word?",
            "opcoes": [
                "A) Editar textos",
                "B) Fazer planilhas",
                "C) Criar bancos de dados",
                "D) Programar",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como salvar um arquivo no Word?",
            "opcoes": [
                "A) Arquivo > Salvar",
                "B) Editar > Cortar",
                "C) Exibir > Zoom",
                "D) Inserir > Tabela",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Para que serve o Excel?",
            "opcoes": [
                "A) Criar textos",
                "B) Editar imagens",
                "C) Criar planilhas",
                "D) Reproduzir vídeos",
            ],
            "resposta": "C",
        },
        {
            "pergunta": "Função de somar no Excel?",
            "opcoes": ["A) =SOMA()", "B) =MULT()", "C) =DIV()", "D) =SUB()"],
            "resposta": "A",
        },
        {
            "pergunta": "O que é um gráfico no Excel?",
            "opcoes": [
                "A) Representação visual dos dados",
                "B) Arquivo de texto",
                "C) Programa",
                "D) Fórmula matemática",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como proteger arquivo no Excel?",
            "opcoes": [
                "A) Inserir senha",
                "B) Apagar arquivo",
                "C) Copiar arquivo",
                "D) Abrir arquivo",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual a importância da TIC?",
            "opcoes": [
                "A) Facilitar comunicação",
                "B) Armazenar papel",
                "C) Desenhar imagens",
                "D) Fazer backup",
            ],
            "resposta": "A",
        },
    ],
    "Pensamento Lógico": [
        {
            "pergunta": "O que é uma variável?",
            "opcoes": [
                "A) Espaço para guardar dados",
                "B) Função matemática",
                "C) Programa",
                "D) Entrada de dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual a linguagem usada aqui?",
            "opcoes": ["A) Python", "B) Java", "C) C++", "D) HTML"],
            "resposta": "A",
        },
        {
            "pergunta": "Qual símbolo para igualdade em Python?",
            "opcoes": ["A) =", "B) ==", "C) !=", "D) >"],
            "resposta": "B",
        },
        {
            "pergunta": "O que é um laço?",
            "opcoes": [
                "A) Repetição de comandos",
                "B) Função",
                "C) Variável",
                "D) Entrada de dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como criar uma função em Python?",
            "opcoes": [
                "A) def nome():",
                "B) function nome()",
                "C) func nome{}",
                "D) function nome[]",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é JSON?",
            "opcoes": [
                "A) Formato para dados",
                "B) Banco de dados",
                "C) Programa",
                "D) Editor de texto",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como iniciar um comentário em Python?",
            "opcoes": [
                "A) # comentário",
                "B) // comentário",
                "C) /* comentário */",
                "D) <!-- comentário -->",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual estrutura para decisão?",
            "opcoes": ["A) if", "B) for", "C) while", "D) def"],
            "resposta": "A",
        },
        {
            "pergunta": "Como criar uma lista?",
            "opcoes": [
                "A) lista = []",
                "B) lista = {}",
                "C) lista = ()",
                "D) lista = <>",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual operador para 'e' lógico?",
            "opcoes": ["A) and", "B) or", "C) not", "D) xor"],
            "resposta": "A",
        },
    ],
    "LGPD": [
        {
            "pergunta": "O que significa LGPD?",
            "opcoes": [
                "A) Lei Geral de Proteção de Dados",
                "B) Lei Geral de Processos Digitais",
                "C) Lei de Garantia de Privacidade",
                "D) Lei de Gestão Pública Digital",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual o objetivo da LGPD?",
            "opcoes": [
                "A) Proteger dados pessoais",
                "B) Facilitar venda de dados",
                "C) Permitir acesso livre",
                "D) Eliminar dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Quem deve cumprir a LGPD?",
            "opcoes": [
                "A) Empresas e pessoas que tratam dados",
                "B) Só o governo",
                "C) Só bancos",
                "D) Só escolas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é dado pessoal?",
            "opcoes": [
                "A) Informação que identifica uma pessoa",
                "B) Dados de empresas",
                "C) Dados públicos",
                "D) Dados anônimos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é consentimento?",
            "opcoes": [
                "A) Permissão para usar dados",
                "B) Venda de dados",
                "C) Apagar dados",
                "D) Compartilhar dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Quem pode acessar seus dados?",
            "opcoes": [
                "A) Só com sua autorização",
                "B) Qualquer pessoa",
                "C) Só empresas",
                "D) Governo",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que fazer se seus dados forem vazados?",
            "opcoes": [
                "A) Reportar às autoridades",
                "B) Ignorar",
                "C) Vender os dados",
                "D) Apagar o computador",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como proteger seus dados?",
            "opcoes": [
                "A) Usar senhas fortes",
                "B) Compartilhar senhas",
                "C) Deixar redes abertas",
                "D) Salvar em computadores públicos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que a empresa deve informar?",
            "opcoes": [
                "A) Como usa seus dados",
                "B) Segredo comercial",
                "C) Nada",
                "D) Só o nome",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é privacidade?",
            "opcoes": [
                "A) Direito de controlar dados pessoais",
                "B) Vender dados",
                "C) Usar dados de outros",
                "D) Divulgar informações",
            ],
            "resposta": "A",
        },
    ],
    "Cibersegurança": [
        {
            "pergunta": "O que é cibersegurança?",
            "opcoes": [
                "A) Proteção de sistemas digitais",
                "B) Programação",
                "C) Rede social",
                "D) Computador",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é um vírus de computador?",
            "opcoes": [
                "A) Programa malicioso",
                "B) Programa educativo",
                "C) Programa de segurança",
                "D) Sistema operacional",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é phishing?",
            "opcoes": [
                "A) Ataque para roubar dados",
                "B) Backup",
                "C) Atualização de sistema",
                "D) Programa de edição",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é firewall?",
            "opcoes": [
                "A) Barreira de proteção digital",
                "B) Hardware",
                "C) Programa de edição",
                "D) Computador antigo",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Por que usar senhas fortes?",
            "opcoes": [
                "A) Evitar invasões",
                "B) Facilitar acesso",
                "C) Guardar dados",
                "D) Compartilhar contas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é atualização de software?",
            "opcoes": [
                "A) Corrigir falhas e melhorar segurança",
                "B) Apagar arquivos",
                "C) Comprar programas",
                "D) Instalar jogos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que não fazer para manter segurança?",
            "opcoes": [
                "A) Compartilhar senhas",
                "B) Usar antivírus",
                "C) Atualizar sistema",
                "D) Evitar links suspeitos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é autenticação?",
            "opcoes": [
                "A) Verificar identidade",
                "B) Apagar dados",
                "C) Programar",
                "D) Compartilhar senhas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é ransomware?",
            "opcoes": [
                "A) Sequestro de dados por vírus",
                "B) Backup automático",
                "C) Atualização de software",
                "D) Computador rápido",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como evitar ataques?",
            "opcoes": [
                "A) Não abrir anexos desconhecidos",
                "B) Compartilhar arquivos",
                "C) Usar senhas simples",
                "D) Desligar antivírus",
            ],
            "resposta": "A",
        },
    ],
    "Ética": [
        {
            "pergunta": "O que é ética na tecnologia?",
            "opcoes": [
                "A) Uso responsável e justo",
                "B) Usar tudo sem limites",
                "C) Copiar conteúdos",
                "D) Ignorar direitos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Por que economizar energia?",
            "opcoes": [
                "A) Preservar o meio ambiente",
                "B) Gastar mais",
                "C) Aumentar poluição",
                "D) Gastar dinheiro",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é descarte correto de lixo eletrônico?",
            "opcoes": [
                "A) Levar para pontos de coleta",
                "B) Jogar no lixo comum",
                "C) Queimar lixo",
                "D) Jogar em rios",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como agir com respeito online?",
            "opcoes": [
                "A) Não praticar bullying",
                "B) Insultar pessoas",
                "C) Espalhar fake news",
                "D) Invadir contas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é cidadania digital?",
            "opcoes": [
                "A) Uso consciente da internet",
                "B) Usar a internet sem regras",
                "C) Ignorar leis",
                "D) Compartilhar senhas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Por que respeitar privacidade?",
            "opcoes": [
                "A) Direito de todos",
                "B) Invadir contas",
                "C) Espalhar informações",
                "D) Usar dados alheios",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é inclusão digital?",
            "opcoes": [
                "A) Acesso de todos à tecnologia",
                "B) Excluir pessoas",
                "C) Usar só computadores antigos",
                "D) Compartilhar senhas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como contribuir para sustentabilidade?",
            "opcoes": [
                "A) Reutilizar e reciclar",
                "B) Jogar lixo no chão",
                "C) Gastar muita energia",
                "D) Desperdiçar água",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é transparência digital?",
            "opcoes": [
                "A) Clareza no uso de dados",
                "B) Esconder informações",
                "C) Compartilhar senhas",
                "D) Invadir contas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Por que agir com ética?",
            "opcoes": [
                "A) Construir confiança",
                "B) Enganar pessoas",
                "C) Copiar trabalhos",
                "D) Quebrar regras",
            ],
            "resposta": "A",
        },
    ],
    "Direitos Humanos": [
        {
            "pergunta": "O que são Direitos Humanos?",
            "opcoes": [
                "A) Garantias de liberdade e igualdade",
                "B) Regras só para governos",
                "C) Direito de algumas pessoas",
                "D) Leis para empresas",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é inclusão digital?",
            "opcoes": [
                "A) Acesso universal à tecnologia",
                "B) Excluir pessoas da internet",
                "C) Controlar uso de dados",
                "D) Proibir internet",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual documento protege Direitos Humanos?",
            "opcoes": [
                "A) Declaração Universal dos Direitos Humanos",
                "B) Constituição",
                "C) Código Civil",
                "D) Estatuto do Idoso",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é igualdade?",
            "opcoes": [
                "A) Todos têm os mesmos direitos",
                "B) Alguns têm mais direitos",
                "C) Só alguns podem usar tecnologia",
                "D) Discriminação",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Direito à privacidade inclui?",
            "opcoes": [
                "A) Controle sobre seus dados pessoais",
                "B) Exposição forçada",
                "C) Compartilhar dados sem consentimento",
                "D) Vender dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como promover inclusão?",
            "opcoes": [
                "A) Facilitar acesso e educação digital",
                "B) Bloquear acesso",
                "C) Impedir uso de tecnologia",
                "D) Ignorar grupos",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Quem deve respeitar Direitos Humanos?",
            "opcoes": ["A) Todos", "B) Só o governo", "C) Só empresas", "D) Ninguém"],
            "resposta": "A",
        },
        {
            "pergunta": "O que é discriminação digital?",
            "opcoes": [
                "A) Negar acesso por raça ou renda",
                "B) Permitir acesso a todos",
                "C) Educar sobre tecnologia",
                "D) Proteger dados",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Direito de acesso à informação é?",
            "opcoes": [
                "A) Acesso à internet e dados públicos",
                "B) Proibir acesso",
                "C) Cobrar caro pela internet",
                "D) Bloquear sites",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Por que proteger dados pessoais?",
            "opcoes": [
                "A) Preservar direitos e segurança",
                "B) Vender para terceiros",
                "C) Compartilhar sem controle",
                "D) Ignorar leis",
            ],
            "resposta": "A",
        },
    ],
    "Matemática e Estatística": [
        {
            "pergunta": "O que é média aritmética?",
            "opcoes": [
                "A) Soma dos valores dividida pela quantidade",
                "B) Maior valor",
                "C) Menor valor",
                "D) Valor mais frequente",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é moda em estatística?",
            "opcoes": [
                "A) Valor que mais se repete",
                "B) Média dos valores",
                "C) Valor mínimo",
                "D) Valor máximo",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que é mediana?",
            "opcoes": [
                "A) Valor central ordenado",
                "B) Soma dos valores",
                "C) Valor mais frequente",
                "D) Diferença entre valores",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Como calcular média?",
            "opcoes": [
                "A) Somar e dividir",
                "B) Multiplicar",
                "C) Subtrair",
                "D) Dividir e somar",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual é o valor da moda em [2, 3, 3, 5]?",
            "opcoes": ["A) 3", "B) 2", "C) 5", "D) Nenhum"],
            "resposta": "A",
        },
        {
            "pergunta": "Qual a mediana de [1, 3, 5]?",
            "opcoes": ["A) 3", "B) 1", "C) 5", "D) 2"],
            "resposta": "A",
        },
        {
            "pergunta": "Para que serve a estatística?",
            "opcoes": ["A) Analisar dados", "B) Jogar", "C) Pintar", "D) Cozinhar"],
            "resposta": "A",
        },
        {
            "pergunta": "O que é desvio padrão?",
            "opcoes": [
                "A) Medida de dispersão dos dados",
                "B) Média",
                "C) Moda",
                "D) Mediana",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "O que significa 'frequência' em estatística?",
            "opcoes": [
                "A) Quantidade de vezes que um valor aparece",
                "B) Média dos valores",
                "C) Diferença entre valores",
                "D) Soma dos valores",
            ],
            "resposta": "A",
        },
        {
            "pergunta": "Qual é a média de [4, 6, 8]?",
            "opcoes": ["A) 6", "B) 4", "C) 8", "D) 7"],
            "resposta": "A",
        },
    ],
}
