var express = require("express");
var router = express.Router();
var query = require("../utils/query");
var amizadesRouter = require("./amizades");
var postagensRouter = require("./postagensUsuario");
var dynamicFilter = require("../utils/dynamicFilter");
var dynamicSet = require("../utils/dynamicSet");

//Sub-recurso amizades
router.use("/:idUsuario/amizades", amizadesRouter);
//Sub-recurso postagensUsuario
//router.use("/:idUsuario/postagem", postagensRouter);

//Create
router.post("/", async function(req, res, next) {
  try {
    const result = await query(
      "INSERT INTO Usuario (nomeUsuario, cidade, privacidade, email) VALUES (?, ?, ?, ?);",
      [
        req.body.nomeUsuario,
        req.body.cidade,
        req.body.privacidade,
        req.body.email
      ]
    );
    res.json(result);
  } catch (err) {
    res.status(500).json({ erro: err.code });
  }
});

//READ
//Get all users listing
router.get("/", async function(req, res, next) {
  try {
    var result = await query(
      "SELECT * FROM Usuario" + dynamicFilter(req.query),
      console.log(dynamicFilter)
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

//Get user by id
router.get("/:id", async function(req, res, next) {
  try {
    var result = await query(`SELECT * FROM Usuario WHERE idUsuario LIKE ?;`, [
      req.params.id
    ]);
    res.json(result);
  } catch (err) {
    res.status(444).json({ erro: err.code });
  }
});

//Update

//Update privacidade
router.put("/:idUsuario", async function(req, res, next) {
  try {
    //Se nenhum corpo for passado como argumento
    if (Object.keys(req.body).length == 0) res.status(200).end();

    var result = await query(
      "UPDATE Usuario SET " + dynamicSet(req.body) + " WHERE idUsuario=?",
      [req.params.idUsuario]
    );
    res.json(result);
  } catch (e) {
    res.status(444).json({ erro: err.code });
  }
});

//Delete

module.exports = router;
