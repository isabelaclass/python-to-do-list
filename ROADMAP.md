| Nível | Melhoria | Breve descrição |
| --- | --- | --- |
| Intermediário | Persistência com SQLite | Substituir a lista em memória por armazenamento local com SQLite para manter as tarefas entre execuções. |
| Intermediário | ORM com SQLAlchemy ou SQLModel | Adotar um ORM para modelar entidades e acessar dados sem depender de SQL puro em toda a aplicação. |
| Intermediário | Tratamento de exceções | Envolver entradas e operações críticas com try-except para evitar falhas por dados inválidos. |
| Intermediário | Logs com logging | Registrar erros e eventos importantes em arquivo usando a biblioteca logging. |
| Intermediário | Testes unitários com Pytest | Escrever testes automatizados para validar regras como cadastro e persistência de tarefas. |
| Intermediário | Transformação em API REST | Migrar a lógica do terminal para uma API com FastAPI ou Flask. |
| Intermediário | Validação com Pydantic | Definir modelos de entrada e saída para validar dados e padronizar respostas da API. |
| Intermediário | Conteinerização com Docker | Criar Dockerfile para empacotar a aplicação de forma reprodutível. |
| Intermediário | Orquestração com docker-compose | Subir API e banco de dados robusto, como PostgreSQL, em ambiente integrado. |
| Intermediário | Clean Architecture | Separar entidades, casos de uso e adaptadores para reduzir acoplamento e facilitar evolução. |
| Intermediário | CI/CD com GitHub Actions | Automatizar testes e lint a cada commit para manter qualidade e integração contínua. |
| Intermediário | Documentação com Swagger | Publicar e manter documentação interativa da API, aproveitando suporte nativo do FastAPI. |
| Intermediário | Autenticação básica | Criar usuários com senha criptografada e preparar o fluxo de acesso autenticado. |
| Intermediário | Login com JWT | Implementar emissão e validação de tokens JWT para proteger endpoints. |
| Avançado | Autenticação e autorização avançada | Proteger rotas com middlewares e aplicar regras de acesso por perfil de usuário. |
| Avançado | Permissões por papel | Diferenciar acessos entre perfis, como administrador e usuário comum. |
| Avançado | Mensageria e tarefas em background | Usar Celery com Redis para processar lembretes ou tarefas assíncronas sem bloquear a API. |