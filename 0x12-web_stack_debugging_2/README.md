# 0x12. Web stack debugging #2

## Overview
This project involves debugging tasks related to web stack configurations, focusing on user permissions and Nginx setup. It requires addressing issues, such as running software as another user and configuring Nginx to run securely.

- **Project Start:** December 18, 2023,
- **Project End:** December 20, 2023,

## Concepts
This project is centered around the concept of **Web stack debugging**.

## Requirements
### General
- All files are interpreted on Ubuntu 20.04 LTS.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Bash script files must be executable.
- Bash scripts must pass Shellcheck without any error.
- Bash scripts must run without error.
- The first line of Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of Bash scripts should be a comment explaining the script's purpose.

## Tasks
### Task 0: Run software as another user (0-iamsomeoneelse)
This task involves creating a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument.

### Task 1: Run Nginx as Nginx (1-run_nginx_as_nginx)
The goal is to ensure that Nginx is running as the `nginx` user, listening on all active IPs on port 8080. This task involves configuring the container to fulfill these requirements without using `apt-get remove`.

## Repository Details
- **GitHub Repository:** alx-system_engineering-devops
- **Directory:** 0x12-web_stack_debugging_2
