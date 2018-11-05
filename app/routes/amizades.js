const express = require("express");
//mergeParams garante preservação de parametros vindo de rotas superiores
const router = express.Router({ mergeParams: true });
const dynamicSet = require("../utils/dynamicSet");
const query = require("../utils/query");
const { split } = require("../utils/slug");

router.get("/", async function(req, res) {
  try {
    let result = await query(
      "select  idUsuario, nomeUsuario, cidade, email from Amizade a1, Usuario u where a1.idUsuario1=? and u.idUsuario=a1.idUsuario2",
      [req.params.idUsuario]
    );
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});



router.get("/pendentes", async function(req, res, next) {
  try {
    var result = await query(
      "SELECT idUsuario, nomeUsuario, email FROM Amizade a, Usuario u WHERE idUsuario1=? AND status=0 AND u.idUsuario=a.idUsuario2",
      [req.params.idUsuario]
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

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

//Pesquisa por amizade com {idUsuario1}-{idUsuario2} para alterar
// Ja altera dos dois
router.put("/:slugAmizade", async function(req, res) {
  try {
    let ids = split(req.params.slugAmizade);
    let result = await query(
      "UPDATE Amizade SET " +
        dynamicSet(req.body) +
        " WHERE idUsuario1=? AND idUsuario2=? OR idUsuario2=? AND idUsuario1=?",
      [ids[0], ids[1], ids[0], ids[1]]
    );
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

//Mostrar amigos dos meus amigos
//localhost:3000/api/usuarios/{idUsuario1}/amizades/to/{idUsuario2}
http: router.get("/to/:amigo", async function(req, res) {
  try {
    console.log(req.params);
    const queryString =
      "SELECT u.* FROM Amizade a1, Amizade a2, Usuario u " +
      "WHERE a1.idUsuario2 = a2.idUsuario2 " +
      "AND u.idUsuario = a1.idUsuario2 " +
      "AND a1.idUSuario1 = ? " +
      "AND a2.idUsuario2 = ?";

    let result = await query(queryString, [
      req.params.idUsuario,
      req.params.amigo
    ]);

    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

module.exports = router;
