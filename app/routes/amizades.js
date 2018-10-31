const express = require("express");
//mergeParams garante preservação de parametros vindo de rotas superiores
const router = express.Router({ mergeParams: true });
const dynamicSet = require("../utils/dynamicSet");
const query = require("../utils/query");
const { split } = require("../utils/slug");

router.get("/", async function(req, res) {
  try {
    let result = await query(
      "SELECT * FROM Amizade WHERE idUsuario1=? OR idUsuario2=?",
      [req.params.idUsuario, req.params.idUsuario]
    );
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

//("SELECT * FROM Amizade");

router.post("/", async function(req, res) {
  try {
    let result = await query(
      "INSERT INTO Amizade (idUsuario1, idUsuario2, bloqueio, status) VALUES (?,?,?,?), (?,?,?,?)",
      [
        req.body.idUsuario1,
        req.body.idUsuario2,
        req.body.bloqueio,
        req.body.status,
        req.body.idUsuario2,
        req.body.idUsuario1,
        req.body.bloqueio,
        req.body.status
      ]
    );
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

router.put("/:slugAmizade", async function(req, res) {
  try {
    let ids = split(req.params.slugAmizade);
    let result = await query(
      "UPDATE Amizade SET " +
        dynamicSet(req.body) +
        " WHERE idUsuario1=? AND idUsuario2=?",
      [ids[0], ids[1]]
    );
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

module.exports = router;
