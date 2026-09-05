def create_report(result):

    report = {}

    for ip, attempts in result.items():

        if attempts <= 2:
            severity = "LOW"

        elif attempts <= 4:
            severity = "MEDIUM"

        else:
            severity = "HIGH"

        report[ip] = {
            "failed_login": attempts,
            "severity": severity
        }

    return report