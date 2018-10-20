var mysql = require('mysql');
var util = require('util');

const conn = mysql.createConnection({
    host: 'localhost',
    port: '3306',
    database: 'facebook',
    user: 'luciano',
    password: '1234'
});

const query = util.promisify(conn.query).bind(conn);
module.exports = query;