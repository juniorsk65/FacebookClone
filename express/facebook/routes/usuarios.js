var express = require('express');
var router = express.Router();
var query = require('../utils/query');


//Create
router.post('/', async function(req, res, next) {
  try{
    const result = await query('INSERT INTO Usuario (nomeUsuario, cidade, privacidade, email) VALUES (?, ?, ?, ?);', [req.body.nomeUsuario,req.body.cidade, req.body.privacidade, req.body.email])
    res.json(result)
  }catch(err){
    res.status(500).json({erro: err.code})
  }
});

//READ
//Get all users listing
router.get('/', async function(req, res, next) {
  try{
    var result = await query('SELECT * FROM Usuario;')
    res.json(result)
  }catch(err)
  {
    res.status(404).json({erro: err.code});
  }
});

//Get user by id
router.get('/:id' , async function(req, res, next){
  try{
    var result = await query('SELECT * FROM Usuario WHERE idUsuario LIKE ?;',[req.params.id])
    res.json(result)
  }catch(err)
  {
    res.status(444).json({erro: err.code});
  }
})

//Get users by city
router.get('/:cidade', async function(req, res, next){
  try{
    var result = await query('SELECT * FROM Usuario WHERE ')
  }catch(err){
    
  }
})

//Update



//Delete


module.exports = router;
