# CodeSync Architecture

## Overview

CodeSync is an automated LeetCode-to-GitHub synchronization platform.

The system detects successful LeetCode submissions, retrieves submission and problem metadata, formats the solution, and synchronizes it with a GitHub repository.

## High-Level Architecture

```text
LeetCode
    |
    v
Chrome Extension
    |
    | HTTP/REST
    v
FastAPI Backend
    |
    +----------------+
    |                |
    v                v
Sync Service      PostgreSQL
    |
    +-------------------+
    |         |         |
    v         v         v
LeetCode  Formatter  GitHub
Service    Service    Service
                         |
                         v
                  GitHub Repository

React Dashboard
       |
       v
FastAPI Backend