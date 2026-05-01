originally based on: https://github.com/sebinxavi/Docker-Image-Of-Simple-Python-Flask-Application
based on the docker image: sebinxavi/python-web-app:1

add to ``DB_MODE=mock`` .env file to use mock data

## Deployment Notes
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
