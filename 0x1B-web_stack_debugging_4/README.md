Project Explanation: 0x1B. Web stack debugging #4
Overview
The project focuses on debugging a web server setup that utilizes Nginx and is experiencing performance issues under pressure. The specific problem is a high number of failed requests during a benchmarking test using ApacheBench. The goal is to optimize the web server configuration to handle the load successfully and minimize the number of failed requests.

Project Details
Author: Elizabeth E NdZukule

Tasks
0. Sky is the limit, let's bring that limit higher 
The primary task involves testing the web server setup under pressure using ApacheBench. The benchmark consists of making 2000 HTTP requests to the server with 100 requests sent simultaneously. Currently, there are 943 failed requests, indicating a performance issue. The objective is to troubleshoot and optimize the web server configuration to eliminate failed requests.

Requirements
General
Environment: All files will be interpreted on Ubuntu 14.04 LTS.
File Formatting: All files should end with a new line.
Documentation: A README.md file at the root of the project folder is mandatory.
Puppet Manifests
Linting: Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Execution: Puppet manifests must run without error.
Documentation: The first line of Puppet manifests must be a comment explaining the manifest's purpose.
File Naming: Puppet manifest files must end with the extension .pp.
Version Compatibility: Files will be checked with Puppet v3.4.
Puppet-lint Installation
bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
Project Execution
Clone Repository: Clone the project repository.

bash

$ git clone https://github.com/your-username/your-repository.git
Navigate to Project Directory: Change into the project directory.

bash

$ cd your-repository
Apply Puppet Manifests: Execute the Puppet manifests to implement the required changes.

bash

$ puppet apply <filename>.pp
Benchmarking with ApacheBench: Run ApacheBench to simulate the load and test the web server's performance.

bash
$ ab -n 2000 -c 100 http://your-server-url
Check Logs: Inspect the server logs, especially the error log, for any issues.
