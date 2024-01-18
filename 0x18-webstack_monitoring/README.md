0x18. Webstack Monitoring
Project Overview
This project focuses on implementing monitoring solutions for a web stack using Datadog, a popular monitoring and analytics platform. The objectives include signing up for Datadog, installing the Datadog agent on a server, and creating monitors and dashboards to track system metrics.

Learning Objectives
By the end of this project, you are expected to:

Understand the importance of monitoring in the tech industry.
Differentiate between application monitoring and server monitoring.
Explain the purpose of access logs and error logs for a web server like Nginx.
Resources
What is server monitoring
What is application monitoring
System monitoring by Google
Nginx logging and monitoring

Tasks
Task 0: Sign up for Datadog and Install Datadog Agent
Objective: Sign up for a Datadog account, install the Datadog agent on web-01, and create an application key.

Requirements:

Use the US website of Datadog: Datadog US.
Use the US1 region.
Install the Datadog agent on web-01.
Create an application key.
Copy-paste the DataDog API key and application key in your Intranet user profile.
Ensure web-01 is visible in Datadog under the hostname XX-web-01.
Task 1: Monitor Some Metrics
Objective: Set up monitors within the Datadog dashboard to monitor read and write requests issued to the device per second.

Requirements:

Set up a monitor for the number of read requests issued to the device per second.
Set up a monitor for the number of write requests issued to the device per second.
Task 2: Create a Dashboard
Objective: Create a new Datadog dashboard with at least 4 widgets, displaying various metrics.

Requirements:

Create a new dashboard.
Add at least 4 widgets of any type, monitoring different metrics.
Create a file named 2-setup_datadog with the dashboard_id on the first line.
