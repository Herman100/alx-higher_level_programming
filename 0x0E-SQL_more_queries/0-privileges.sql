-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
SELECT User, Host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, Index_priv, Alter_priv
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2') AND Host = 'localhost';
