# Ansible Playbook to Deploy Lambda Functions

An Ansible Playbook to package the pip dependencies and deploy it to AWS Amazon Lambda function.

The example shows direct deploy to Lambda and Referenced deployment using S3. Also, the 2 virtual environments `venv` and `deployvenv` are used for working virtual environment and deployment environment respectively.

Of course, there are better approaches involving pipenv and other newer techniques. I find this approach easier to manage.

