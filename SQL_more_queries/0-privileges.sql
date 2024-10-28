-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT GRANTEE, PRIVILEGE_TYPE
FROM information_schema.user_privileges
WHERE GRANTEE IN ('\'user_0d_1\'@\'localhost\'','\'user_0d_2\'@\'localhost\'');