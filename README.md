# borg-report
 
This script prints the details of all the
archives in the borg repo as well as some of
the details of the borg repo

>This script doesn't have any error checking...yet. 

Sample report:
+---------------------------------------------------------------------------------------------------------+
|                                            Borg Backup Report                                           |
+--------------+--------------------------------------+------------+----------+------------+--------------+
| Hostname     | Archive                              |    Date    | Original | Compressed | Deduplicated |
+--------------+--------------------------------------+------------+----------+------------+--------------+
| sample-host1 | sample-host1-daily-2024-02-13-0200   | 2024-02-13 |  39.3 GB |    36.7 GB |     118.9 MB |
| sample-host1 | sample-host1-daily-2024-02-12-0200   | 2024-02-12 |  39.3 GB |    36.9 GB |     271.8 MB |
| sample-host1 | sample-host1-daily-2024-02-11-0452   | 2024-02-11 |  38.9 GB |    36.7 GB |     114.0 MB |
| sample-host1 | sample-host1-weekly-2024-02-10-1901  | 2024-02-10 |  38.9 GB |    36.7 GB |      64.6 MB |
| sample-host1 | sample-host1-daily-2024-02-09-1800   | 2024-02-09 |  40.9 GB |    38.5 GB |     211.5 MB |
| sample-host1 | sample-host1-daily-2024-02-08-1800   | 2024-02-08 |  40.8 GB |    38.5 GB |     340.4 MB |
| sample-host1 | sample-host1-monthly-2024-01-31-1800 | 2024-01-31 |  32.3 GB |    30.1 GB |     306.5 MB |
| sample-host1 | sample-host1-weekly-2024-01-27-1800  | 2024-01-27 |  32.7 GB |    30.5 GB |     274.2 MB |
| sample-host1 | sample-host1-weekly-2024-01-20-1800  | 2024-01-20 |  31.6 GB |    29.9 GB |     262.8 MB |
| sample-host1 | sample-host1-weekly-2024-01-06-1800  | 2024-01-06 |  32.1 GB |    30.0 GB |     305.5 MB |
| sample-host1 | sample-host1-monthly-2023-12-31-1800 | 2023-12-31 |  32.1 GB |    30.1 GB |     199.0 MB |
| sample-host1 | sample-host1-weekly-2023-12-30-1800  | 2023-12-30 |  31.3 GB |    29.3 GB |     176.1 MB |
| sample-host1 | sample-host1-weekly-2023-12-23-1800  | 2023-12-23 |  31.4 GB |    29.3 GB |     398.3 MB |
| sample-host1 | sample-host1-weekly-2023-12-16-1800  | 2023-12-16 |  29.2 GB |    28.0 GB |      74.0 MB |
| sample-host1 | sample-host1-weekly-2023-12-09-1800  | 2023-12-09 |  29.2 GB |    28.0 GB |      85.7 MB |
| sample-host1 | sample-host1-monthly-2023-12-02-1029 | 2023-12-02 |  30.1 GB |    28.9 GB |       1.1 GB |
+--------------+--------------------------------------+------------+----------+------------+--------------+
