# Azure-Resume

This is my cloud resume built using Azure with the [ACG Project Video](https://www.youtube.com/watch?v=ieYrBWmkfno&t=635s) as a reference.

The below diagram details the specific offerings we leveraged and their functionalities within the project's architecture.
![Alt text](Other/image.png)

## Frontend

- The front-end is a static website coded in HTML, CSS & Javascript. I used a template provided by [Ceevee](https://www.styleshout.com/free-templates/ceevee/) and amended it to showcase my personal profile & relevant details.

- In addition, there is also a visitor counter element that shows how many times the webpage has been accessed which is updated via a Javascript API call to Azure Functions. This gets activated everytime the webpage is fully rendered.

- The code is hosted within an Azure Storage account blob using the **Static Website** capability that can be enabled and allows static content to be served from an endpoint.

- In order to deliver the static content from my own custom domain I had to implement Azure CDN. The **Custom Domain HTTPS** feature was then enabled which allows content to be delivered securely from the CDN to the User's Client.

## Backend

- Cosmos DB is used to store the visitor count within a container named counter which can be retrieved through the NoSQL API.

- Azure Functions was used to create an event-driven trigger that whenever called through a specific URL, would increment the visitor count and return the value in JSON Format.

## CI/CD