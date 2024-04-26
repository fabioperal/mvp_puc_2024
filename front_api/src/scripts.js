/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/

const getList = async () => {
  let url = 'https://fakestoreapi.com/products';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      // console.log(data);
      data.forEach(item => insertCard(item))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/

const getListLocal = async () => {
  let url = 'http://localhost:5000/produtos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // data.forEach(item => insertCard(item))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getListLocal()

getList()

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertCard = (product) => {
  var section = document.getElementById('products-list');
  let article = document.createElement('article');
  article.setAttribute('class','product');
  article.setAttribute('id', product.id);

  let img = document.createElement('img');
  img.setAttribute('src', product.image);
  img.setAttribute('alt', 'Não foi possível carregar a imagem do produto');
  
  let h3 = document.createElement('h3');
  h3.setAttribute('class', 'price-product');
  let span = document.createElement('span');
  span.innerHTML = 'R$ ' + product.price;
  h3.appendChild(span);

  let p = document.createElement('p');
  p.setAttribute('class', 'name-product');
  p.innerHTML = product.title;

  let button = document.createElement('button');
  button.setAttribute('class', 'buy-product');
  button.setAttribute('type', 'button');
  button.setAttribute('id', product.id);
  button.innerHTML = 'Comprar';

  article.appendChild(img);
  article.appendChild(h3);
  article.appendChild(p);
  article.appendChild(button);
  section.appendChild(article);
}