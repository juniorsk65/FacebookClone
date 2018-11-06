var express = require("express");
var router = express.Router({ mergeParams: true });
var query = require("../utils/query");
var postagensGrupoRouter = require("./postagensGrupo");
var dynamicFilter = require("../utils/dynamicFilter");
var dynamicSet = require("../utils/dynamicSet");


//Sub recurso de Grupo
router.use("/:idGrupo/postagens/", postagensGrupoRouter);

//Create Group POST
//http://localhost:3000/api/grupos/
router.post("/", async function(req, res, next){
    try{
      const sql = mysql.format(
       "INSERT INTO Grupo (nomeGrupo, descricaoGrupo, foto) VALUES(?, ?, ?);\
        INSERT INTO Participacao (Usuario_idUsuario, Grupo_idGrupo, Administrador, Participacao) VALUES (?, LAST_INSERT_ID(), ?, ?);",
       [
           req.body.nomeGrupo,
           req.body.descricaoGrupo,
           req.body.foto,
           req.body.Usuario_idUsuario,
           req.body.Administrador,
           req.body.Participacao
       ]
      );
      var result =  await query(sql);
      res.json({
        sql,
        result,
      });
    }catch(err){
        res.status(500).json({erro: err.code});
    }
});


//Read all groups
//http://localhost:3000/api/grupos/
router.get("/", async function(req, res, next){
    try{
      const sql = mysql.format(
        "SELECT * FROM Grupo"
       );
       var result =  await query(sql);
       res.json({
         sql,
         result,
       });
    } catch(err){
        res.status(404).json({ erro: err.code });
    }
});

//Get group by id
//http://localhost:3000/api/grupos/{idGrupo}
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
//http://localhost:3000/api/grupos/
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
//http://localhost:3000/api/grupos/{idGrupo}
//Dentro do body colocar os campos que deseja alterar
router.put("/:idGrupo", async function(req, res, next) {
    try {
      //Se nenhum corpo for passado como argumento
      if (Object.keys(req.body).length == 0) res.status(200).end();
      console.log( "UPDATE Grupo SET " + dynamicSet(req.body) + " WHERE idGrupo=?")
      
      var result = await query(
        "UPDATE Grupo SET " + dynamicSet(req.body) + " WHERE idGrupo=?",
        [req.params.idGrupo]
      );
      console.log(result);
      res.json(result);

    } catch (err) {
      res.status(444).json({ erro: err.code });
    }
  });


//Delete
//http://localhost:3000/api/grupos/{idGrupo}
router.delete("/:idGrupo", async function(req, res, next){
  try {
    var result = await query(
      "DELETE FROM Grupo WHERE idGrupo = ?",
      [req.params.idGrupo]
    );
    res.json(result);
  } catch (e) {
    res.status(666).json({ erro: err.code });
  }
});

module.exports = router;