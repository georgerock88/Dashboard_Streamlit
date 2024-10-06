import EXERCICIO_2_DASHBOARD_2024

# Agora você pode usar as funções e variáveis definidas no notebook

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Caminho do arquivo
notebook_path = r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\EXERCICIO_2_DASHBOARD_2024.ipynb"

# Carregar o notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Criar um processador para executar o notebook
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

# Executar o notebook
ep.preprocess(nb, {'metadata': {'path': './'}})

# Agora você pode usar as variáveis e funções definidas no notebook

