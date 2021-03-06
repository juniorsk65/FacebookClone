const express = require("express");
//mergeParams garante preservação de parametros vindo de rotas superiores
const router = express.Router({ mergeParams: true });
const dynamicSet = require("../utils/dynamicSet");
const mysql = require("mysql");
const query = require("../utils/query");
const { split } = require("../utils/slug");
const respostaGrupo = require("../routes/respostaGrupo");

//router.use()
router.use("/:idPostagem/respostas/", respostaGrupo);

//http://localhost:3000/api/grupos/{idGrupo}/postagens/
router.get("/", async function(req, res) {
    try{
        let result = await query(
            "SELECT * FROM PostagensGrupo WHERE Grupo_idGrupo=?",
            [req.params.idGrupo]
        );
        res.json(result);
    }catch(err){
        res.status(404).json({erro: err.code});
    }
});

//http://localhost:3000/api/grupos/{idGrupo}/postagens/
router.post("/", async function(req, res, next) {
    try{
        let result = await query(
            "INSERT INTO PostagensGrupo (Usuario_idUsuario, Grupo_idGrupo, conteudo) VALUES (?,?,?);",
            [
                req.body.Usuario_idUsuario,
                req.body.Grupo_idGrupo,
                req.body.conteudo
            ]
        )
        res.json(result);
    }catch(err){
        res.status(500).json({erro: err.code});
    }
});

router.delete("/:idPostagem", async function(req, res, next){
    try{
      let stringsql = mysql.format(
        "DELETE FROM PostagensGrupo WHERE Usuario_idUsuario=? AND idPostagem = ?",
        [req.params.idUsuario, req.params.idPostagem]
      );
      var result =  await query(stringsql);
      res.json({ stringsql, result});
    }catch(e){
      res.status(404).json({ erro: err.code });
    }
  });

module.exports = router;