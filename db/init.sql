CREATE TABLE IF NOT EXISTS patients (
    nhs_number VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    postcode VARCHAR(8) NOT NULL
);

CREATE INDEX idx_nhs_number on patients(nhs_number);
