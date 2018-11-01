const express = require("express");
//mergeParams garante preservação de parametros vindo de rotas superiores
const router = express.Router({ mergeParams: true });
const respostaUsuario = require("../routes/respostaUsuario");
var dynamicFilter = require("../utils/dynamicFilter");
const dynamicSet = require("../utils/dynamicSet");
const query = require("../utils/query");
const { split } = require("../utils/slug");

//Sub recurso de Grupo
router.use("/:idPostagem/respostas/", respostaUsuario);

//Get all posts from userX, where owner=X and id=X
//http://localhost:3000/api/usuarios/{idUsuario}/postagens/
router.get("/", async function(req, res) {
  try {
    let result = await query(
      "SELECT * FROM PostagensUsuario WHERE usuarioProprietario=? AND idUsuario2=?",
      [req.params.idUsuario, req.params.idUsuario]
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

//http://localhost:3000/api/usuarios/{idUsuario}/postagens/{idDestino}
router.get("/:amigo", async function(req, res) {
  try {
    let result = await query(
      "SELECT * FROM PostagensUsuario WHERE 0 = (SELECT bloqueio FROM Amizade WHERE idUsuario1=? AND idUsuario2=?) AND usuarioProprietario=?",
      [req.params.idUsuario, req.params.amigo, req.params.amigo]
    );
    res.json(result);
  } catch (err) {
    res.status(303).json({ erro: err.code });
  }
});

//Post in PostagensUsuario
//http://localhost:3000/api/usuarios/{usuarioProprietario}/postagens/{idUsuarioDestino}
router.post("/:idUsuario", async function(req, res, next) {
  try {
    let result = await query(
      "INSERT INTO PostagensUsuario (usuarioProprietario, idUsuario2, conteudo) VALUES (?,?,?)",
      [req.body.usuarioProprietario, req.body.idUsuario2, req.body.conteudo]
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

module.exports = router;
