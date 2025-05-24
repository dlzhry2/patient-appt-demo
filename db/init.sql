CREATE TABLE IF NOT EXISTS patients (
    nhs_number integer PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    postcode VARCHAR(8) NOT NULL
);
