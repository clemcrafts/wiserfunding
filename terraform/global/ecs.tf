resource "aws_ecs_cluster" "main" {
  name = "${var.project_name}"
}

resource "aws_ecr_repository" "ecr" {
  name = "${var.project_name}"
}
