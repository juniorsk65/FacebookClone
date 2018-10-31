var express = require('express');
var router = express.Router();
var query = require('../utils/query');
var usuarios = require('./usuarios');
var grupos = require('./grupos');

//Use usuarios router
router.use('/usuarios', usuarios)
router.use('/grupos', grupos)

//Use grupos router

module.exports = router;
