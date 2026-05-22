# Personal Finance + Portfolio Tracker

## OOP Concepts Used

Classes & Objects → `Stock`, `Crypto`, `SavingsAcc`, `Portfolio`  
Abstraction → `Asset` used as the abstract base class  
Inheritance → All asset types inherit from `Asset`  
Polymorphism → `get_net_worth()` calls `get_value()` on different asset types  
Encapsulation → Financial data handled within class structures  
Composition → `Portfolio` stores and manages `Asset` objects  
Dunder Methods → `__str__`, `__len__`, `__iter__`  
File Handling → Portfolio data stored using JSON

---

## Overview

A simple Python-based portfolio tracker built to practice Object-Oriented Programming concepts through a real-world use case.

The project manages different asset types and calculates total portfolio value using a modular and extensible structure.

---

## Project Structure

```text
finance-portfolio-tracker/
│
├── models/
│   ├── __init__.py
│   ├── asset.py
│   ├── portfolio.py
│   └── transaction.py
│
├── data/
│   └── portfolio.json
│
├── main.py
├── masterfile.py
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd finance-portfolio-tracker
```

3. Run the application

```bash
python main.py
```

---

## What I Learned

Built practical understanding of OOP concepts by applying them in a real project structure.

The main takeaway was understanding polymorphism — `Portfolio` can call `get_value()` on every asset object without needing to know its exact type.

Each asset class handles its own implementation independently.