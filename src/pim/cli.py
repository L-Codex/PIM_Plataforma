"""
CLI module for the PIM platform user interface.
"""

import logging
from typing import List, Optional

from .core import calcular_media, calcular_mediana, calcular_moda
from .data import conteudos, disciplinas, perguntas
from .io import Aluno, carregar_dados, salvar_dados

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure logging for the application.

    Args:
        level: Logging level (default: INFO).
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def registrar_aluno(alunos: List[Aluno]) -> None:
    """
    Register a new student.

    Args:
        alunos: List of existing students.
    """
    print("\n=== Registro de Aluno ===")
    nome = input("Nome: ").strip()
    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return

    email = input("Email: ").strip()
    if not email:
        print("Erro: Email não pode ser vazio.")
        return

    # Check if email already exists
    if any(aluno.email == email for aluno in alunos):
        print("Erro: Este email já está registrado.")
        return

    senha = input("Senha: ").strip()
    if not senha:
        print("Erro: Senha não pode ser vazia.")
        return

    aluno = Aluno(nome=nome, email=email, senha=senha)
    alunos.append(aluno)
    salvar_dados(alunos)
    logger.info(f"Student registered: {nome} ({email})")
    print(f"Aluno {nome} registrado com sucesso!")


def revisar_conteudos() -> None:
    """Display review content for all disciplines."""
    for disciplina, texto in conteudos.items():
        print(f"\n{disciplina}:\n{texto}")
        input("Pressione Enter para continuar")


def fazer_perguntas(disciplina: str) -> float:
    """
    Execute the quiz for a discipline.

    Args:
        disciplina: Name of the discipline.

    Returns:
        Score from 0 to 10 based on correct answers.
    """
    print(f"\nIniciando avaliação de {disciplina}...")
    acertos = 0
    questoes = perguntas.get(disciplina, [])

    if not questoes:
        logger.warning(f"No questions found for discipline: {disciplina}")
        return 0.0

    for p in questoes:
        print(f"\n{p['pergunta']}")
        for opcao in p["opcoes"]:
            print(opcao)
        resp = input("Escolha (A, B, C, D): ").upper().strip()
        if resp == p["resposta"]:
            acertos += 1

    # Calculate score based on actual number of questions
    total_perguntas = len(questoes)
    nota = (acertos / total_perguntas) * 10
    logger.info(
        f"Quiz completed for {disciplina}: {acertos}/{total_perguntas} = {nota:.1f}"
    )
    return nota


def aplicar_avaliacao(aluno: Aluno, alunos: List[Aluno]) -> None:
    """
    Apply an evaluation for a student.

    Args:
        aluno: Student taking the evaluation.
        alunos: List of all students (for saving).
    """
    print("\n=== Avaliação ===")
    for i, disciplina in enumerate(disciplinas, 1):
        print(f"{i}. {disciplina}")

    escolha = input("Escolha a disciplina: ").strip()
    if not escolha.isdigit():
        print("Opção inválida.")
        return

    escolha_num = int(escolha)
    if not 1 <= escolha_num <= len(disciplinas):
        print("Opção inválida.")
        return

    disciplina = disciplinas[escolha_num - 1]
    if disciplina not in perguntas or not perguntas[disciplina]:
        print("Esta disciplina ainda não possui avaliação.")
        return

    nota = fazer_perguntas(disciplina)
    aluno.notas[disciplina].append(nota)
    salvar_dados(alunos)
    logger.info(f"Grade {nota:.1f} recorded for {aluno.nome} in {disciplina}")
    print(f"Nota {nota:.1f} registrada em {disciplina}.")


def ver_notas(aluno: Aluno) -> None:
    """
    Display the grades for a student.

    Args:
        aluno: Student whose grades to display.
    """
    print(f"\n=== Notas de {aluno.nome} ===")
    for disciplina, notas in aluno.notas.items():
        if notas:
            print(f"\n{disciplina}: {notas}")
            media = calcular_media(notas)
            if media is not None:
                print(
                    f"  Média: {media:.2f} -> Indica o desempenho geral ao longo das autoavaliações"
                )
            mediana = calcular_mediana(notas)
            if mediana is not None:
                print(
                    f"  Mediana: {mediana:.2f} -> Representa o valor central das pontuações"
                )
            moda = calcular_moda(notas)
            if moda is not None:
                print(f"  Moda: {moda} -> Valor mais frequente entre as avaliações")
            else:
                print("  Moda: Não definida (valores únicos)")
        else:
            print(f"{disciplina}: Sem notas")


def fazer_login(alunos: List[Aluno]) -> Optional[Aluno]:
    """
    Authenticate a student.

    Args:
        alunos: List of registered students.

    Returns:
        The authenticated student, or None if authentication failed.
    """
    print("\n=== Login ===")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    for aluno in alunos:
        if aluno.email == email and aluno.senha == senha:
            logger.info(f"Successful login: {aluno.nome} ({email})")
            print(f"Bem-vindo(a), {aluno.nome}!")
            return aluno

    logger.warning(f"Failed login attempt for email: {email}")
    print("Email ou senha incorretos.")
    return None


def menu_aluno(aluno: Aluno, alunos: List[Aluno]) -> None:
    """
    Display the student menu.

    Args:
        aluno: Logged-in student.
        alunos: List of all students.
    """
    while True:
        print(f"\n=== Menu de {aluno.nome} ===")
        print("1. Revisar Conteúdos")
        print("2. Avaliação")
        print("3. Notas")
        print("4. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            revisar_conteudos()
        elif opcao == "2":
            aplicar_avaliacao(aluno, alunos)
        elif opcao == "3":
            ver_notas(aluno)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


def main() -> None:
    """Main entry point for the application."""
    setup_logging()
    logger.info("Starting PIM Platform")

    try:
        alunos = carregar_dados()
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        print(f"Erro ao carregar dados: {e}")
        alunos = []

    while True:
        print("\n=== Plataforma de Revisão ===")
        print("1. Registro")
        print("2. Login")
        print("3. Encerrar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            registrar_aluno(alunos)
        elif opcao == "2":
            aluno = fazer_login(alunos)
            if aluno:
                menu_aluno(aluno, alunos)
        elif opcao == "3":
            logger.info("Shutting down PIM Platform")
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
