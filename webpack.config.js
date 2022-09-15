const path = require('path')
const HtmlWebpack = require('html-webpack-plugin')
const MinCssExtract = require('mini-css-extract-plugin')

module.exports = {

    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /\.(sa|c|sc)ss$/, //Expressão regular - regex
                use: [
                    MinCssExtract.loader,
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.css$/i,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.js$/i,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.(jpeg|jpg|png|svg|gif)$/i,
                use: {
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]'
                    }
                }
            }
        ]
    },

    plugins: [
        new HtmlWebpack({
            filename: 'index.html',
            template: './src/index.html'
        }),
        new MinCssExtract({
            filename: 'style.css'
        })
    ]
}