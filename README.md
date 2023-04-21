# CSV to SQL Table Structure Converter

## Description

This Python script reads a CSV file and generates an SQL script to create a table with the same column names as the input CSV. The table name will be the same as the output SQL file name (without the file extension). This script does not include data from the CSV file, only the table structure.

## Features

- Reads a CSV file and extracts column names.
- Generates an SQL script to create a table with the same column names as the input CSV.
- The table name in the SQL script is based on the output SQL file name.
- Only the table structure is created, no data is imported from the CSV file.

## Usage

1. Update the `csv_file_path` variable with the path to your input CSV file.
2. Update the `output_sql_file_path` variable with the path where you want to save the output SQL file.
3. Run the script using `python script_name.py`, replacing `script_name` with the name of the script file.

## Example

Given an input CSV file `input.csv` with the following content:
prolificId,participantId,condition,status,screeningTime
001,101,A,active,2021-10-01
002,102,B,active,2021-10-02


And the output SQL file name `output.sql`, the generated SQL script will be:

```sql
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `output`
--

-- --------------------------------------------------------

--
-- Table structure for table `output`
--

CREATE TABLE `output` (
  `prolificId` text,
  `participantId` text,
  `condition` text,
  `status` text,
  `screeningTime` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;
```

- This script is useful when you need to create a table structure in your SQL database based on the column names from a CSV file.


