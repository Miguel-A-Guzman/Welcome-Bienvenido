--============================================================
--SCRIPT FOR CREATION OF DATABASE 'data_warehouse' AND SCHEMES
--'bronze', 'silver' and 'gold'.
--============================================================
/*
-----------------------------------------------------------------------
WARNING: The following script search a database named 'data_warehouse'.
If it finds it, it will delete it and create a new one. It is
mandatory to verify the existence of the database before proceeding.
-----------------------------------------------------------------------
Description: The following script search a database (DB) named 'data_warehouse'.
If it finds it, it will delete it and create a new one.
Next, the DB will be used to create three schemes: 'bronze',
'silver' and 'gold', which will be used respectively for the next layers.
*/
USE master;
GO
--Serch for existing DB 'data_warehouse' if it finds it, it will delete it.
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'data_warehouse')
	DROP DATABASE data_warehouse;
GO
--Creation of the new DB 'data_warehouse'
CREATE DATABASE data_warehouse;
GO

USE data_warehouse;
GO
--Creation of schemes.
CREATE SCHEMA bronze;
GO
CREATE SCHEMA silver;
GO
CREATE SCHEMA gold;
GO
