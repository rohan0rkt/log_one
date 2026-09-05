import requests


def send_report(report):

    try:

        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=report,
            timeout=5
        )

        response.raise_for_status()

        return response

    except requests.exceptions.RequestException as error:

        print("API request failed:", error)

        return None