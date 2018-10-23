const { escape, escapeId } = require("mysql");

const dynamicSet = obj => {
  keys = Object.keys(obj);
  return keys.length > 0
    ? keys.map(key => `${escapeId(key)}=${escape(obj[key])}`).join(" , ")
    : "";
};

module.exports = dynamicSet;
