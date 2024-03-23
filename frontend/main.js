window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const productionApiUrl = 'https://chikfuncs.azurewebsites.net/api/azureResumeCounter?code=lQxSzOthjy7qLL_lJ7kwbBXnLGgQcqkTJB4FQVVsx-UJAzFu2neVbQ==';
const localapi = "http://localhost:7071/api/azureResumeCounter"

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
    return count;
}