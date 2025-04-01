const express = require('express');
const router = express.Router();
const pool = require('../database');

// Create function
router.post('/functions', async (req, res) => {
  const { name, route, language, timeout } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO functions (name, route, language, timeout) VALUES ($1, $2, $3, $4) RETURNING *',
      [name, route, language, timeout]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get all functions
router.get('/functions', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM functions');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
