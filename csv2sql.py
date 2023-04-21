# Import dependencies
import csv
import os

# Define input and output paths
csv_file_path = "input.csv"
output_sql_file_path = "output.sql"   # SQL-table will have same name as this file name

def csv_to_sql(csv_file_path, output_sql_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)

        table_name, _ = os.path.splitext(os.path.basename(output_sql_file_path))

        with open(output_sql_file_path, 'w', encoding='utf-8') as sql_file:
            sql_file.write('SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";\n')
            sql_file.write('START TRANSACTION;\n')
            sql_file.write('SET time_zone = "+00:00";\n\n')

            sql_file.write('/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;\n')
            sql_file.write('/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;\n')
            sql_file.write('/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;\n')
            sql_file.write('/*!40101 SET NAMES utf8mb4 */;\n\n')

            sql_file.write(f'--\n-- Database: `{table_name}`\n--\n\n')
            sql_file.write('-- --------------------------------------------------------\n\n')
            sql_file.write(f'--\n-- Table structure for table `{table_name}`\n--\n\n')

            sql_file.write(f'CREATE TABLE `{table_name}` (\n')
            for i, header in enumerate(headers):
                sql_file.write(f'  `{header}` text')
                if i < len(headers) - 1:
                    sql_file.write(',\n')
            sql_file.write('\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n')

            sql_file.write('COMMIT;\n')

csv_to_sql(csv_file_path, output_sql_file_path)