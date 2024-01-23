# Azure-Resume

This is my cloud resume built using Azure with the [ACG Project Video](https://www.youtube.com/watch?v=ieYrBWmkfno&t=635s) as a reference.

The below diagram details the specific offerings we leveraged and their functionalities within the project's architecture.
![Alt text](Other/image.png)

## Frontend

- The front-end is a static website coded in HTML, CSS & javascript. I used a template provided by [Ceevee](https://www.styleshout.com/free-templates/ceevee/) and amended it to showcase my personal profile & relevant details.

- In addition, there is also a visitor counter that shows how many times the webpage has been accessed via a javascript API call to Azure Functions.

- The code is hosted within an Azure Storage account blob using the **Static Website** capability that can be enabled and allows static content to be served from an endpoint.

- In order to deliver the static content from my own custom domain I had to implement Azure CDN. The **Custom Domain HTTPS** feature was then enabled which allows content to be delivered securely from the CDN to the User's Client.

## Backend


## CI/CD