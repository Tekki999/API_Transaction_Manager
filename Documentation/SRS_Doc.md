# Software Requirements Specification (SRS)

**Project Title:** API Transaction Manager – Simulating Reliable API Calls  
**Author:** Andre Wright
**Date:** November 7, 2025  
**Version:** 1.0

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the API Transaction Manager. The system simulates reliable API interactions by implementing retry logic, idempotency enforcement, transaction logging, and failure recovery mechanisms.

### 1.2 Scope
The API Transaction Manager will:
- Accept transaction requests via RESTful endpoints
- Simulate API calls with configurable failure modes
- Implement retry policies with exponential backoff
- Enforce idempotency using unique keys
- Log transaction metadata
- Provide endpoints for querying transaction status and accessing logs

### 1.3 Definitions, Acronyms, and Abbreviations
- **API**: Application Programming Interface  
- **Idempotency**: Property ensuring repeated requests produce the same result  
- **DLQ**: Dead Letter Queue  
- **SLA**: Service Level Agreement

---

## 2. Overall Description

### 2.1 Product Perspective
This is a standalone simulation tool for developers and system architects to test reliable API transaction patterns.

### 2.2 Product Functions
- Submit transaction requests  
- Simulate API call failures  
- Retry failed calls  
- Enforce idempotency  
- Log transaction metadata  
- Provide status and log retrieval endpoints

### 2.3 User Classes and Characteristics

| User Role     | Description                                           |
|---------------|-------------------------------------------------------|
| Developer     | Tests retry and idempotency logic                     |
| QA Engineer   | Validates transaction behavior under failure          |
| Architect     | Evaluates system design patterns and fault tolerance  |

### 2.4 Operating Environment
- OS: Linux, Windows  
- Language: Python 3.x  
- Frameworks: Flask or FastAPI  
- Database: SQLite or PostgreSQL  
- Optional: Redis, Docker

---

## 3. Specific Requirements

### 3.1 Functional Requirements

| ID   | Requirement         | Description                                      |
|------|---------------------|--------------------------------------------------|
| FR1  | Submit Transaction  | Accept transaction requests via POST endpoint    |
| FR2  | Retry Logic         | Retry failed API calls up to N times             |
| FR3  | Backoff Strategy    | Support exponential backoff between retries      |
| FR4  | Idempotency         | Reject duplicate transactions using unique keys  |
| FR5  | Logging             | Log all transaction attempts and outcomes        |
| FR6  | Status Endpoint     | Provide GET endpoint to query transaction status |
| FR7  | Failure Simulation  | Simulate API failures with configurable rates    |

### 3.2 Non-Functional Requirements

| ID    | Requirement     | Description                                      |
|-------|-----------------|--------------------------------------------------|
| NFR1  | Performance     | Handle 1000 transactions per minute              |
| NFR2  | Reliability     | Prevent duplicate processing of idempotent calls |
| NFR3  | Usability       | Provide OpenAPI/Swagger documentation            |
| NFR4  | Extensibility   | Support plug-in modules for new failure types    |
| NFR5  | Portability     | Run on Linux and Windows environments            |

---

## 4. Acceptance Criteria

| ID   | Criteria              | Test Method                                               |
|------|-----------------------|-----------------------------------------------------------|
| AC1  | Retry logic works     | Submit failing transaction and verify retry attempts      |
| AC2  | Idempotency enforced  | Submit same transaction twice and verify second is rejected |
| AC3  | Logs are complete     | Verify logs contain metadata for each transaction         |
| AC4  | Failure simulation    | Configure 50% failure rate and verify outcomes            |
| AC5  | Status endpoint       | Query transaction and verify correct status is returned   |

---

## 5. Traceability Matrix

| Requirement ID | Acceptance Criteria ID |
|----------------|------------------------|
| FR1            | AC1, AC5               |
| FR2            | AC1                    |
| FR4            | AC2                    |
| FR5            | AC3                    |
| FR7            | AC4                    |