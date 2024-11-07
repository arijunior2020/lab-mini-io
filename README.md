# 🚀 Laboratório de Armazenamento de Objetos com MinIO, Terraform e Docker

Este repositório contém o projeto de um laboratório construído para explorar o uso do **MinIO** como solução de armazenamento de objetos, utilizando **Terraform** para provisionamento na AWS e **Docker** para o gerenciamento de contêineres.

## 📝 Descrição

Neste laboratório, criamos uma aplicação de upload de arquivos que usa o **MinIO** como backend de armazenamento, simulando um ambiente de armazenamento de objetos similar ao S3 da AWS. A aplicação é composta por três contêineres:
- **Frontend** 🌐: Interface em HTML e CSS para facilitar o upload de arquivos.
- **Backend** 🔙: API construída em Python (Flask) para receber os uploads e enviar os arquivos ao MinIO.
- **MinIO** 🗄️: Solução de armazenamento de objetos compatível com a API S3.

O provisionamento da infraestrutura é feito com Terraform, e a configuração do ambiente com Docker. Abaixo estão todos os detalhes de como configurar e executar este laboratório.

## 📦 Estrutura do Projeto

```plaintext
├── app/
│   ├── app.py               # Código do backend em Flask
│   ├── Dockerfile           # Dockerfile do backend
│   ├── requirements.txt     # Dependências do backend
├── frontend/
│   ├── index.html           # Interface de upload de arquivos
├── terraform/
│   ├── main.tf              # Configuração principal do Terraform para provisionamento AWS
├── docker-compose.yml       # Configuração do Docker Compose
└── README.md                # Documentação do projeto
```

## 🛠️ Tecnologias Utilizadas

- **Terraform** para provisionamento de infraestrutura na AWS
- **Docker** para contêineres e isolamento de serviços
- **Flask** (Python) para o backend da aplicação
- **MinIO** para armazenamento de objetos compatível com S3
- **HTML/CSS/JavaScript** para o frontend da aplicação

## 🌐 Infraestrutura

A infraestrutura foi provisionada com Terraform na AWS:

- **Instância EC2**: Servidor onde os contêineres foram executados.
- **User Data**: Script para instalar o Docker automaticamente na inicialização da instância EC2.
- **Provisioner File**: Transferência de arquivos locais para a instância EC2 para configurar o ambiente.

## 📋 Pré-requisitos

- Terraform instalado
- AWS CLI configurado com permissões adequadas
- Docker e Docker Compose instalados

## ⚙️ Configuração e Execução

1. ## Provisionar a Instância EC2 com Terraform
   
No diretório terraform/, configure as variáveis necessárias para a instância EC2 (região, chave SSH, etc.).

Execute os comandos:

```
terraform init
terraform apply
```
Isso criará uma instância EC2 com Docker instalado, configurada para receber os arquivos da aplicação via provisioner.

1. ## Configurar e Executar o Ambiente com Docker Compose
   
Transfira os arquivos da aplicação para a instância EC2 (ou use o provisioner do Terraform).

Na instância, inicie o ambiente com:

```
docker-compose up --build -d
```

Isso iniciará três contêineres:

**frontend**: Interface web para upload de arquivos.
**backend**: API Flask para receber e processar os uploads.
**minio**: Servidor MinIO para armazenar os arquivos.

1. ## Acessar o Laboratório
   
Acesse o Frontend em http://<EC2_PUBLIC_IP>:8080 para fazer upload de arquivos.
Acesse a interface de administração do MinIO em http://<EC2_PUBLIC_IP>:9001 com as credenciais configuradas (usuário: admin, senha: password).

## 📂 Organização dos Contêineres

- frontend: Servido via Nginx na porta 8080.
- backend: API Flask na porta 5000.
- minio: Servidor MinIO na porta 9000 (API) e 9001 (Web UI).

## 🔒 Segurança e Controle de Acesso no MinIO

O MinIO oferece compatibilidade com a API S3 e permite a aplicação de políticas para controle de acesso. No laboratório, você pode criar uma política personalizada para restringir ou permitir acessos específicos aos buckets.

Exemplo de política de leitura pública para todos os objetos no bucket uploads:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::uploads/*"]
    }
  ]
}
```

### 💡 Conclusão

Este laboratório foi construído para explorar a compatibilidade S3 do MinIO e simular uma aplicação de upload de arquivos com infraestrutura autônoma. Foi possível aprender sobre provisionamento de infraestrutura com Terraform, configuração de contêineres Docker e controle de armazenamento com MinIO.

Sinta-se à vontade para experimentar e estender esse laboratório com recursos adicionais, como versionamento de objetos, replicação, notificações de eventos e políticas avançadas de controle de acesso.