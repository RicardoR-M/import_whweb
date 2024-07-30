# Import WH Web Tool 🚀

[![GitHub](https://img.shields.io/badge/GitHub-RicardoR--M-blue?style=flat-square&logo=github)](https://github.com/RicardoR-M)

## 🌟 Overview

This Data Import Tool is designed to automate the process of importing data from Excel files into SQL databases. It's particularly useful for managing multiple data sources and tables.

## 🔑 Features

- 📊 Supports multiple Excel file imports
- 🗃️ Configurable database connections
- 🔄 Automatic table creation and data insertion
- 🎨 Rich console output with status updates
- 🛠️ Easily extendable for additional services

## 📦 Requirements

- Python 3.x
- SQLAlchemy
- pandas
- rich
- pymssql

## 🛠️ Setup

1. Clone the repository:
   ```
   git clone https://github.com/RicardoR-M/import-wh-web-tool.git
   cd import-wh-web-tool
   ```

2. Install the required packages:
   ```
   pip install sqlalchemy pandas rich pymssql
   ```

3. Set up your database connection string as an environment variable:
   ```
   export DB_CONN='your_database_connection_string_here'
   ```

## 🚀 Usage

1. Place your Excel files in the `../data/` directory relative to the project root.

2. Run the main script:
   ```
   python main.py
   ```

3. The tool will process each configured service, importing data from the Excel files into the specified SQL tables.

4. Check the console output for import status and any error messages.

## ⚙️ Configuration

Modify the `config/Servicios.py` file to add or change the services for data import. Each service should specify:

- `file_name`: The name of the Excel file to import
- `tabla`: The name of the SQL table where the data will be inserted

Example:
```python
servicios = [
    {
        'file_name': 'RECLAMOS.xls',
        'tabla': 'BO_ATC'
    },
    # Add more services here
]
```

## 📦 Building Executable

To create a standalone executable, use PyInstaller with the provided `main.spec` file:

```
pyinstaller main.spec
```

This will create an executable in the `dist` directory.

## 📄 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.