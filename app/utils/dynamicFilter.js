const { escape, escapeId } = require("mysql");

const dynamicFilter = obj => {
  keys = Object.keys(obj);
  return keys.length > 0
    ? "WHERE " +
        keys.map(key => `${escapeId(key)}=${escape(obj[key])}`).join(" AND ")
    : "";
};

module.exports = dynamicFilter;
