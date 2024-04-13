import os

def create_clean_architecture_structure(base_dir):
    # Diretórios principais
    app_dir = os.path.join(base_dir, 'app')
    config_dir = os.path.join(base_dir, 'config')
    tests_dir = os.path.join(base_dir, 'tests')
    infra_dir = os.path.join(base_dir, 'infrastructure')

    # Diretórios dentro de 'app'
    adapters_dir = os.path.join(app_dir, 'adapters')
    entities_dir = os.path.join(app_dir, 'entities')
    use_cases_dir = os.path.join(app_dir, 'use_cases')
    repositories_dir = os.path.join(adapters_dir, 'repositories')
    interfaces_dir = os.path.join(adapters_dir, 'interfaces')
    controllers_dir = os.path.join(adapters_dir, 'controllers')
    gateways_dir = os.path.join(adapters_dir, 'gateways')

    # Lista de diretórios a serem criados
    directories = [
        app_dir, config_dir, tests_dir,
        adapters_dir, entities_dir, use_cases_dir,
        repositories_dir, interfaces_dir, controllers_dir, gateways_dir
    ]

    # Criar os diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        init_file = os.path.join(directory, '__init__.py')
        with open(init_file, 'w') as f:
            f.write('')

if __name__ == '__main__':
    # Diretório base onde a estrutura será criada (pode ser alterado conforme necessário)
    base_directory = os.getcwd()  # Diretório atual onde o script está sendo executado
    create_clean_architecture_structure(base_directory)
    print('Estrutura de pastas criada com sucesso!')