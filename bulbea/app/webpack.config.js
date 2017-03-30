var path       = require('path');
var webpack    = require('webpack');

module.exports = {
  entry: [
    path.resolve('client/app/Client.js')
  ],
  output: {
    path: path.resolve('assets/js'),
    filename: 'bundle.min.js'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loaders: ['babel-loader']
      }
    ]
  }
};
