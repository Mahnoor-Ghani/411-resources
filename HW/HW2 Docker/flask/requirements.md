# Functional and Non-Functional Requirements

## **Functional Requirements**
1. The application shall return a JSON response containing a greeting message when accessed via the root (`/`) endpoint.
2. The application shall accept an optional `name` parameter in the query string and include it in the response message.
3. The application shall provide a health check endpoint (`/health`) that returns a JSON response indicating system status.
4. The application shall listen on a configurable port set via an environment variable (`PORT`).
5. The application shall be containerized using Docker and run in a Docker container.
6. The application shall expose the configured port to allow access from outside the container.

## **Non-Functional Requirements**
1. The application shall be highly available and capable of restarting automatically in case of failure.
2. The response time for requests shall not exceed 500 milliseconds under normal load.
3. The application shall follow security best practices, including restricting debug mode for production use.
4. The Docker container shall use a minimal and secure base image to reduce vulnerabilities.
5. The container shall pass a health check every 30 seconds to ensure continued functionality.
6. The application shall be lightweight, with a container image size kept as small as possible.

