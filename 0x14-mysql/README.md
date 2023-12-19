# 0x14. MySQL

## Overview
This project involves database administration tasks focusing on MySQL installation, user management, replication setup, and database backup strategies. It emphasizes understanding primary-replica clusters, backup strategies, and MySQL configuration.

## Concepts
This project expects familiarity with the following concepts:
- Database administration
- Web stack debugging
- How to install MySQL 5.7

## Learning Objectives
Upon completion of this project, you are expected to comprehend the following without external assistance:
- The primary role of a database
- Database replication and its significance
- Importance of storing database backups in different physical locations
- Regular operations required to validate a database backup strategy

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- Files ending with a new line
- Mandatory README.md at the project root
- Executable Bash script files
- Bash scripts passing Shellcheck (version 0.3.7-5~ubuntu16.04.1)
- Bash scripts starting with `#!/usr/bin/env bash`
- Bash scripts' second line explaining their purpose

## Tasks
### Task 0: Install MySQL
Install MySQL 5.7.x on web-01 and web-02 servers.

### Task 1: Let us in!
Create a MySQL user named `holberton_user` on both web-01 and web-02 with specified privileges.

### Task 2: If only you could see what I've seen with your eyes
Set up a database with a table and an entry in your primary MySQL server.

### Task 3: Quite an experience to live in fear, isn't it?
Create a new user for the replica server on web-01.

### Task 4: Setup a Primary-Replica infrastructure using MySQL
Establish a primary-replica infrastructure using MySQL for the tyrell_corp database.

### Task 5: MySQL backup
Create a Bash script for generating MySQL dumps and archiving them.
