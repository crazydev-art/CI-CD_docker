Project Description:
This project is designed to automate the testing of a FastAPI-based application by orchestrating a multi-container environment using Docker. It includes the following components:

FastAPI Service:

A RESTful API that provides endpoints for authentication, authorization, and other business logic.
Testing Containers:

Multiple containers designed to test different aspects of the FastAPI service (e.g., authentication, authorization, and content management).
Each container runs Python scripts to simulate requests and validate API responses against expected outcomes.
Centralized Logging:

All test results are written to a shared volume, consolidating logs into a single file for easy access and analysis.
Docker Compose Setup:

Simplifies the deployment of the entire environment, enabling seamless integration and communication between services using shared networks and volumes.
Key Features:

Efficient automation of API testing workflows.
Centralized log management for tracking and debugging.
Lightweight, containerized infrastructure for portability and scalability.
