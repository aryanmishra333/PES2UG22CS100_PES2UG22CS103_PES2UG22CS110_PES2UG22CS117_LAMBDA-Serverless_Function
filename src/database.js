const { Sequelize } = require("sequelize");

const sequelize = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
  host: process.env.DB_HOST,
  dialect: "postgres",
  logging: false, // Disable logging for cleaner output
});

const connectDB = async () => {
  try {
    await sequelize.authenticate();
    console.log("Connected to PostgreSQL");
  } catch (error) {
    console.error("Unable to connect:", error);
  }
};

module.exports = { sequelize, connectDB };
