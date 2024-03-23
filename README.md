# Azure-Resume

This is my cloud resume built using Azure with the [ACG Project Video](https://www.youtube.com/watch?v=ieYrBWmkfno&t=635s) as a reference.I used VS Code as my IDE of choice.

The below diagram details the specific offerings we leveraged and their functionalities within the project's architecture.
![Alt text](frontend/images/project-structure.png)

## Frontend

- **Programming Languages**: The frontend is a static website coded in HTML, CSS & Javascript. I used a template provided by [Ceevee](https://www.styleshout.com/free-templates/ceevee/) and amended it to showcase my personal profile & relevant details.

- **Visitor Counter**: In addition, there is also a counter element that shows how many times the webpage has been accessed which is updated via a Javascript API call to Azure Functions. This gets triggered everytime the webpage is fully rendered.

- **Azure Blob Storage**: The code is hosted within a container named *$web* using the *Static Website* capability that can be enabled and allows static content to be served from an endpoint.

- **Azure CDN**: In order to deliver the static content from my own custom domain I had to implement Azure CDN. The *Custom Domain HTTPS* feature was then enabled which allows content to be delivered securely from the CDN to the User's Client.

## Backend

- **Azure Cosmos DB**: Cosmos DB is used to store the visitor count within a container named counter which can be retrieved through the NoSQL API.

- **Azure Function Apps**: This was used to create a Python-Based event-driven trigger that whenever called through a specific URL, would increment the visitor count and return the value in JSON Format. I had to add my Custom Domain to the allowed origins section in CORS to allow the frontend to call the api.

## CI/CD

- **Platform**: Github actions was used to create my Continuous Integration & Continuous Delivery pipeline through workflow scripts written in YAML.

- **Frontend**: Whenever changes are pushed to the frontend folder, they are also uploaded to the blob storage container used to serve the website. Afterwards, the CDN endpoint is purged to refresh the content and display the newly uploaded content.

- **Backend**: Whenever changes are pushed to the backend folder, a unit test is executed to see if the function works as expected.Once passed, the function app gets redoployed into Azure with the new changes.