0x17. Web Stack Debugging #3
Project Overview
This project focuses on debugging a Wordpress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. The goal is to investigate and resolve a 500 Internal Server Error returned by Apache using the strace tool. Once the issue is identified, the fix is to be automated using Puppet, as specified in the provided tasks.

Background Context
When debugging, logs might not provide enough information, and sometimes the issue requires going deeper into the stack. In this case, the students are tasked with investigating a Wordpress website running on a LAMP stack, where Apache is returning a 500 error. The challenge is to use strace to find the cause of the error and then automate the fix using Puppet.

Tasks
Task 0: Strace is Your Friend
Objective: Using strace, identify why Apache is returning a 500 error and automate the fix using Puppet.

Hints:

Strace can attach to a currently running process.
Use tmux to run strace in one window and curl in another.
Requirements:

The 0-strace_is_your_friend.pp file must contain Puppet code.
Any Puppet resource type can be used
...
Requirements
All files are interpreted on Ubuntu 14.04 LTS.
All files should end with a new line.
A README.md file at the root of the folder is mandatory.
Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Puppet manifests must run without error.
Puppet manifests' first line must be a comment explaining what the manifest is about.
Puppet manifest files must end with the extension .pp.
Files will be checked with Puppet v3.4.
Concepts
Web Server
Web Stack Debugging
