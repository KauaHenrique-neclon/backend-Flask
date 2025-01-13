var content = document.getElementById("content")
var button_content = document.getElementById("buttonContent")

button_content.addEventListener("click", function (){
    
    var content = document.getElementById("content")
    if(content.style.display === "block"){
        content.style.display = "block"
    }else{
        content.style.display = "block"
        listaUsuario.style.display = "none"
        relatorioResumo.style.display = "none"
    }
});

var listaUsuario = document.getElementById("lista-usuario")
var buttonListaUsuario = document.getElementById("buttonUsuario")

buttonListaUsuario.addEventListener("click", function(){
     
    var listaUsuario = document.getElementById("lista-usuario")
    if(listaUsuario.style.display === "block"){
        listaUsuario.style.display = "block"
    }else{
        listaUsuario.style.display = "block"
        content.style.display = "none"
        relatorioResumo.style.display = "none"
    }
});

var relatorioResumo = document.getElementById("resumoRelatorio")
var buttonRelatorio = document.getElementById("relatorio")

buttonRelatorio.addEventListener("click", function(){

    var relatorioResumo = document.getElementById("resumoRelatorio")
    if(relatorioResumo.style.display === "block"){
        relatorioResumo.style.display = "block"
    }else{
        relatorioResumo.style.display = "block"
        content.style.display = "none"
        listaUsuario.style.display = "none"
    }
})