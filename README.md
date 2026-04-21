# Task Manager

Projeto simples em Python para gerenciar uma lista de tarefas pelo terminal.

## Funcionalidades

- Adicionar uma tarefa
- Listar as tarefas cadastradas
- Remover uma tarefa pelo ID
- Encerrar o programa
atch case`, recurso disponivel a partir do Python 3.10.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Como usar

Ao iniciar, o programa exibe um menu com quatro opcoes:

1. Adicionar uma tarefa
2. Visualizar tarefas
3. Excluir uma tarefa
4. Sair

### Exemplo de fluxo

```text
Welcome to the Task Manager!

Please choose an option:
1. Add a task
2. View tasks
3. Delete a task
4. Exit
```

## Estrutura do projeto

```text
.
|- main.py
|- README.md
```

## Limitacoes atuais

- As tarefas ficam apenas em memoria durante a execucao
- Ao fechar o programa, a lista de tarefas e perdida
- Nao ha validacao para entradas invalidas no menu ou na exclusao de tarefas

## Possiveis melhorias

- Salvar tarefas em arquivo JSON ou TXT
- Validar entradas do usuario
- Permitir marcar tarefas como concluidas
- Criar testes automatizados