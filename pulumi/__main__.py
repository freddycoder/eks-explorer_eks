# https://www.pulumi.com/docs/guides/crosswalk/aws/eks/
import pulumi
import pulumi_eks as eks

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster')

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
