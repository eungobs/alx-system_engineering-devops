# 0x0C Web Server

This repository comprises tasks related to Web Servers, covering setup, configuration, and management topics in DevOps and SysAdmin.

## Project Description

This project focuses on various aspects of web server management, including transferring files, installing and configuring Nginx, setting up domain names, handling redirection, and customizing error pages. The tasks aim to reinforce skills in server configuration, automation with scripting and Puppet, DNS setup, and Nginx server management.

## Tasks Overview

### Task 0: Transfer a File to Your Server
- Script that transfers a file from a client to a server using `scp`.

### Task 1: Install Nginx Web Server
- Bash script to install and configure Nginx on an Ubuntu server, ensuring it listens on port 80 and returns "Hello World!" on querying `/`.

### Task 2: Setup a Domain Name
- Set up a domain name without subdomains, configuring DNS records for the root domain to point to web-01 IP.

### Task 3: Redirection
- Configure Nginx to redirect `/redirect_me` to another page with a 301 status code.

### Task 4: Not Found Page 404
- Customize the Nginx server to display a custom 404 error page with the string "Ceci n'est pas une page" for non-existent pages.

### Task 5: Install Nginx Web Server (w/ Puppet)
- Puppet manifest to automate the installation and configuration of Nginx on an Ubuntu machine, including the setup for a 301 redirection.

## Task Details

Each task contains specific requirements and instructions within the project's directory.

- [0-transfer_file](./0x0C-web_server/0-transfer_file): Script to transfer files using `scp`.
- [1-install_nginx_web_server](./0x0C-web_server/1-install_nginx_web_server): Bash script to install and configure Nginx.
- [2-setup_a_domain_name](./0x0C-web_server/2-setup_a_domain_name): Set up a domain name and configure DNS records.
- [3-redirection](./0x0C-web_server/3-redirection): Configure Nginx for redirection.
- [4-not_found_page_404](./0x0C-web_server/4-not_found_page_404): Customize Nginx for a custom 404 error page.
- [7-puppet_install_nginx_web_server.pp](./0x0C-web_server/7-puppet_install_nginx_web_server.pp): Puppet manifest for Nginx installation.

## Getting Started

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/0x0C-web_server.git
    ```

2. Navigate to the respective task directory.

3. Follow the instructions in each task directory to execute or run the provided scripts.

## Author

Elizabeth Eunice Ndzukule.
