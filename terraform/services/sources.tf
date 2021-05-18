data "aws_vpc" "default" {
  filter {
    name   = "tag:Name"
    values = ["Default VPC"]
  }
}

data "aws_instances" "kafka_brokers" {
  instance_tags {
    cluster     = "kafka_${terraform.workspace}"
    Environment = "${terraform.workspace}"
    Terraform   = true
  }

  instance_state_names = ["running"]
}

data "aws_vpc" "main" {
  filter {
    name   = "tag:Name"
    values = ["${terraform.workspace}-vpc"]
  }
}

data "aws_subnet_ids" "private" {
  vpc_id = "${data.aws_vpc.main.id}"

  tags {
    Tier = "Private"
  }
}
