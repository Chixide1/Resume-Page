window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const productionApiUrl = 'https://chikfuncs.azurewebsites.net/api/counter?code=MaEUxidZ0gIzFgqGhjcrFYRiFciziNF6EqbiVTMD9BZaAzFuK24sCw==';
const localapi = "http://localhost:7071/api/counter"

async function getVisitCount() {

  try {

    const response = await fetch(productionApiUrl);

    const data = await response.json();

  

    console.log("Website called function API.");

    count = data;

    document.getElementById("counter").innerText = count;

  

    return count; // Return the count after receiving the response

  } catch (error) {

    console.error("Error fetching API response:", error);

    throw error; // Re-throw the error for further handling if needed

  }

}