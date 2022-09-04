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
- Then through this [merge request](https://gitlab.com/eks-explorer/eks/-/merge_requests/1) every error was fixed

## Permission of the AWS user

The AWS user needs to have the following permissions:
- AmazonEC2FullAccess
- AmazonEKSClusterPolicy
- AmazonEKSWorkerNodePolicy
- AmazonEKSServicePolicy
- AmazonEKS_CNI_Policy
- AmazonEKSFargatePodExecutionRolePolicy
- AmazonEKSLocalOutpostClusterPolicy
- AmazonEKSVPCResourceController