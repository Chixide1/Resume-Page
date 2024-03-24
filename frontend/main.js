window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const productionApiUrl = 'https://chikfuncs.azurewebsites.net/api/counter?code=MaEUxidZ0gIzFgqGhjcrFYRiFciziNF6EqbiVTMD9BZaAzFuK24sCw==';
const localapi = "http://localhost:7071/api/counter"

const getVisitCount = () => {
    fetch(productionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count =  response;
        
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
}