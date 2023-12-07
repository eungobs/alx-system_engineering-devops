# 0x10. HTTPS SSL

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
    - [0. World wide web](#0-world-wide-web)
    - [1. HAproxy SSL termination](#1-haproxy-ssl-termination)
- [Repo Structure](#repo-structure)

## Description

This project focuses on understanding HTTPS SSL, DNS configurations, and setting up HAproxy for SSL termination. It includes practical tasks to configure domains, subdomains, and SSL termination using HAproxy.

## Concepts

- DNS
- Web stack debugging

## Background Context

HTTPS SSL (HyperText Transfer Protocol Secure/Secure Sockets Layer) is a protocol used for secure communication over a computer network. When a website uses HTTPS, the connection between the browser and the website is encrypted, enhancing security and protecting sensitive information.

## Resources

- [What is HTTPS?](https://en.wikipedia.org/wiki/HTTPS)
- [What are the 2 main elements that SSL is providing](https://www.thesslstore.com/blog/2-main-elements-ssl-is-providing/)
- [HAProxy SSL termination on Ubuntu 16.04](https://www.haproxy.com/documentation/hapee/1-5r1/onepage/ssl.html)
- [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- Bash function - `awk`, `dig`

## Learning Objectives

At the end of this project, learners will understand:

- What HTTPS SSL is and its main roles
- The purpose of encrypting traffic
- What SSL termination means

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 16.04 LTS
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- Use `#!/usr/bin/env bash` as the first line in all Bash scripts
- Quiz questions included

## Tasks

### 0. World wide web

Configure the domain zone, create subdomains, and write a Bash script to display information about subdomains.

- Add subdomains `www`, `lb-01`, `web-01`, `web-02` to the domain
- Bash script should accept domain and subdomain arguments to display information about subdomains
- Use `awk` and at least one Bash function

### 1. HAproxy SSL termination

Configure HAproxy to accept encrypted traffic for subdomain www.

- HAproxy should listen on port TCP 443 and accept SSL traffic
- Serve encrypted traffic returning the root of the web server with the content "Holberton School"
- Share HAproxy config in `1-haproxy_ssl_termination` file

## Repo Structure

- **GitHub repository:** alx-system_engineering-devops
- **Directory:** 0x10-https_ssl
- **Files:**
    - `0-world_wide_web` (Bash script)
    - `1-haproxy_ssl_termination` (HAproxy configuration file)
