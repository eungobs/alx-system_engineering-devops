# 0x0E. Web stack debugging #1

## Description

This project is part of the DevOps, SysAdmin, Scripting, and Debugging fields and aims to fix an issue with the Nginx installation in an Ubuntu container that prevents it from listening on port 80.

## Concepts

The project expects you to look at the following concepts:
- Network basics
- Web stack debugging

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- Mandatory README.md file at the root of the project folder
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does
- Usage of `wget` is not allowed

### Tasks
- **0. Nginx likes port 80**
  - Find and fix the issue preventing the Ubuntu container's Nginx installation from listening on port 80
  - Write a Bash script that configures the server to meet the specified requirements
  - Expected behavior: Nginx running and listening on port 80 of all the server’s active IPv4 IPs

## Script Execution and Testing

Execute the script with:

```bash
./0-nginx_likes_port_80 > /dev/null 2&>1
