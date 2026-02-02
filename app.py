from flask import Flask, render_template_string

app = Flask(__name__)

# Lista de produtos corrigida
produtos = [
    # --- CASA ---
    {
        "titulo": "Copo térmico gigante 1,2L",
        "preco": "R$ 49,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_620176-MLB104273894494_012026-F-copo-termico-gigante-12l-inox-com-tampa-e-canudo.webp", 
        "link": "https://mercadolivre.com/sec/2eBPaet", 
        "categoria": "casa"
    },
    {
        "titulo": "Fritadeira sem óleo Air Fryer 4L Mondial", 
        "preco": "R$ 268,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_775407-MLA99776749612_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/1agqeTX", 
        "categoria": "casa"
    },
    {   "titulo": "Conjunto Panelas Antiaderente 10 Peças Teflon Várias Cores",
        "preco": "R$ 189,00",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_784556-MLB75962100686_052024-F-conjunto-panelas-antiaderente-10-pecas-teflon-varias-cores.webp",
        "link": "https://mercadolivre.com/sec/2qGJMst",
        "categoria": "casa"
    },
    {   
        "titulo": "Mop Flash Limp Mop Giratório Fit com balde centrífuga Cinza-escuro",
        "preco": "R$ 69,90",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_646002-MLA99406426656_112025-F.webp",
        "link" : "https://mercadolivre.com/sec/1DTHqCR",
        "categoria": "casa"
    },
    {   
        "titulo": "Kit 2 Lustre Luminária Pendente Para Balcão De Cozinha Mini Pequim Cor Fendi 24 Cm Iluminar Ambiente",
        "preco": "R$115,34",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_665120-MLA99859032031_112025-F.webp",
        "link"  : "https://mercadolivre.com/sec/1UYGUk4",
        "categoria": "casa"
    },
    {   
        "titulo": "Jogo Lençol Casal 3pç 400 Fios Hipercal Conforto Macio Cor Cinza Desenho do tecido Liso",
        "preco": "R$ 35,81", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_623437-MLA100086251965_122025-F.webp", 
        "link"  : "https://mercadolivre.com/sec/2eXAEWc", 
        "categoria": "casa"
    },
    {   
        "titulo": "Aparelho de Jantar e Chá Ryo Maresia 20 Peças Branco e Marrom Oxford", 
        "preco": "R$ 339,90", 
        "imagem":"https://http2.mlstatic.com/D_NQ_NP_2X_619198-MLA96107579199_102025-F.webp",
        "link" : "https://mercadolivre.com/sec/2ro33LN", 
        "categoria": "casa"
    },
    {   
        "titulo": "Kit 4 Organizador De Geladeira 2l Acrílico Frutas E Verduras Transparente",
        "preco":  "R$ 68,87", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_857413-MLB84509903752_052025-F.webp", 
        "link" :  "https://mercadolivre.com/sec/2MrMsU9",
        "categoria": "casa"
    },
    {   
        "titulo": "Tapete 2,00x1,50 Peludo Felpudo Sala E Quarto Cores Cor Bege-mesclado Desenho Do Tecido Pelo Alto Casa Laura Enxovais Tapete Médio Para Sala", 
        "preco": "R$ 62,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_755662-MLA99498152944_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2TtBMhS",
        "categoria" : "casa"
    },
    {   
        "titulo": "Liquidificador Philco 1200W 3L 12 Velocidades Preto PH900",
        "preco": "R$ 122,57", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_857659-MLA98259160111_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2bpeTVm", 
        "categoria": "casa"
    },
    {   
        "titulo": "Kit 4 Capas De Almofadas Decorativas Com Zíper 42 X 42 Cm 09 Cor Verde-escuro Cor 31", 
        "preco": "R$ 32,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_932601-MLA100084463137_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/29nKjS8", 
        "categoria": "casa"
    },
    {   
        "titulo": "Conjunto de 6 Copos Vidro 450ml Califórnia Praticasa Transparente", 
        "preco": "R$ 39,15", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_964593-MLA99614676300_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/1ptsfgj", 
        "categoria": "casa"
    },

    # --- MODA ---
    {
        "titulo": "Camisa Casual Slim", 
        "preco": "R$ 46,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_942962-MLB90363960505_082025-F-kit-2-camiseta-americana-canelada-ribana-algodo-justa-slim.webp", 
        "link": "https://mercadolivre.com/sec/2qatTHa", 
        "categoria": "moda"
    },
    {
        "titulo": "Kit 3 Calça Jeans Skinny Masculina Com Lycra Estica Muito Nf", 
        "preco": "R$ 129,19", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_844444-MLB99168165420_112025-F-kit-3-calca-jeans-skinny-masculina-com-lycra-estica-muito-nf.webp", 
        "link": "https://mercadolivre.com/sec/1nSFiKo", 
        "categoria": "moda"
    },
    {
        "titulo": "Vestido Feminino Midi Elegante Floral Moda Evangélica", 
        "preco": "R$ 69,46", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_626715-MLB96659591940_112025-F-vestido-feminino-midi-elegante-floral-moda-evangelica.webp", 
        "link": "https://mercadolivre.com/sec/2P11uZj", 
        "categoria": "moda"
    },
    {
        "titulo": "Jaqueta Alta Performance Leve Proteção Uv Treino Academia", 
        "preco": "R$ 120,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_949065-MLB86829802986_072025-F-jaqueta-alta-performance-leve-proteco-uv-treino-academia.webp", 
        "link": "https://mercadolivre.com/sec/1ybwhMF", 
        "categoria": "moda"
    },
    {
        "titulo": "Smartwatch Xiaomi Redmi Watch 5 Active Tela Lcd 2.00 Preto", 
        "preco": "R$ 236,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_949046-MLA99507276886_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2cZbnB2", 
        "categoria": "moda"
    },
    {
        "titulo": "Kit Bolsas Feminina Sacola Transversal Tira Colo Carteira", 
        "preco": "R$ 99,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_941814-MLB106275973405_012026-F-kit-bolsas-feminina-sacola-transversal-tira-colo-carteira.webp", 
        "link": "https://mercadolivre.com/sec/2CgpV9P", 
        "categoria": "moda"
    },
    {
        "titulo": "Kit 4 Camiseta Dry-fit Sandrini Masculina Academia Caminhada", 
        "preco": "R$ 76,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_626928-MLB82004918446_022025-F-kit-4-camiseta-dry-fit-sandrini-masculina-academia-caminhada.webp", 
        "link": "https://mercadolivre.com/sec/1VAv5nQ", 
        "categoria": "moda"
    },
    {
        "titulo": "Óculos De Sol Quadrado Preto Fosco Unissex Proteção Uv400", 
        "preco": "R$ 46,04", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_973375-MLB93487816021_092025-F-oculos-de-sol-quadrado-preto-fosco-unissex-proteco-uv400.webp", 
        "link": "https://mercadolivre.com/sec/22MeWGR", 
        "categoria": "moda"
    },
    {
        "titulo": "Cinto Masculino Couro Legítimo Ferracini Verona Fc 565", 
        "preco": "R$ 74,49", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_886368-MLB69940267143_062023-F-cinto-masculino-couro-legitimo-ferracini-verona-fc-565.webp", 
        "link": "https://mercadolivre.com/sec/1CZcbh9", 
        "categoria": "moda"
    },
    {
        "titulo": "Moletom Liso Algodão Unissex Blusa De Frio Canguru Flanelado", 
        "preco": "R$ 47,34", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_710995-MLB77244233388_072024-F-moletom-liso-algodo-unissex-blusa-de-frio-canguru-flanelado.webp", 
        "link": "https://mercadolivre.com/sec/1V1yiCg", 
        "categoria": "moda"
    },
    {
        "titulo": "Sandália Rasteirinha Feminina H Simples Elegante Casual", 
        "preco": "R$ 45,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_882947-MLB104798834954_012026-F-sandalia-rasteirinha-feminina-h-simples-elegante-casual.webp", 
        "link": "https://mercadolivre.com/sec/1nVvU4A", 
        "categoria": "moda"
    },
    {
        "titulo": "Boné Ny New York Aba Curva Strapback", 
        "preco": "R$ 35,", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_984548-MLB89370363117_082025-F-bone-ny-new-york-aba-curva-strapback.webp", 
        "link": "https://mercadolivre.com/sec/295sueV", 
        "categoria": "moda"
    },

    # --- FERRAMENTAS ---
    {
        "titulo": "Martelete Furadeira Allmind 1200W Kamaré SDS Plus Impacto 5Kg", 
        "preco": "R$ 335,94", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_796432-MLA97975510381_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2n8fm9Y", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Jogo De Ferramentas 169 Peças Com Maleta E Furadeira Parafusadeira Sem Fio A Bateria Tb-12e 12v 3/8 10mm The Black Tools", 
        "preco": "R$ 289,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_936056-MLA99425564798_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2GjdAyx", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Kit Jogo De Ferramentas 129 Peças Com Jogo De 40 Soquetes Chaves E Kit 300 Peças Brocas E Buchas The Black Tools", 
        "preco": "R$ 189,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_618929-MLA99520369354_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2smPaaS", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Chave De Impacto Parafusadeira Furadeira Recarregável 48v Azul Several Importados 2000mah", 
        "preco": "R$ 256", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_982598-MLA105448104477_012026-F.webp", 
        "link": "https://mercadolivre.com/sec/2CX8fuU", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Trena de aço 5mx19mm Vonder econômica medição", 
        "preco": "R$ 19,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_798462-MLA100048916969_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/2unMmw9", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Kit Nível A Laser Verde 12 Linhas Esquadro + Suporte + Tripé Recarregavel Profissional Prumo Autonivelante Nano Bateria", 
        "preco": "R$ 89,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_609947-MLA100070739765_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/2maUjG1", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Alicate Universal Vonder 8 Pol", 
        "preco": "R$ 42,39", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_807084-MLA100072970361_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/1gszwv1", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Serra Circular Bosch 7.1/4 Para Madeira GKS 150 mais Guia e Disco de Corte 1500W", 
        "preco": "R$ 729,65", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_691458-MLA99453208022_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/1g4JpHq", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Mini esmerilhadeira angular Bosch Professional GWS 700 azul 710 W", 
        "preco": "R$ 299,20", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_670719-MLA99986706915_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2YVtKLg", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Martelo De Unha 27 Cm De Cabo De Fibra Emborrachado Ergonómico Luzilar Martelo De Unha", 
        "preco": "R$ 20,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_965337-MLA97402349830_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/1PrZAFb", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Caixa De Ferramentas Tática Cinza 18,3 Polegadas Metasul", 
        "preco": "R$ 36,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_651384-MLA99360086264_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/296ZC7X", 
        "categoria": "ferramentas"
    },
    {
        "titulo": "Alicate Pressão + Chave Inglesa + Grifo", 
        "preco": "R$ 71,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_736031-MLB88919983948_082025-F.webp", 
        "link": "https://mercadolivre.com/sec/1AEBG8Q", 
        "categoria": "ferramentas"
    },

    # --- ESPORTE ---
    {
        "titulo": "Tênis Esportivo", 
        "preco": "R$ 178,75", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_853410-MLB87242826822_072025-F-tnis-new-speed-esporte-masculino-100-original-caminhada.webp", 
        "link": "https://mercadolivre.com/sec/1aPVVFe", 
        "categoria": "esporte"
    },
    {
        "titulo": "Tatame Esteira Para Yoga Exercícios Físicos 1,80mx53cmx5mm Cor Preto", 
        "preco": "R$ 42,29", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_951298-MLA84849917275_052025-F.webp", 
        "link": "https://mercadolivre.com/sec/29iPY5D", 
        "categoria": "esporte"
    },
    {
        "titulo": "Kit 3 Faixas Elásticas Theraband Zornix Academia Exercício Treino Funcional", 
        "preco": "R$ 21,99", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_640754-MLA101914761165_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/2noXCBZ", 
        "categoria": "esporte"
    },
    {
        "titulo": "Garrafa Térmica Gocase Urban Inox Parede Dupla Isolada 500ml", 
        "preco": "R$ 70,30,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_703127-MLA99864871405_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/1TkhCoL", 
        "categoria": "esporte"
    },
    {
        "titulo": "Bola Para Futebol De Campo Bravo Xxiv Branco e Azul Penalty", 
        "preco": "R$ 76,62", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_877637-MLA99858457169_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2bbq6pY", 
        "categoria": "esporte"
    },
    {
        "titulo": "Corda De Pular Speed Rope Rolamento Cabo De Aço Profissional Rubber Fit Preto", 
        "preco": "R$ 21,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_710026-MLA104663682813_012026-F.webp", 
        "link": "", 
        "categoria": "esporte"
    },
    {
        "titulo": "Par de Halteres Hexagonal RMG8 Fit 2kg PVC Preto Emborrachado", 
        "preco": "R$ 59,90", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_795776-MLA96152982443_102025-F.webp", 
        "link": "https://mercadolivre.com/sec/1cWheQS", 
        "categoria": "esporte"
    },
    {
        "titulo": "Mochila Masculina Grande Notebook Impermeável Reforçada", 
        "preco": "R$ 60,12,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_615102-MLA99700960038_122025-F.webp", 
        "link": "https://mercadolivre.com/sec/2rxPgc9", 
        "categoria": "esporte"
    },
    {
        "titulo": "Bicicleta Aro 29 Gts Dexter 24 Marchas Freio A Disco Cor Branco Com Preto Tamanho Do Quadro 19", 
        "preco": "R$ 827,99 belo desconto", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_848325-MLA99453050974_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2hxcick", 
        "categoria": "esporte"
    },
    {
        "titulo": "Kit 2 Shorts De Compressão P/ Corrida Masculino Térmica", 
        "preco": "R$ 56,24", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_906889-MLB88368149898_072025-F-kit-2-shorts-de-compresso-p-corrida-masculino-termica.webp", 
        "link": "https://mercadolivre.com/sec/21qZ2h9", 
        "categoria": "esporte"
    },
    {
        "titulo": "Joelheira Compressão Ortopédica Ajustável Alívio Dor Tensor", 
        "preco": "R$ 19,00", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_876733-MLA99358545910_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2UxgGr4", 
        "categoria": "esporte"
    },
    {
        "titulo": "Óculos Natação Espelhado Leader Speed Pro Cor Preto",
        "preco": "R$ 67,42", 
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_843486-MLA99493085148_112025-F.webp", 
        "link": "https://mercadolivre.com/sec/2JAhGQr", 
        "categoria": "esporte"
    }
]

