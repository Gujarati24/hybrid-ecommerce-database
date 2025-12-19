# Hybrid E-Commerce Database System Using MySQL and MongoDB  
### M605 – Advanced Databases  
### Student: Tomik Gujarati | Student ID: GH1026955  

---

## 📌 Project Overview  
This project demonstrates a **hybrid SQL + NoSQL database architecture** suitable for modern e-commerce applications.  
It integrates:

- **MySQL** → for structured, transactional data  
- **MongoDB** → for flexible product documents and embedded reviews  
- **Python Integration Layer** → to connect and exchange data across both databases  

This architecture reflects real-world systems used by Amazon, Flipkart, Shopify, and other modern platforms.

---

## 📂 Folder Structure  



This project demonstrates a hybrid database architecture using **MySQL** for transactional data and **MongoDB** for flexible product data.

Below are the screenshots for the ER diagram and example outputs.

---

---

## 🏗 System Architecture  
### Hybrid SQL–NoSQL Architecture

![System Architecture](docs/screenshots/architecture.png)

This diagram shows how the Python layer interacts with both databases:

- Sends SQL queries to **MySQL**
- Sends document queries to **MongoDB**
- Aggregates results into a unified output layer

---

## 🔄 Data Flow Diagram  
Shows how data moves between the user, integration layer, MySQL, and MongoDB.

![Data Flow Diagram](docs/screenshots/dataflow.png)

---

## 🗂 ER Diagram (MySQL)

![ER Diagram](docs/screenshots/er_diagram1.png)

Tables include:

- Users  
- Orders  
- Order Items  
- Products (SQL metadata)  

---

## 💾 Database Components  

### ✔ MySQL  
Used for ACID-compliant transactions:

- Users  
- Orders  
- Order Items  
- Minimal product metadata  

### ✔ MongoDB  
Used for flexible, schema-free product storage:

- Product details  
- Embedded customer reviews  
- Dynamic attributes  

---

## 🧪 Results & Screenshots  

### 📊 SQL Aggregation Query
![SQL Aggregation](docs/screenshots/mysql_aggregation.png)

### 🧮 MongoDB Aggregation Pipeline
![MongoDB Aggregation](docs/screenshots/mongo_aggregation.PNG)

### 📝 MongoDB Product Document
![MongoDB Document](docs/screenshots/mongo_document.png)

### 🖥 Python Integration Output
![Python Output](docs/screenshots/integration_output.png)

---

## ▶ How to Run This Project  

### 1️⃣ Install Dependencies  
```bash
pip install pymongo mysql-connector-python


## ER Diagram
![ER Diagram](docs/screenshots/er_diagram1.png)

---

## MySQL Screenshots

### Tables
![MySQL Tables](docs/screenshots/mysql_tables.png)

### JOIN Query Output
![MySQL Join](docs/screenshots/mysql_join.png)

### Aggregation Query Output
![MySQL Aggregation](docs/screenshots/mysql_aggregation.png)

---

## MongoDB Screenshots

### Product Documents
![MongoDB Document](docs/screenshots/mongo_document.png)

### Aggregation Pipeline Output
![MongoDB Aggregation](docs/screenshots/mongo_aggregation.PNG)

---

## Python Integration Output
![Integration Output](docs/screenshots/integration_output.png)
