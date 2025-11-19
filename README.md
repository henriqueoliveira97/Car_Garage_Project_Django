🚗 AutoTech - Sistema de Gestão de Oficina em Django

O AutoTech é uma aplicação web desenvolvida em Django que permite gerir uma oficina automóvel de forma moderna e eficiente.
Com ela, é possível:

-Registar clientes, viaturas e reparações.
-Associar mecânicos e peças a cada reparação.
-Calcular automaticamente o custo total de cada serviço.
-Permitir que os clientes acompanhem o estado da reparação da sua viatura online.

O objetivo é digitalizar o processo de gestão de uma oficina, tornando-o mais transparente tanto para o cliente.

⚙️ Funcionalidades Principais
✅ Registo e autenticação de utilizadores (clientes e mecânicos)
✅ Registo de viaturas associadas a clientes
✅ Criação e acompanhamento de reparações
✅ Gestão de peças e custos através de relações ManyToMany
✅ Área de administração completa no Django Admin
✅ Acompanhamento online do estado da reparação pelo cliente

🚀 Como Executar o Projeto Localmente
-Clona o repositório
git clone https://github.com/henriqueoliveira97/Car_Garage_Project_Django.git
cd Car_Garage_Project_Django

-Cria e ativa o ambiente virtual
python -m venv venv
venv\Scripts\activate   # no Windows
ou
source venv/bin/activate   # no Linux/Mac

-Instala as dependências
pip install -r requirements.txt

-Aplica as migrações
python manage.py makemigrations
python manage.py migrate

-Cria um superutilizador (para aceder ao admin)
python manage.py createsuperuser


-Corre o servidor
python manage.py runserver
