const express = require('express');

const app = express();

app.get('/', (req, res) => { return res.send('Rota principal'); });

app.listen(3000, () => console.log('Servidor rodando'));