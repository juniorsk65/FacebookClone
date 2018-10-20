var express = require('express');
var router = express.Router();
var query = require('../utils/query');
var usuarios = require('./usuarios');

//Use usuarios router
router.use('/usuarios', usuarios)

//Use grupos router

module.exports = router;
