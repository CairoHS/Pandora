const express = require('express')
const app = express()
const port = 3000;

const path = require('path')

//app.use((req,res,next) => {
//    res.setHeader( 'Cache-control',' no-store, no-cache, must-validate, private' )
//})
//para não ficar voltando muito no front end

//remove o html do final


//app.use((req, res, next) => {
//    if (req.path.endsWith('.html')) {
//        const newPath = req.path.slice(0, -5); // Remove .html
//        return res.redirect(301, newPath);
//    }
//    next();
//});

app.use("/", express.static('html',{extensions:['html']}))
app.use(express.static('public'))



//para rota 404
app.use(function(req, res) {
    res.redirect("/404")
});

app.listen(port, () => {
    console.log(`Servidor Ouvindo a Porta ${port}`)
})