# 🔒 Secure Task Manager API  

A **backend API** built with **Flask** that manages tasks securely, with user authentication, password hashing, and JWT-based access control.  
Designed as a portfolio project to showcase **backend development** and **cybersecurity best practices**.  

---

## 🚀 Features
- ✅ **User Authentication**
  - Register new users with **bcrypt-hashed passwords**  
  - Login with **JWT tokens** for secure access  

- ✅ **Task Management**
  - Create, Read, Update, Delete (CRUD) tasks  
  - Only accessible with valid JWT  

- ✅ **Security Focus**
  - Password hashing with bcrypt  
  - JWT authentication  
  - Input validation & error handling  
  - Structure ready for future 2FA & rate limiting  

---

## 🛠 Tech Stack
- **Language:** Python  
- **Framework:** Flask  
- **Database:** SQLite (default) / PostgreSQL (optional)  
- **Authentication:** Flask-JWT-Extended  
- **Security:** bcrypt, dotenv  
- **DevOps Ready:** Docker & GitHub Actions (future improvement)  

---

## 📂 Project Structure
