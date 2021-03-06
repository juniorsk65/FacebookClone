const express = require("express");
const router = express.Router({ mergeParams: true });
const query = require("../utils/query");
const mysql = require("mysql");
const dynamicFilter = require("../utils/dynamicFilter");
const dynamicSet = require("../utils/dynamicSet");

router.get("/:idResposta", async function(req, res) {
  try {
    let result = await query(
      "SELECT idUsuario,conteudo FROM Resposta WHERE idPostagemUsuario=?;",
      [req.params.idResposta]
    );
    console.log(req.params.idResposta);
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

router.post("/", async function(req, res) {
  try {
    let result = await query(
      "INSERT INTO Resposta (idPostagemUsuario, idUsuario, conteudo, Reposta_idComentario) VALUES (?,?,?,?);",
      [
        req.body.idPostagem,
        req.body.idUsuario,
        req.body.conteudo,
        req.body.idResposta
      ]
    );
    res.json(result);
  } catch (err) {
    res.status(404).json({ erro: err.code });
  }
});

router.delete("/", async function(req, res){
  try{
    let stringsql = mysql.format(
      "DELETE FROM Resposta WHERE idPostagemUsuario = ? AND idUsuario =?",
    [req.params.idPostagem, req.params.idUsuario])
    
    var result = await query(stringsql);
    res.json({stringsql, result});
  }catch(e){
    res.status(404).json({erro: err.code});
  }
});

module.exports = router;
