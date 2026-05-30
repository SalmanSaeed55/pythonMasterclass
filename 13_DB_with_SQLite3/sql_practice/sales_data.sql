-- SQL Script to create a normalized database for aggregate function demonstration

-- Enable Foreign Key enforcement
PRAGMA foreign_keys = ON;

-- Drop existing tables to allow re-running the script
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Regions;
DROP TABLE IF EXISTS Departments;

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL UNIQUE
);

-- Create Regions table
CREATE TABLE Regions (
    RegionID INTEGER PRIMARY KEY,
    RegionName TEXT NOT NULL UNIQUE
);

-- Create Products table
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT NOT NULL UNIQUE,
    UnitPrice REAL NOT NULL
);

-- Create Employees table with Foreign Key to Departments
CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    NickName TEXT,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER NOT NULL,
    Salary REAL NOT NULL,
    HireDate TEXT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create Sales table with Foreign Keys to Regions and Products
CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY,
    RegionID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    SaleDate TEXT,
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert data into Departments
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (1, 'IT');
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (2, 'HR');
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (3, 'Marketing');
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (4, 'Finance');

-- Insert data into Regions
INSERT INTO Regions (RegionID, RegionName) VALUES (1, 'North');
INSERT INTO Regions (RegionID, RegionName) VALUES (2, 'South');
INSERT INTO Regions (RegionID, RegionName) VALUES (3, 'East');
INSERT INTO Regions (RegionID, RegionName) VALUES (4, 'West');

-- Insert data into Products
INSERT INTO Products (ProductID, ProductName, UnitPrice) VALUES (1, 'Widget A', 5.00);
INSERT INTO Products (ProductID, ProductName, UnitPrice) VALUES (2, 'Widget B', 15.50);
INSERT INTO Products (ProductID, ProductName, UnitPrice) VALUES (3, 'Widget C', 25.00);

-- Insert data into Employees
INSERT INTO Employees (EmployeeID, FirstName, NickName, LastName, DepartmentID, Salary, HireDate) VALUES
(1, 'John', Null, 'Doe', 1, 75000, '2020-01-15'),
(2, 'Jane', Null, 'Smith', 2, 65000, '2019-05-23'),
(3, 'Michael', 'Mike', 'Brown', 1, 82000, '2018-09-10'),
(4, 'Emily', 'Em', 'Davis', 3, 70000, '2021-03-12'),
(5, 'David', 'Dave', 'Wilson', 4, 85000, '2017-11-30'),
(6, 'Sarah', Null, 'Johnson', 2, 62000, '2022-07-01'),
(7, 'Christopher', 'Chris', 'Lee', 3, 72000, '2020-08-19'),
(8, 'Anna', Null, 'Kim', 1, 78000, '2021-12-05'),
(9, 'Robert', Null, 'Hall', 4, 90000, '2016-04-15'),
(10, 'Laura', 'Whitey', 'White', 1, 76000, '2019-11-01');

-- Insert data into Sales
INSERT INTO Sales (SaleID, RegionID, ProductID, Quantity, SaleDate) VALUES
(1, 1, 1, 10, '2025-11-01'),
(2, 2, 2, 5, '2025-11-02'),
(3, 3, 1, 20, '2025-11-03'),
(4, 4, 3, 7, '2025-11-04'),
(5, 1, 2, 12, '2025-11-05'),
(6, 2, 1, 8, '2025-11-06'),
(7, 3, 3, 15, '2025-11-07'),
(8, 4, 2, 6, '2025-11-08'),
(9, 1, 3, 9, '2025-11-09'),
(10, 2, 3, 4, '2025-11-10'),
(11, 1, 1, 15, '2025-11-11'),
(12, 3, 2, 10, '2025-11-12');
