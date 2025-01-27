import os
import time
from uuid import uuid4
import subprocess

def generate_curriculum(name, email, celphone, experience, resume):
    # Gera um identificador único para arquivos
    unique_id = uuid4()

    # Caminhos para os arquivos
    template_path = 'latex_templates/base_template.tex'
    output_tex = f'latex_templates/generated_curriculum_{unique_id}.tex'
    final_output = f'latex_templates/generated_curriculum_{unique_id}.pdf'

    # Lê o template e substitui os placeholders
    with open(template_path, 'r') as f:
        template = f.read()
    
    filled_template = (
        template.replace('<name>', name)
                .replace('<email>', email)
                .replace('<celphone>', celphone)
                .replace('<experience>', experience)
                .replace('<resume>', resume)
    )

    # Escreve o template preenchido em um novo arquivo .tex
    with open(output_tex, 'w') as f:
        f.write(filled_template)

    # Chama o pdflatex para gerar o PDF
    try:
        subprocess.run(
            ['pdflatex', '-output-directory=latex_templates', output_tex],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao gerar o PDF: {e.stderr.decode()}")

    time.sleep(2)
    # Verifica se o arquivo PDF foi gerado
    if not os.path.exists(final_output):
        raise FileNotFoundError(f"Erro: O PDF não foi gerado em {final_output}")

    # Retorna o caminho do PDF gerado
    return final_output




# import os
# from uuid import uuid4

# async def generate_curriculum(name, email, celphone, experience, resume):
#     unique_id = uuid4()

#     template_path = 'latex_templates/base_template.tex'
    
#     with open(template_path, 'r') as f:
#         template = f.read()

#         template = template.replace('<name>', name)
#         template = template.replace('<email>', email)
#         template = template.replace('<celphone>', celphone)
#         template = template.replace('<experience>', experience)
#         template = template.replace('<resume>', resume)

#     output_tex = f'latex_templates/generated_curriculum_{unique_id}.tex'
#     final_output = f'generate_curriculum_{unique_id}.pdf'

#     with open(output_tex, 'w') as f:
#         f.write(template)

     
#     os.system(f'pdflatex {output_tex}')

#     # output_pdf = output_tex.replace('.tex', '.pdf')

#     return final_output 