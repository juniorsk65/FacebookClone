var express = require("express");
var router = express.Router();
var query = require("../utils/query");
var postagensGrupoRouter = require("./postagensGrupo");
var dynamicFilter = require("../utils/dynamicFilter");
var dynamicSet = require("../utils/dynamicSet");


//Sub recurso de Grupo
router.use("/:idGrupo/postagens/", postagensGrupoRouter);

//Create Group
router.post("/", async function(req, res, next){
    try{
        const result = await query(
            "INSERT INTO Grupo (nomeGrupo, descricaoGrupo, foto) VALUES(?, ?, ?); INSERT INTO Participacao (Usuario_idUsuario, Grupo_idGrupo, Administrador, Participacao) VALUES (?, LAST_INSERT_ID(), ?, ?);",
            [
                req.body.nomeGrupo,
                req.body.descricaoGrupo,
                req.body.foto,
                req.body.Usuario_idUsuario,
                req.body.Administrador,
                req.body.Participacao
            ]
        );
        res.json(result);
    }catch(err){
        res.status(500).json({erro: err.code});
    }
});


//Read all groups
router.get("/", async function(req, res, next){
    try{
        const result = await query(
            "SELECT * FROM Grupo"
        );
        res.json(result);
    } catch(err){
        res.status(404).json({ erro: err.code });
    }
});

//Get group by id
router.get("/:id", async function(req, res, next) {
    try {
      var result = await query(`SELECT * FROM Grupo WHERE idGrupo LIKE ?;`, [
        req.params.id
      ]);
      res.json(result);
    } catch (err) {
      res.status(444).json({ erro: err.code });
    }
  });

//Get all group listing by query
router.get("/", async function(req, res, next) {
    try {
      var result = await query(
        "SELECT * FROM Grupo " + dynamicFilter(req.query),
        console.log(dynamicFilter)
      );
      res.json(result);
    } catch (err) {
      res.status(404).json({ erro: err.code });
    }
  });
  
  //Update


module.exports = router;