- [FacebookClone](#facebookclone)
- [Features](#features)
    - [Usuarios](#usuarios)
    - [Relacionamentos](#relacionamentos)
    - [Postagens](#postagens)
    - [Comentários](#comentários)
    - [Grupos](#grupos)

# FacebookClone

Repositorio usado para a disciplina de Banco de Dados da UFPB.

# Features

## Usuarios

> Um usuario mantem um perfil com nome, foto, cidade onde vive, mural amizades e grupos.

- [x] Criar usuário


> O usuário pode definir a visibiliadde das informações do seu perfil: para amigos; para amigos e amigos de amigos; ou pública.

- [x] Atualizar privacidade

> Um usuário pode listar todos os usuários e grupos da rede social, para que ele possa fazer novos amigos ou participar de grupos, porém não devem ser exibidos grupos ou usuarios que lhe bloquearam

- [x] Listar usuario
- [x] Listar grupos

## Relacionamentos

> Para duas pessoas se tornarem amigas, uma visita o perfil da outra e envia-lhe um pedido de amizsade, cabendo à segunda aceitar ou rejeitar o pedido.

- [x] Listar pedidos de amizade
- [x] Aceitar pedido de amizade
- [x] Rejeitar pedido de amizade
- [x] Pedir amizade

> Quando se está visitando o perfil de alguém, se a visibilidade do perfil desta pessoa permitir, [...] a listagem completa dos amigos devem estar indicados

- [x] Listar amizades

> Quando se está visitando o perfil de alguém, se a visibilidade do perfil desta pessoa permitir, [...] os amigos em comum que se tem com esta pessoa devem estar indicados

- [ ] Listar amizades comuns

> Um usuario pode bloquear outro usuario da rede social

> Apenas o usuário que realizou o bloqueio podeŕa removelo

- [x] Atualizar bloqueio usuario

## Postagens

> Em seu mural um usuário pode postar textos e fotos

> O moral do grupo é coletivo, pois todos os participantes do grupo podem postar fotos e textos [...]

- [ ] Criar postagem

> Podem apagar postagens, comentários e respostas, os autores dos conteúdos e o dono do perfil

> Podem apagar conteudos do mural do grupo os autores do conteudos e administradores.

- [ ] Deletar postagem

## Comentários

> Cada postagem no mural pode ter comentários e cada comentário [...]

- [ ] Postar comentario

> Podem apagar postagens, comentários e respostas, os autores dos conteúdos e o dono do perfil

> Podem apagar conteudos do mural do grupo os autores do conteudos e administradores.

- [ ] Deletar comentario

> [...] e cada comentário pode ter respostas a ele

- [ ] Responder comentario

## Grupos

> Os usuários da rede social podem criar e participar de grupos.

- [x] Criar grupos

> Para participar de um grupo, um usuário deve solicitar sua entrada no grupo, cabendo aos administradores aprovar ou rejeitar a soliticação.

- [ ] Listar pedidos de participação
- [ ] Aceitar pedido de participação
- [ ] Rejeitar pedido de participação
- [ ] Pedir participação

> Um administrador pode tornar administrador qualquer párticipe do gurpo, bem como fazer o inverso.

- [ ] Atualizar status de administrador

> Os administradores também podem remover qualquer membro do grupo, podendo o usuario removido solicitar novamente participação no grupo.

- [ ] Remover participante

> Os administradores podem ainda bloquear qualquer membro do grupo, ficando o membro bloqueado impedido de visualizar o grupo, e consequentemente, de solicitar participação do grupo, até que um administrador faça o desbloqueio do usuário.

- [ ] Atualizar bloqueio de participante
