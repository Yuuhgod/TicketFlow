# Sistema de Chamados para Empresa de Desenvolvimento de Software

## Descrição
Este é um sistema de gerenciamento de chamados desenvolvido para facilitar o processo de suporte e resolução de problemas para clientes da nossa empresa de desenvolvimento de software. Ele permite que os clientes relatem problemas, solicitem novos recursos e acompanhem o progresso de suas solicitações.

## Funcionalidades Principais
- **Registro de Usuários:** Clientes podem se registrar para acessar o sistema.
- **Criação de Chamados:** Os clientes podem criar novos chamados relatando problemas ou solicitando novos recursos.
- **Acompanhamento de Chamados:** Os clientes podem acompanhar o status e o progresso de seus chamados.
- **Atribuição de Técnicos:** Os chamados são automaticamente atribuídos a técnicos disponíveis ou podem ser atribuídos manualmente pelos administradores.
- **Priorização de Chamados:** Os chamados podem ser classificados com diferentes níveis de prioridade para garantir uma resposta rápida aos problemas críticos.
- **Comentários e Notificações:** Os clientes e técnicos podem adicionar comentários aos chamados e receber notificações sobre atualizações.
- **Histórico de Chamados:** O sistema mantém um histórico completo de todos os chamados, incluindo detalhes sobre a resolução e o tempo de resposta.

## Como Usar
1. **Registro:** Os clientes devem se registrar usando seu endereço de e-mail e criar uma senha.
2. **Login:** Após o registro, os clientes podem fazer login usando suas credenciais.
3. **Criação de Chamados:** Na página inicial, os clientes têm a opção de criar um novo chamado, fornecendo detalhes sobre o problema ou solicitação.
4. **Acompanhamento de Chamados:** Os clientes podem visualizar todos os chamados que criaram e acompanhar seu status e progresso.
5. **Interagir com Chamados:** Os clientes podem adicionar comentários aos chamados existentes e interagir com os técnicos responsáveis.
6. **Resolução de Chamados:** Os técnicos recebem notificações sobre novos chamados e trabalham para resolvê-los o mais rápido possível.

## Tecnologias Utilizadas
- **Backend:** Node.js, Express.js, MongoDB
- **Frontend:** React.js, Bootstrap
- **Autenticação:** JWT (JSON Web Tokens)
- **Comunicação em Tempo Real:** Socket.io

## Pré-requisitos
- Node.js e npm instalados
- MongoDB rodando localmente ou em uma instância na nuvem

## Instalação
1. Clone este repositório: `git clone <https://github.com/Yuuhgod/SistemadeChamado.git>`
2. Instale as dependências do backend: `cd backend && npm install`
3. Instale as dependências do frontend: `cd frontend && npm install`
4. Configure as variáveis de ambiente necessárias (consulte o arquivo `.env.example`)
5. Inicie o servidor backend: `npm start`
6. Inicie o servidor frontend: `npm start`

## Contribuindo
Sinta-se à vontade para enviar pull requests e sugerir melhorias. 

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE).



