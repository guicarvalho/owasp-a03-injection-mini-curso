# OWASP a03-Injection

Projeto educacional criado para ilustrar as vulnerabilidades de injeção de código durante o evento da semana de tecnologia da FATEC Araraquara.

## Dependências

- Python
- Django
- SQLite

## Executando o projeto

Crie o ambiente virtual para instalar as bibliotecas utilizadas no projeto:

```sh
python -m venv .env
. .env/bin/activate   # caminho no Windows: .env\venv\activate
pip install -r requirements.txt
```

Após instalar todas as bibliotecas, vamos criar o banco de dados e rodar o servidor de aplicação:

```sh
python manage.py migrate
python manage.py loaddata users.json
python manage.py runserver
```

### Material

PPT: [Slides](https://docs.google.com/presentation/d/1zvVHAjAj0KowNEWxS7_aqof61-VXIj-GXbjUV65SWmU/edit?usp=sharing)
