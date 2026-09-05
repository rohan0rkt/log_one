import json

from analyzer import analyze_logs
from report import create_report
from api import send_report


with open("logs.txt", "r") as file:
    logs = file.readlines()


if logs:

    result_log = analyze_logs(logs)

    new_report_brute = create_report(result_log["BRUTE_FORCE"])
    new_report_injection = create_report(result_log["SQL_INJECTION"])
    new_report_traversal = create_report(result_log["PATH_TRAVERSAL"])

    # print(json.dumps(new_report_brute, indent=4))
    # print(json.dumps(new_report_injection, indent=4))

    final_report ={

         " Brute_Force ": new_report_brute,
         "SQL_Injection":new_report_injection,
         "Path_Traversal":new_report_traversal
    }

    with open("report.json", "w") as file:
        json.dump(final_report, file, indent=4)

    response = send_report(new_report_brute)

    if response:

            print("API Status:", response.status_code)
            print("API Response:", response.json())  
    else:
         print("could not send the report")
else:

    print("Log file is empty")