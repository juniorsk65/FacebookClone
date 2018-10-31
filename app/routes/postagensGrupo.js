const express = require("express");
//mergeParams garante preservação de parametros vindo de rotas superiores
const router = express.Router({ mergeParams: true });
const dynamicSet = require("../utils/dynamicSet");
const query = require("../utils/query");
const { split } = require("../utils/slug");

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

router.post("/:idGrupo", async function(req, res, next) {
    try{
        let result = await query(
            "INSERT INTO PostagensGrupo ("
        )
    }
})

module.exports = router;