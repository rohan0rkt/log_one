
def detect_login(logs):

    failed_ips = {}

    for log_entry in logs:

        if "Failed login" in log_entry:
            ip = log_entry.split()[0]
            failed_ips[ip] = failed_ips.get(ip, 0) + 1

    return failed_ips

def detect_sql_injection(logs):

    sql_injection ={}

    for log_entry in logs:
        if " OR " in log_entry or " 'OR' " in log_entry :
            ip = log_entry.split()[0]
            sql_injection[ip] = sql_injection.get(ip,0) + 1

    return sql_injection        

def detect_path_traversal(logs):

    path_traversal ={}

    for log_entry in logs:
        if "../" in log_entry:
            ip = log_entry.split()[0]
            path_traversal[ip]= path_traversal.get(ip,0) + 1

    return path_traversal        

def analyze_logs(logs):
    brute_force = detect_login(logs)
    sql_injection = detect_sql_injection(logs)
    path_traversal = detect_path_traversal(logs)

    return {
        "BRUTE_FORCE": brute_force,
        "SQL_INJECTION": sql_injection,
        "PATH_TRAVERSAL": path_traversal
    }
