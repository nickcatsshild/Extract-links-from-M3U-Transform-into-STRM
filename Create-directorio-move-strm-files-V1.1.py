import os
import shutil

# Defina o diretório onde os arquivos .strm estão localizados
strm_dir = 'Strm'

# Verifique se o diretório Strm existe
if not os.path.exists(strm_dir):
    print(f'O diretório "{strm_dir}" não foi encontrado.')
    exit(1)

# Itere sobre todos os arquivos no diretório Strm
for filename in os.listdir(strm_dir):
    if filename.endswith('.strm'):
        # Nome do arquivo sem a extensão .strm
        nome_filme = os.path.splitext(filename)[0]

        # Caminhos completos do arquivo .strm e do novo diretório
        strm_filepath = os.path.join(strm_dir, filename)
        movie_folder = os.path.join(strm_dir, nome_filme)

        # Crie o diretório se não existir
        if not os.path.exists(movie_folder):
            os.makedirs(movie_folder)

        # Caminho para mover o arquivo .strm para dentro do novo diretório
        new_strm_filepath = os.path.join(movie_folder, filename)

        # Mover o arquivo .strm para o novo diretório
        shutil.move(strm_filepath, new_strm_filepath)

print('.strm files moved successfully into their respective directories.')
