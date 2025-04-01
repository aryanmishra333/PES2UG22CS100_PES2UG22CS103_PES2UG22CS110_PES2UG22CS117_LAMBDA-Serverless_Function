const pool = require('../database');

const createTableQuery = `
  CREATE TABLE IF NOT EXISTS functions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    route VARCHAR(255) NOT NULL UNIQUE,
    language VARCHAR(50) CHECK (language IN ('python', 'javascript')),
    timeout INTEGER DEFAULT 5000
  );
`;

pool.query(createTableQuery)
  .then(() => console.log('Table created'))
  .catch(err => console.error('Error creating table', err));
