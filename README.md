## Query for Create Table

**Create Districts Table**

```sql
CREATE TABLE `distriks` (
  `distrik_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nama_distrik` varchar(255) NOT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `ibu_kota_distrik` varchar(255) DEFAULT NULL,
  `nama_kepala_distrik` varchar(255) DEFAULT NULL,
  `foto_kepala_distrik` varchar(255) DEFAULT NULL,
  `foto_kantor` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `telp` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `peta_distrik` geometry DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`distrik_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
	
	
**Create Villages Table**

```sql
CREATE TABLE `desas` (
  `desa_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `distrik_id` bigint(20) UNSIGNED DEFAULT NULL,
  `nama_desa` varchar(255) NOT NULL,
  `nama_kepala_desa` varchar(255) DEFAULT NULL,
  `foto_kepala_desa` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `telp` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `foto_kantor` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `jumlah_penduduk` varchar(255) DEFAULT NULL,
  `peta_desa` geometry DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`desa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
	
	
**Import this sql file to Table**

1. [`distriks_dump.sql`](./distriks_dump.sql): 
2. [`desas_dump.sql`](./desas_dump.sql): 
	
	
**Create by [antheiz](https://github.com/antheiz)**
