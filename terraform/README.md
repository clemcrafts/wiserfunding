# AWS Terraform

We assume all the commands are run from within this directory.

## AWS

The terraform state is stored in AWS, so you'd need to supply your credentials for it.

> See [main.tf](main.tf) to check how to connect to AWS and [config.tf](config.tf) for terraform's backend config.

## Variables and environments

### Globally Shared Resources
A separate terraform file/dir structure exists under ./global. This is the home of any resources shared across environments (e.g. IAM's, S3 buckets, etc). This should be a limited set of resources and the bulk of the infrastructure defined under environment workspaces as described below.

Note this global dir is quite separate to the workspaces and has it's own state file, etc. This is intentional and ensure you can work in any env workspace without concern about clobbering shared resources.

### Getting Started / Boostrapping the Project

First you need to ensure the state bucket is present.

1. Create the state S3 bucket
$ cd terraform/global
$ terraform init
$ terraform apply

That's the dependencies setup, you're ready to proceed with setting up your workspaces (environments) and deploying infrastructure as described below.

### Workspaces

[Workspaces](https://www.terraform.io/docs/state/workspaces.html) are a new and interesting way to keep things with slights differences separated.

The main workspaces and resources are defined in /terraform dir

**Workspaces isolate states**.

There is only one workspace for this project:

```console
$ terraform workspace list  
* default
```

### Variables

Variables are stored in different files as follow:

* `terraform.tfvars`: ignored by version control, keep your secrets in there.
* `variables.tf`: vars valid across all environments
* `dev.tfvars`: vars valid just for `dev` env
* `uat.tfvars`: vars valid just for `uat` env
* `prod.tfvars`: vars valid just for `prod` env

## Working on the project

```console
$ terraform apply -var-file="`terraform workspace show`.tfvars"
```
