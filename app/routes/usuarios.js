var express = require("express");
var router = express.Router();
var query = require("../utils/query");
var dynamicFilter = require("../utils/dynamicFilter");
var dynamicSet = require("../utils/dynamicSet");
//SubRecursos
var amizadesRouter = require("./amizades");
var postagensUsuarioRouter = require("./postagensUsuario");


//Sub-recurso amizades
router.use("/:idUsuario/amizades/", amizadesRouter);
//Sub-recurso postagensUsuario
router.use("/:idUsuario/postagens/", postagensUsuarioRouter);

//Create
//POST, receive body with JSON of user
//http://localhost:3000/api/usuarios/
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
//http://localhost:3000/api/usuarios/?{parametro}={busca}
router.get("/", async function(req, res, next) {
  try {
    var result = await query(
      "SELECT * FROM Usuario" + dynamicFilter(req.query),
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

//Get user by id
//http://localhost:3000/api/usuarios/{idUsuario}
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
//http://localhost:3000/api/usuarios/{idUsuario}
//Dentro do body colocar os campos que deseja alterar
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
//http://localhost:3000/api/usuarios/{idUsuario}
router.delete("/:idUsuario", async function(req, res, next){
  try {
    var result = await query(
      "DELETE FROM Usuario WHERE idUsuario = ?",
      [req.params.idUsuario]
    );
    res.json(result);
  } catch (e) {
    res.status(666).json({ erro: err.code });
  }
});
module.exports = router;
