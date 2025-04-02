const express = require("express");
const FunctionModel = require("../models/functionModel");

const router = express.Router();

// Create a new function
router.post("/", async (req, res) => {
  try {
    const newFunction = await FunctionModel.create(req.body);
    res.status(201).json(newFunction);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all functions
router.get("/", async (req, res) => {
  try {
    const functions = await FunctionModel.findAll();
    res.json(functions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a function by ID
router.get("/:id", async (req, res) => {
  try {
    const func = await FunctionModel.findByPk(req.params.id);
    if (!func) return res.status(404).json({ error: "Function not found" });
    res.json(func);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update function by ID
router.put("/:id", async (req, res) => {
  try {
    const updated = await FunctionModel.update(req.body, { where: { id: req.params.id } });
    if (!updated[0]) return res.status(404).json({ error: "Function not found" });
    res.json({ message: "Function updated successfully" });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Delete function by ID
router.delete("/:id", async (req, res) => {
  try {
    const deleted = await FunctionModel.destroy({ where: { id: req.params.id } });
    if (!deleted) return res.status(404).json({ error: "Function not found" });
    res.json({ message: "Function deleted successfully" });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
