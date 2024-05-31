const express = require('express')
const app = express()
const port = 3000;

//para não ficar voltando muito no front end
app.use("/", express.static('html'))
app.use("/css", express.static('css'))
app.use("/js",express.static('js'))
app.use("/img",express.static('img'))
app.use("/fontes",express.static('fontes'))




//para rota 404
app.use(function(req, res) {
    res.redirect("/404.html")
});

app.listen(port, () => {
    console.log(`Servidor Ouvindo a Porta ${port}`)
})