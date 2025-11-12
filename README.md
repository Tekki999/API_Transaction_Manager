# 📘 API Transaction Manager

**Author:** Andre Wright  
**Started:** October 2025  
**Completed:** November 7, 2025  
**Duration:** ~3 weeks  
**Version:** 1.0

---

## 🧠 Project Summary

The API Transaction Manager is a simulation tool designed to model reliable API interactions under failure conditions. It was built to demonstrate key principles of fault-tolerant system design, including:

- Retry logic with exponential backoff  
- Idempotency enforcement  
- Transaction logging  
- Failure simulation  
- Status querying via RESTful endpoints

This project was developed as part of a systems reliability and API design study, with a strong focus on requirements engineering, traceability, and testable acceptance criteria.

---

## 🎯 Goals

- Build a robust FastAPI backend that simulates real-world transaction behavior  
- Validate retry and idempotency logic through automated tests  
- Document the system using a formal Software Requirements Specification (SRS)  
- Ensure traceability between requirements and implementation  
- Provide a clean deployment path for developers and testers

---

## 🛠️ Technologies Used

- **Language:** Python 3.10  
- **Framework:** FastAPI  
- **Database:** SQLite (via SQLAlchemy)  
- **HTTP Client:** httpx  
- **Testing:** pytest  
- **Documentation:** Markdown (SRS), Swagger UI  
- **Optional:** Docker

---

## 📦 Development Timeline

| Phase              | Dates              | Description                                      |
|--------------------|--------------------|--------------------------------------------------|
| Requirements Draft | Oct 15–18, 2025     | Wrote SRS and acceptance criteria                |
| Core API Build     | Oct 19–25, 2025     | Developed `/submit`, retry, idempotency, logging |
| Database Integration | Oct 26–30, 2025   | Added SQLite persistence and status endpoint     |
| Testing & Docs     | Nov 1–6, 2025       | Wrote unit tests, finalized Swagger + README     |
| Completion         | Nov 7, 2025         | Final review and deployment guide                |

---

## ✅ Completion Status

All features outlined in the SRS have been implemented and validated. The project is considered complete for version 1.0. Future enhancements may include:

- Modular failure simulation plug-ins  
- Rate limiting and authentication  
- Performance benchmarking  
- Dashboard UI for transaction history

---
