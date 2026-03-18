import express from "express";

const app = express();
const port = 5000;

app.use(express.json());
// CRUD

// Create
// Read
// Update
// Delete

// GET
app.get("/", (request, response) => {
  response.json({ name: "davit", age: 21 });
});

// POST
app.post("/", (request, response) => {
  console.log(request.body);
  response.json(request.body);
});

// PUT / UPDATE
app.put("/", (request, response) => {
  console.log(request.body);
  response.json({ name: "davit", age: 21 });
});

// DELETE
app.delete("/", (request, response) => {
  response.json({ name: "davit", age: 21 });
});

app.listen(port, () => {
  console.log("server is started at port:", port);
});