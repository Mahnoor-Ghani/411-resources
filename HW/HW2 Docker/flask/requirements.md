# Project Requirements for GiggleGit Demo Onboarding

## Goal:
Create an intuitive and stable demo for GiggleGit that can start onboarding adventurous clients.

## Non-Goal:
Do not implement advanced features like integration with third-party systems or complex branching scenarios.

---

## Non-Functional Requirements

### 1. Security
Ensure that only authorized users and developers can access sensitive components of GiggleGit and the onboarded clients’ data.

#### Functional Requirements:
- Implement user authentication via OAuth2 to ensure secure login.
- Secure storage of sensitive data (like API keys) using environment variables or encryption.

### 2. Scalability
Ensure that GiggleGit can handle multiple onboarded clients and their interactions with Git repositories.

#### Functional Requirements:
- Set up load balancing for servers handling multiple client requests.
- Ensure that the system can store user settings and repositories without performance degradation as new clients are onboarded.

---

## Agile User Stories

### User Story 1:
**As a vanilla git power-user who has never seen GiggleGit before, I want to experience the demo smoothly and without confusion, so I can understand how GiggleGit improves the version control process.**

#### Task:
Create a clean onboarding UI.

#### Tickets:
- **Ticket 1:** Design the demo UI  
    Design a user-friendly interface that will guide users through the onboarding experience of GiggleGit without overwhelming them.
- **Ticket 2:** Implement tooltips and guided instructions  
    Add tooltips or onboarding steps within the app to guide users, explaining key features and differences from traditional git tools.

---

### User Story 2:
**As a team lead onboarding an experienced GiggleGit user, I want to quickly get them set up so they can start using the version control system and integrating it with their existing workflows.**

#### Task:
Set up and optimize client-specific onboarding.

#### Tickets:
- **Ticket 1:** Create a personalized onboarding flow  
    Implement a flow that allows experienced users to skip unnecessary steps but still provides insights into the key differences in GiggleGit's functionalities.
- **Ticket 2:** Provide repository migration instructions  
    Provide clear and concise instructions for migrating repositories from a traditional git setup to GiggleGit.

---

### User Story 3:
**As a product manager, I want the demo to be stable, so clients can explore the core features without any downtime or bugs.**

#### Task:
Improve demo stability and performance.

#### Tickets:
- **Ticket 1:** Implement error handling and logging  
    Ensure that GiggleGit logs errors and provides informative error messages that can help both users and developers.
- **Ticket 2:** Optimize for performance  
    Profile the system to identify bottlenecks and optimize performance for key user interactions.

---

## Formal Requirements for SnickerSync Diff Tool

### Goal:
Create a diff tool (SnickerSync) that syncs with GiggleGit to allow users to merge code with humor.

### Non-Goal:
Do not introduce custom conflict resolution algorithms or integrate SnickerSync with third-party services.

---

## Non-Functional Requirements for SnickerSync

### 1. Usability
Ensure that the SnickerSync diff tool is easy to use and does not add complexity to the user's workflow.

#### Functional Requirements:
- The tool should display a clear and simple UI showing the differences between code versions.
- Allow users to apply changes with a single click, without requiring additional configuration or steps.

### 2. Reliability
Ensure SnickerSync works consistently and accurately, even with large repositories.

#### Functional Requirements:
- SnickerSync should not crash or produce errors during typical usage.
- Implement automated testing to verify the correctness of the diff and sync operations.

---

