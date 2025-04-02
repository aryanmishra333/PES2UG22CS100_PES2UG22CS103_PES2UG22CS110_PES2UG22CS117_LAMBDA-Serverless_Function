const { DataTypes } = require("sequelize");
const { sequelize } = require("../database");

const FunctionModel = sequelize.define("Function", {
  id: {
    type: DataTypes.UUID,
    defaultValue: DataTypes.UUIDV4,
    primaryKey: true,
  },
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  route: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  language: {
    type: DataTypes.ENUM("python", "javascript"),
    allowNull: false,
  },
  timeout: {
    type: DataTypes.INTEGER,
    allowNull: false,
    defaultValue: 5000, // Default timeout 5s
  },
  code: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
});

module.exports = FunctionModel;
