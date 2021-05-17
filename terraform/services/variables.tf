# AWS
variable "aws_region" {
  default = "eu-west-1"
}

variable "aws_profile" {
  default = "SET-ME"
}

variable "aws_shared_credentials_file" {
  default = "~/.aws/credentials"
}

variable "project_name" {
  default = "dtc-api"
}

# Route 53
variable "domain" {
  default = "SET-ME"
}

# ECS
variable "docker_image_tag" {}

variable "aws_ecs_container_port" {
  default = 8000
}

variable "ecs_task_desired_count" {
  description = "Desired number of ECS tasks to keep running"
  default     = 1
}

variable "ecs_task_max_count" {
  description = "Maximum amount of concurrent tasks running when autoscaling"
  default     = 1
}

# This version is only stepped if the message schema changes or
# when the application absolutely needs to re-process all data
variable "application_id_version" {
  default = "1"
}

# For the task sizing below,
# please refer to https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html
# for valid combinations CPU / Memory
variable "ecs_task_size_memory" {
  description = "How much memory you want to give to the task"
  default     = 512
}

variable "ecs_task_size_cpu" {
  description = "How much CPU shares"
  default     = 256
}

// @fixme: couldn't find a way to retrieve this value from data_sources at this moment.
variable "es_host" {
  description = "ES domain endpoint. No default"
}

# Redis settings
variable "redis_cluster_name" {
  description = "Cluster name without environment suffix"
  default     = "dtc"
}

variable "redis_ssl_enabled" {
  description = "Is access to Redis encrypted in transit?"
  default     = true
}
