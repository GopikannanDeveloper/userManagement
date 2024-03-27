from rest_framework.response import Response

def valid_data_response( **kwargs):
    if kwargs and 'status_code' in kwargs and 'detail' in kwargs:
        statuscode = kwargs['status_code']
        response_data = {
            "statuscode": statuscode,
            "body":{"data":kwargs['detail'] }
            }
    else:
        statuscode = 500
        response_data = {
            "statuscode": statuscode,
            "body":{"message":'error occured' }
            }

    return Response(response_data,status=statuscode)


def valid_response( **kwargs):
    if kwargs and 'status_code' in kwargs and 'detail' in kwargs:
        statuscode = kwargs['status_code']
        response_data = {
            "statuscode": statuscode,
            "body":{"message":kwargs['detail'] }
            }
    else:
        statuscode = 500
        response_data = {
            "statuscode": statuscode,
            "body":{"message":'error occured' }
            }

    return Response(response_data,status=statuscode) 