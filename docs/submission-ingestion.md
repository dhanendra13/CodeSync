# Submission Ingestion Architecture

## Overview

CodeSync receives coding-submission data through a browser-extension bridge.

The extension is responsible for collecting submission information from the user's active coding workflow and sending a normalized submission payload to the CodeSync backend.

The backend does not depend on the browser DOM or LeetCode-specific implementation details.

## Submission Flow

```text
User solves problem
        |
        v
Submit solution
        |
        v
Accepted submission
        |
        v
CodeSync Extension
        |
        v
Normalize submission
        |
        v
POST /api/v1/submissions
        |
        v
CodeSync Backend
        |
        +----------------+
        |                |
        v                v
   PostgreSQL        Sync Service
                         |
                         v
                   GitHub Service
                         |
                         v
                  GitHub Repository