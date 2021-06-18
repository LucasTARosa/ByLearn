from reportlab.lib import colors  # Trabalhar com cores
from reportlab.lib.pagesizes import A4  # (210*mm,297*mm)
from reportlab.lib.units import cm, inch, mm  # Padrão = Points
from reportlab.pdfbase import pdfmetrics  # Usamos para registrar a fonte
from reportlab.pdfbase.ttfonts import TTFont  # Criar a fonte em si
from reportlab.pdfgen import canvas  # Onde 'desenhamos' no PDF

# Seta se o debug está ativo (para mostrar tamanho e régua)
DEBUG = False

def mostrar_tamanho():
    """Mostra os tamanhos de mm, cm e polegada convertidos para pontos"""

    print(f'1 mm vale {mm} pontos')
    print(f'1 cm vale {cm} pontos')
    print(f'1 polegada vale {inch} pontos')


def desenhar_regua(pdf_canvas, pagina_tamanho):
    """Desenha uma régua para facilitar entender a posição de cada elemento

    Args:
        pdf_canvas: O Canvas que você está trabalhando
        pagina_tamanho: O tamanho da página atual
    """
    pdf_canvas.setFontSize(8)
    pagina_tamanho_y = int(pagina_tamanho[1] / cm)
    pagina_tamanho_x = int(pagina_tamanho[0] / cm)

    for y in range(pagina_tamanho_y + 1):
        pdf_canvas.drawString(0 * cm, y * cm, f'y{y}')

    for x in range(pagina_tamanho_x + 1):
        pdf_canvas.drawString(x * cm, 0 * cm, f'x{x}')

def mostrar_fontes_disponíveis(pdf_canvas):
    """Mostra todas as fontes disponíveis para uso"""

    print(pdf_canvas.getAvailableFonts())

def registrar_fonte(titulo_fonte, arquivo_fonte):
    """Registra fontes para serem utilizadas"""
    pdfmetrics.registerFont(TTFont(titulo_fonte, arquivo_fonte))

# Só entra no IF se executarmos o arquivo diretamente
if __name__ == '__main__':

    # Valores do arquivo
    nome_arquivo = 'Curso de PDF com boas práticas.pdf'
    titulo_arquivo = 'Integrando o Python com PDF'
    tamanho_pagina_arquivo = A4

    # Configura o PDF
    pdf_canvas = canvas.Canvas(nome_arquivo, pagesize=tamanho_pagina_arquivo)
    pdf_canvas.setTitle(titulo_arquivo)

    # Valores do título e subtítulo
    titulo_conteudo = 'ByLearn Apresenta:'
    subtitulo_conteudo = 'Aprenda a manipular arquivos PDF com o Python'

    # Configura o Título
    registrar_fonte('OpenSans', 'OpenSans-Regular.ttf')
    pdf_canvas.setFont('OpenSans', 36)
    pdf_canvas.drawCentredString((210*mm)/2, (27) * cm, titulo_conteudo)

    # Configura o Subtítulo
    pdf_canvas.setFillColorRGB(0, 0, 1.0)
    pdf_canvas.setFont('Courier-Bold', 20)
    pdf_canvas.drawCentredString((210*mm)/2, (25.5) * cm, subtitulo_conteudo)

    # Desenha a linha divisória
    pdf_canvas.line(0.5 * cm, 25 * cm, 20.5 * cm, 25 * cm)

    # Valores do corpo do PDF
    conteudo_curso = [
        'Neste curso você aprenderá: ',
        '- Extrair informações de PDF Existente',
        '- Extrair Texto de PDF Existente',
        '- Juntar PDFS (Merge)',
        '- Rotacionar Páginas',
        '- Dividir PDFs (Split)',
        '- Adicionar Senha ',
        '- Trabalhando com arquivos com senha ',
        '- Gerar PDF através de arquivo html ou url',
        '- Criar um PDF do Zero'
    ]

    # Configuração do corpo do PDF
    texto = pdf_canvas.beginText(1.5 * cm, 24 * cm)
    texto.setFont('Courier', 18)
    texto.setFillColor(colors.darkgreen)

    for linha in conteudo_curso:
        texto.textLine(linha)

    pdf_canvas.drawText(texto) # Funciona com textos longos, como Listas de Texto

    # Valores da imagem
    logo_bylearn = 'bylearn.jpg'

    # Configuração da imagem
    pdf_canvas.drawImage(logo_bylearn, 6*cm, 7*cm)
    
    # Configurando a página 2
    pdf_canvas.showPage()

    # Valores de agradecimento
    agradecimento_titulo = 'Muito Obrigado Pela Atenção!'
    agradecimento_subtitulo = 'Nos vemos no próximo curso da ByLearn :)'

    # Configuração do agradecimento
    pdf_canvas.setFont('OpenSans', 36)
    pdf_canvas.drawCentredString((210*mm)/2, (29.7/2) * cm + 25, agradecimento_titulo)
    pdf_canvas.setFontSize(28)
    pdf_canvas.drawCentredString((210*mm)/2, (29.7/2) * cm - 25, agradecimento_subtitulo)

    # Mostrando informações de Debug
    if DEBUG:
        pdf_canvas.showPage()
        mostrar_tamanho()
        desenhar_regua(pdf_canvas, tamanho_pagina_arquivo)

    # Salvando o arquivo
    pdf_canvas.save()
