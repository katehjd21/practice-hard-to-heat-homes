
terraform {
  backend "s3" {
    bucket         = "kd-test-terraform-bucket"
    key            = "practice_hard_to_heat_homes/terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}