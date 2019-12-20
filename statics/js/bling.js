/**
 * bling.js
 */
window.$ = document.querySelectorAll.bind(document);
window.$id = document.getElementById.bind(document);

Array.prototype.each = Array.prototype.forEach;

NodeList.prototype.__proto__ = Array.prototype;
NodeList.prototype.on = function(name, delegate, fn) {
  this.each(function(e) {
    e.on(name, delegate, fn);
  });

  return this;
};

Node.prototype.on = window.on = function(names, fn) {
  var self = this;

  names.split(' ').each(function(name) {
    self.addEventListener(name, fn);
  });

  return this;
};