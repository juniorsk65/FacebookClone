var mysql = require("mysql");
var util = require("util");

const conn = mysql.createConnection({
  host: "localhost",
  port: "8080",
  database: "facebook",
  user: "admin",
  password: "admin"
});

const query = util.promisify(conn.query).bind(conn);
module.exports = query;
