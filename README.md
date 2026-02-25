Asset Management System (CE301)

This project is a web-based Asset Management System developed as part of the CE301 module. It provides a simple platform for managing physical assets, reporting faults, and viewing asset information through role-based dashboards.

The system is designed to simulate a real-world asset management workflow in an organisational setting (e.g. facilities management, transport depots, IT equipment tracking).

Key Features

User authentication with role-based access (e.g. Admin, Technician, Asset Manager)

Asset registration and tracking

QR code support for asset identification

Fault reporting linked to specific assets

Dashboards for different user roles

Asset and fault status management

Basic reporting and data export functionality

Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite (local development)

QR code generation and scanning

Deployed version (if applicable): PythonAnywhere

How It Works (High-Level)

Users log in and are assigned a role.
Assets can be created and managed in the system.
Faults can be reported against assets (e.g. when equipment breaks).
Technicians and managers can view, update, and resolve reported issues.
QR codes can be used to quickly access asset details.

Project Structure

Django project structure

Apps for assets, fault reporting, user management, and dashboards

Templates for role-based views

Static files for styling

Setup (Local Development)

Clone the repository

Create and activate a virtual environment

Install dependencies

Run database migrations

Start the development server

(Exact commands may vary depending on your local setup.)

Notes

This project was developed for academic purposes and is intended as a demonstration of a full-stack asset management system using Django. It is not production-hardened.
