const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const extractCSS = new ExtractTextPlugin({ filename: 'css.bundle.css' })

module.exports = {
    entry: './src/app.js',
    output: {
        filename: 'index.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude:/(node_modules|bower_components)/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015']
                }
            },
            {
                test: /\.css$/,
                use: extractCSS.extract({ // Instance 1
                  fallback: 'style-loader',
                  use: [ 'css-loader' ]
                })
            },
            
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.template.html'
        }),
        extractCSS
    ]
};