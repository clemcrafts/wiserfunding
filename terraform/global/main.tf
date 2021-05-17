terraform {
  backend "s3" {
    bucket  = "terraform-state-api"
    key     = "global/terraform.tfstate"
    region  = "eu-west-1"
    encrypt = true
    profile = "SET-ME"
  }
}

provider "aws" {
  shared_credentials_file = "${var.aws_shared_credentials_file}"
  profile                 = "${var.aws_profile}"
  region                  = "${var.aws_region}"
}
