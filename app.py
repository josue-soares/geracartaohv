from flask import Flask, request, send_file, Response, render_template
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cartao_de_visita', methods=['POST'])
def cartao_de_visita():
    # Obtém os dados do formulário
    nome = request.form['nome']
    telefone = request.form['telefone']

    # Carrega a imagem
    img = Image.open("cartao_de_visita.png")

    # Define a fonte e o tamanho do texto
    fonte = ImageFont.truetype("arial.ttf", 24)

    # Obtém as dimensões da imagem e do texto
    largura, altura = img.size
    tamanho_nome = fonte.getsize(nome)
    tamanho_telefone = fonte.getsize(telefone)

    # Calcula a posição central do texto na horizontal
    posicao_x_nome = (largura - tamanho_nome[0]) // 2
    posicao_x_telefone = (largura - tamanho_telefone[0]) // 2

    # Calcula a posição do texto na metade superior da imagem
    posicao_y_nome = 925
    posicao_y_telefone = 950

    # Cria um objeto ImageDraw para desenhar o texto na imagem
    draw = ImageDraw.Draw(img)

    # Define a cor da fonte como branca
    cor = (255, 255, 255)

    # Insere o nome na imagem
    draw.text((posicao_x_nome, posicao_y_nome), nome, font=fonte, fill=cor)

    # Insere o telefone na imagem
    draw.text((posicao_x_telefone, posicao_y_telefone), telefone, font=fonte, fill=cor)

    # Salva a imagem em memória
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Retorna a imagem como resposta para download
    return Response(img_io.getvalue(), mimetype='image/png', headers={
        'Content-Disposition': f'attachment;filename=cartao_de_visita_modificado.png'
    })

if __name__ == '__main__':
    app.run(debug=True)
