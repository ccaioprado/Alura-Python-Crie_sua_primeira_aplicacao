admin = 'admin123'

senha = 'senha321'

admin_entrada = input('Digite seu user: ')

senha_entrada = input('Digite sua senha: ')

if admin_entrada == admin and senha_entrada == senha:
    print('Você acessou o sistema')
else:
    print('Usuário e/ou senha incorretos')