require("dotenv").config();
const express = require("express");
const { connectDB, sequelize } = require("./database");
const functionRoutes = require("./routes/functions");

const app = express();
app.use(express.json());

// Routes
app.use("/functions", functionRoutes);

const PORT = process.env.PORT || 3000;

// Start server
const startServer = async () => {
  await connectDB();
  await sequelize.sync(); // Sync DB tables
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
};

startServer();
