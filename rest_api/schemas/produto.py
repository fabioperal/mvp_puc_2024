from pydantic import BaseModel
from typing import Optional, List
from models.produto import Produto

class ProdutoSchema(BaseModel):
    nome: str = "IPhone 11"
    descricao: Optional[str] = "Na medida certa. Amplie seus horizontes com a câmera ulta-angular. "
    marca: str = "Apple"
    categoria: str = "Telefonia"
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 3599.10

class ProdutoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"

class ProdutoBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    termo: str = "IPhone 11"

class ProdutoBuscaSchema(BaseModel):
    id: Optional[int] = 1
    nome: Optional[str] = "IPhone 11"


class ProdutoViewSchema(BaseModel):
    id: int = 1
    nome: str = "IPhone 11"
    descricao: Optional[str] = "Na medida certa. Amplie seus horizontes com a câmera ulta-angular. "
    marca: str = "Apple"
    categoria: str = "Telefonia"
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 3599.10
    total_cometarios: int = 1
    nota_media: int = 0


class ProdutoDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_produto(produto: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ListagemProdutosSchema.
    """
    result = []
    for produto in produto:
        result.append({
        "id": produto.id,
        "nome": produto.nome,
        "marca": produto.marca,
        "categoria": produto.categoria,
        "descricao": produto.descricao,
        "imagem": produto.imagem_path,
        "valor": float(produto.valor),
        "price": float(produto.valor),
          })

    return {"produto": result}

class ProdutoListaViewSchema(BaseModel):
    produtos: List[ProdutoViewSchema]

def apresenta_lista_produto(produtos):
    result = []
    for produto in produtos:
        result.append(apresenta_produto(produto))
    return {"produtos": result}

class ProdutoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"

class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoViewSchema]

class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "valor": produto.valor,
        "descricao": produto.descricao,
        "marca": produto.marca,
        "categoria": produto.categoria,
    }
