const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const path = require('path');
const functionRoutes = require('./routes/functions'); // your function routes

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Add a route for the root URL
app.get('/', (req, res) => {
  res.send('Welcome to Lambda Serverless Function Platform!');
});

// API routes for functions
app.use('/api', functionRoutes);

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
