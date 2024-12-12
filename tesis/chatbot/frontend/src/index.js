const express = require("express");
const cors = require("cors");
const authRoutes = require("./routes/auth");
const tareasRoutes = require("./routes/tareas");
const chatbotRoutes = require("./routes/chatbot");
const notasRoutes = require("./routes/notas");

require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

app.use("/api/auth", authRoutes);
app.use("/api/tareas", tareasRoutes);
app.use("/api/chatbot", chatbotRoutes);
app.use("/api/notas", notasRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor corriendo en el puerto ${PORT}`));