@app.route("/")
def home():
    template = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indicações do Renato</title>
    <style>
        body { margin: 0; font-family: 'Segoe UI', Arial, sans-serif; background: #111; color: #fff; }
        .topo { background: linear-gradient(180deg, #000 65%, #f5c400 100%); padding: 20px 10px; text-align: center; }
        .topo h1 { margin: 0; font-size: 28px; color: #f5c400; text-transform: uppercase; letter-spacing: 1px; }
        .topo p { font-size: 13px; opacity: 0.8; margin-top: 5px; }
        
        .categorias { display: flex; justify-content: center; gap: 10px; padding: 15px; flex-wrap: wrap; }
        .categorias button { padding: 10px 18px; border-radius: 25px; border: none; cursor: pointer; background: #222; color: #f5c400; font-weight: bold; transition: 0.3s; }
        .categorias button:hover { background: #f5c400; color: #000; }

        .btn-whatsapp-container { text-align: center; margin: 10px 0 25px; }
        .btn-whatsapp { display: inline-block; background: #25D366; color: #fff; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: bold; transition: 0.3s; box-shadow: 0 4px 15px rgba(37,211,102,0.3); }
        .btn-whatsapp:hover { transform: translateY(-3px); background: #1da851; }

        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; padding: 0 20px 40px; }
        
        .card { background: #1b1b1b; border-radius: 15px; padding: 15px; text-align: center; transition: 0.3s; border: 1px solid #333; display: flex; flex-direction: column; }
        .card:hover { transform: translateY(-5px); border-color: #f5c400; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
        
        /* CONTAINER DE IMAGEM PARA NÃO CORTAR */
        .img-box { width: 100%; height: 180px; background: #fff; border-radius: 10px; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .card img { max-width: 95%; max-height: 95%; object-fit: contain; }
        
        .card h3 { font-size: 14px; margin: 10px 0; height: 40px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; color: #ddd; }
        .card p { font-size: 18px; color: #f5c400; font-weight: bold; margin: 10px 0; }
        .card a { display: block; padding: 12px; background: #f5c400; color: #000; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: auto; }
        
        @media (max-width: 1000px) { .grid { grid-template-columns: repeat(3, 1fr); } }
        @media (max-width: 768px) { .grid { grid-template-columns: repeat(2, 1fr); } }
        @media (max-width: 480px) { .grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>

<div class="topo">
    <h1>Confira essas ofertas</h1>
    <p>*Esta página é filiada ao Mercado Livre*</p>
</div>

<div class="categorias">
    <button onclick="filtrar('todos')">Todos</button>
    <button onclick="filtrar('casa')">Casa</button>
    <button onclick="filtrar('moda')">Moda</button>
    <button onclick="filtrar('ferramentas')">Ferramentas</button>
    <button onclick="filtrar('esporte')">Esporte</button>
</div>

<div class="btn-whatsapp-container">
    <a href="https://chat.whatsapp.com/HaB12c5YvYRGljl2wJwXHI?mode=gi_t" target="_blank" class="btn-whatsapp">
        🟢 ENTRAR NO GRUPO DE OFERTAS
    </a>
</div>

<div class="grid" id="grid-produtos">
{% for p in produtos %}
    <div class="card" data-categoria="{{ p.categoria }}">
        <div class="img-box">
            <img src="{{ p.imagem }}" alt="{{ p.titulo }}">
        </div>
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.preco }}</p>    
        <a href="{{ p.link }}" target="_blank">ir ao produto</a>
    </div>
{% endfor %}
</div>

<script>
function filtrar(categoria) {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.display = (categoria === 'todos' || card.dataset.categoria === categoria) ? 'flex' : 'none';
    });
}
</script>

</body>
</html>
'''
    return render_template_string(template, produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)