var express = require("express");
var router = express.Router();
var query = require("../utils/query");
var dynamicFilter = require("../utils/dynamicFilter");
var dynamicSet = require("../utils/dynamicSet");

router.get("/:idResposta", async function(req, res) {
    try{
        let result = await query(
            "SELECT * FROM RespostaPostagemUsuario WHERE idPostagemUsuario=?;",
            [req.params.idResposta]
            );
        console.log(req.params.idResposta);
        res.json(result);
    }catch(err){
        res.status(404).json({erro: err.code});
    }
});

router.post("/", async function(req, res){
    try{
        let result = await query(
            "INSERT INTO RespostaPostagemUsuario (idPostagemUsuario, idUsuario, conteudo, Reposta_idComentario) VALUES (?,?,?,?);",
            [
                req.body.idPostagem,
                req.body.idUsuario,
                req.body.conteudo,
                req.body.idResposta
            ]
        );
        res.json(result);
    }catch(err){
        res.status(404).json({erro: err.code});
    }
});

module.exports = router;