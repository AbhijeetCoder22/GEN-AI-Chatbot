#Internal Database Queries

user_creation_query = "INSERT INTO users_tbl (fullname, username, mailid, password) VALUES (%s,%s,%s,%s)"
duplicate_check_query = "SELECT COUNT(*) FROM users_tbl WHERE username = %s OR mailid = %s"
user_details_fetch_query = "SELECT * FROM USERS_TBL WHERE USERNAME = %s"
add_promt_query = "INSERT INTO prompt_info(prompt_name,prompt_text,prompt_type,user_id) VALUES (%s,%s,%s,%s)"
get_promt_query = "SELECT * FROM prompt_info WHERE user_id = %s ORDER BY prompt_id"
update_prompt_query = "UPDATE prompt_info SET prompt_text = %s WHERE prompt_id = %s AND user_id = %s"
delete_prompt_query = "DELETE FROM prompt_info WHERE prompt_id = %s AND user_id = %s"
get_only_prompt_query = "SELECT prompt_text,prompt_type FROM prompt_info WHERE user_id = %s ORDER BY prompt_id"
insert_client_db_cred_query = "INSERT INTO client_db_connections_info (db_type, db_host_name, db_user, db_password, database_name, db_port, db_service_name, db_driver,user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
get_client_db_cred_query = "SELECT * FROM client_db_connections_info WHERE user_id = %s"
update_client_db_cred_query = "UPDATE client_db_connections_info SET db_type = %s, db_host_name = %s, db_user = %s, db_password = %s, database_name = %s, db_port = %s, db_service_name = %s, db_driver = %s WHERE id = %s AND user_id = %s"