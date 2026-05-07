
## Development
This project started out from a template for docker and flask site available here: https://github.com/sebinxavi/Docker-Image-Of-Simple-Python-Flask-Application. However, it's been heavily modified for the deployment to work with Github Actions and AWS Elastic Container Registry.

Requires Python 3.12

## Installation
- clone the repo
- activate the virtual environment

```source .vev/bin/activate```

- install the requirements

```pip install -r requirements```



## Testing
Before running the tests, run the application locally. The end-to-end tests will fail if the app is not running. To start the application, use:

```flask run```

After starting the server, run the tests using ```pytest```
After the tests have completed, if you run them again without restarting the server, some of the test will fail. Restart the server before testing again.



## Deployment
Deploys automatically on push to main branch.
If the deployment fails, you may need to edit the Configure AWS credentials step in .github/workflows/deploy.yaml. To get the correct "role-to-assume"
- create an IAM Role with a trusted identity type of "Web Identity", set the identity provider to token.actions.githubusercontent.com, and the github organisation to the account name of the Github repository
- copy the ARN for the role, and update the 'role-to-assume' in .github/workflows/deploy.yaml with the new ARN

You may also need to create an ECR repository to push the image to.
- create a new ECR repository in the AWS console
- copy the URI for you ECR repository
- update the final run step in .github/workflows/deploy.yaml with:
               
        docker build -t duties-app .
        docker tag duties-app:latest [your ECR-URI]
        docker push [your ECR URI] 
