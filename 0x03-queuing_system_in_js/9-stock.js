import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const getItemById = (id) => listProducts.find((item) => item.id === id);

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
};

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.id);
  return res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.id);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.id });
  }
  reserveStockById(item.id, currentQuantity - 1);
  return res.json({ status: 'Reservation confirmed', itemId: item.id });
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});
