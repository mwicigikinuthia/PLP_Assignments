--SQL script to create tables for a clinic booking system

-- Drop tables if they exist (for repeated execution)
DROP TABLE IF EXISTS appointment_specialties;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS specialties;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS patients;

-- Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    gender ENUM('Male', 'Female', 'Other') NOT NULL
);

-- Doctors Table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    hire_date DATE NOT NULL
);

-- Specialties Table
CREATE TABLE specialties (
    specialty_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Many-to-Many: Doctors and Specialties
CREATE TABLE appointment_specialties (
    doctor_id INT,
    specialty_id INT,
    PRIMARY KEY (doctor_id, specialty_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (specialty_id) REFERENCES specialties(specialty_id)
);

-- Rooms Table
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    floor INT NOT NULL
);

-- Appointments Table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    room_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
