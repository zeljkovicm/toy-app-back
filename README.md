The backend is built with **Python** and **FastAPI**, following a layered architecture inspired by Clean Architecture principles. It exposes a REST API for the frontend, integrates with the external **Pequla Toy API**, and manages internal domain data such as users, orders, reviews, and stock.

**FastAPI** – Web framework (async REST API)
- **Python**
- **PostgreSQL** – Primary database
- **SQLModel** – ORM + Pydantic modeling
- **Alembic** – Database migrations
- **Poetry** – Dependency & environment management