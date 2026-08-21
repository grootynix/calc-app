# Changelog

All notable changes to this project will be documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
Versioning follows [Semantic Versioning](https://semver.org/)

## [Unreleased]

## [0.1.0] - 2024-08-21
### Added
- Python FastAPI backend with /health and /calculate endpoints
- Expression validation with whitelist of allowed characters
- Division by zero and empty expression error handling
- React frontend with dark theme calculator UI
- Button grid with operators, parentheses, and clear/backspace
- API service layer connecting React to Python backend
- 11 unit and integration tests, all passing
- Monorepo structure with frontend/ and backend/ separation
- PR template and branch protection rules
- GitHub Milestone, Labels, and Project board setup

### Security
- eval() protected by character whitelist
- CORS configured for frontend-backend communication