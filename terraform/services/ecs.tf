module "ecs" {
  source                      = "SET-ME"
  project_name                = "${var.project_name}"
  aws_ecs_task_definition_arn = "${aws_ecs_task_definition.main.arn}"
  aws_ecs_container_port      = "${var.aws_ecs_container_port}"
  container_health_path       = "/status/${var.project_name}"
  ecs_task_desired_count      = "${var.ecs_task_desired_count}"
  ecs_task_max_count          = "${var.ecs_task_max_count}"
}

resource "aws_ecs_task_definition" "main" {
  family       = "${var.project_name}-${terraform.workspace}"
  network_mode = "awsvpc"

  requires_compatibilities = [
    "FARGATE",
  ]

  cpu    = "${var.ecs_task_size_cpu}"
  memory = "${var.ecs_task_size_memory}"

  task_role_arn      = "${module.ecs.aws_iam_role_ecs_service_role_arn}"
  execution_role_arn = "${module.ecs.aws_iam_role_ecs_service_role_arn}"

  container_definitions = <<DEFINITION
[
  {
    "name": "${var.project_name}-${terraform.workspace}",
    "image": "${module.ecs.aws_ecr_repository_repository_url}:${var.docker_image_tag}",
    "networkMode": "awsvpc",
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/${var.project_name}-${terraform.workspace}",
        "awslogs-region": "${var.aws_region}",
        "awslogs-stream-prefix": "ecs"
      }
    },
    "portMappings": [
      {
        "containerPort": ${var.aws_ecs_container_port},
        "hostPort": ${var.aws_ecs_container_port},
        "protocol": "tcp"
      }
    ],
    "environment": [
      {
        "name": "LOG_LEVEL",
        "value": "${terraform.workspace == "dev" ? "DEBUG" : "INFO"}"
      },
      {
        "name": "KAFKA_BROKERS",
        "value": "${join(",", formatlist("%s:9092", data.aws_instances.kafka_brokers.private_ips))}"
      },
      {
        "name": "KAFKA_GROUP_ID",
        "value": "${var.project_name}-${var.application_id_version}"
      },
      {
        "name": "ES_HOST",
        "value": "${var.es_host}"
      },
      {
        "name": "ES_PORT",
        "value": "443"
      },
      {
        "name": "ES_USE_SSL",
        "value": "1"
      },
      {
        "name": "APP_ENVIRONMENT",
        "value": "${terraform.workspace}"
      },
      {
        "name": "APP_VERSION",
        "value": "${var.docker_image_tag}"
      },
      {
        "name": "REDIS_HOST",
        "value": "${data.aws_elasticache_replication_group.main.primary_endpoint_address}"
      },
      {
        "name": "REDIS_PORT",
        "value": "${data.aws_elasticache_replication_group.main.port}"
      },
      {
        "name": "REDIS_SSL_ENABLED",
        "value": "${var.redis_ssl_enabled}"
      }
    ]
  }
]
DEFINITION
}

resource "aws_iam_policy" "es_service_role_policy" {
  name = "${var.project_name}-${terraform.workspace}-es-container-service-role"

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "es:*"
      ],
      "Resource": "arn:aws:es:${var.aws_region}:${data.aws_caller_identity.current.account_id}:domain/dtc-${terraform.workspace}/*"
    },
    {
        "Effect": "Allow",
        "Action": [
          "s3:ListBucket"
        ],
        "Resource": [
          "${data.aws_s3_bucket.translations.arn}"
        ]
    },
    {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject"
        ],
        "Resource": [
          "${data.aws_s3_bucket.translations.arn}/*"
        ]
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "ecs_es_service_role" {
  role       = "${module.ecs.aws_iam_role_ecs_service_role_name}"
  policy_arn = "${aws_iam_policy.es_service_role_policy.arn}"
}
