window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const productionApiUrl = 'https://chikfuncs.azurewebsites.net/api/counter';
const localapi = "http://localhost:7071/api/counter"

async function getVisitCount() {

  try {

    const response = await fetch(productionApiUrl);

    if (!response.ok) {
      console.error("API request failed:", response.status + " - " + response.statusText);
      throw "API request error";
    }

    const data = await response.json();

    console.log("Website called function API.");

    const count = data;

    document.getElementById("counter").innerText = count;

  

    return count; // Return the count after receiving the response

  } catch (error) {

    console.error("Error fetching API response:", error);

    throw error; // Re-throw the error for further handling if needed

  }

}