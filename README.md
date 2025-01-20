# Instruções para utilizar os script de análise

## Requisitos
- Docker

## Instruções

É importante que os comandos abaixo sejam executados na raiz no projeto!

1 - Copiar o arquivo de varíáveis de ambiente e preencher os dados necessários

```
cp .env-example .env
```

2 - Levantar os contêineres
```
docker compose up -d

--- OU ---

./run up
```

3 - Acessar o Jupyter notebook