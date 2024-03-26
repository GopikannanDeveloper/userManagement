from rest_framework.views import exception_handler

def handle_exception(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response_data = {
            "statuscode": response.status_code,
             "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
                "Content-Type": "application/json"
            },
            "body":{"message":response.data.get("detail", "An error occurred.") }
            }
        response.data = response_data
    return response