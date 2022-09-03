# eks

This repos contains code for deploying a kubernetes cluster on AWS EKS using pulumi and gitlab.

## Documentation

- [Pulumi EKS](https://www.pulumi.com/docs/guides/crosswalk/aws/eks/)
- [Deplot to AWS from GitLab CI/CD](https://docs.gitlab.com/ee/ci/cloud_deployment/)
- [Pulumi Python](https://www.pulumi.com/docs/intro/languages/python/)
- [Pulumi GitLab CI](https://www.pulumi.com/docs/guides/continuous-delivery/gitlab-ci/)

## How the code in this repos was made

- Create a folder pulumi
- cd into the pulumi folder
- Run ```pulumi new```
- gitlab-ci.yml was edited folloing the instruction of this page [Pulumi GitLab CI](https://www.pulumi.com/docs/guides/continuous-delivery/gitlab-ci/)