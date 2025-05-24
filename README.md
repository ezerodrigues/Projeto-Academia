# Projeto Academia - Cálculo de IMC e Ficha PDF

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Funcional-success)
![Licença](https://img.shields.io/badge/Licença-MIT-green)

## 📋 Descrição do Projeto

Este é um projeto simples em Python desenvolvido para demonstrar a coleta de dados de um aluno (nome, idade, peso e altura) através do console, o cálculo do Índice de Massa Corporal (IMC) e a geração automática de uma ficha de aluno personalizada em formato PDF. A ficha (`ficha_aluno.pdf`) é criada utilizando um template Pug (`template.pug`) para estruturar e estilizar as informações, incluindo o status do IMC (dentro do peso ou sobrepeso).

## 🎯 Funcionalidades

- **Coleta de Dados Interativa**: Solicita ao usuário que insira nome, idade, peso e altura via terminal.
- **Cálculo de IMC**: Calcula o IMC com base no peso e altura fornecidos.
- **Classificação do IMC**: Determina se o aluno está "dentro do peso" ou com "sobrepeso" (baseado em um limite simples de IMC > 25).
- **Geração de PDF**: Cria um arquivo `ficha_aluno.pdf` contendo os dados do aluno, seu IMC calculado e o status correspondente.
- **Template Personalizado**: Utiliza um arquivo `template.pug` para definir a estrutura e o visual do PDF gerado, permitindo fácil customização.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal.
- **pdf_reports**: Biblioteca Python utilizada para gerar relatórios em PDF a partir de templates HTML/Pug. (Nota: A instalação desta biblioteca pode ser necessária).
- **Pug**: Linguagem de template utilizada para criar a estrutura do arquivo PDF final.

## 📦 Pré-requisitos

Antes de executar o projeto, você precisará ter instalado em seu sistema:

- Python 3.x
- Pip (gerenciador de pacotes Python)

## ⚙️ Instalação e Execução

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/ezerodrigues/Projeto-Academia.git
    ```

2.  **Navegue até o Diretório do Projeto:**
    ```bash
    cd Projeto-Academia
    ```

3.  **Instale as Dependências:**
    Este projeto depende da biblioteca `pdf_reports`. Instale-a usando pip:
    ```bash
    pip install pdf_reports
    ```
    *(Observação: Se houver um arquivo `requirements.txt` ou configuração de `Poetry`, siga as instruções específicas dele.)*

4.  **Execute o Script Principal:**
    ```bash
    python Business_Case_Academia.py
    ```

5.  **Interaja com o Script:**
    O script solicitará que você digite as informações do aluno (nome, idade, peso, altura) no terminal.

6.  **Verifique o Resultado:**
    Após fornecer os dados, o script gerará o arquivo `ficha_aluno.pdf` no mesmo diretório. Abra este arquivo para visualizar a ficha do aluno com o cálculo do IMC.

## 📁 Estrutura de Arquivos

```
Projeto-Academia/
│
├── Business_Case_Academia.py  # Script principal Python
├── template.pug               # Template Pug para o PDF
├── ficha_aluno.pdf            # Exemplo de PDF gerado (ou será gerado na execução)
└── README.md                  # Este arquivo
```

## 👨‍💻 Autor

**Eliézer Rodrigues**

- GitHub: [ezerodrigues](https://github.com/ezerodrigues)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE (se disponível no repositório) para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
