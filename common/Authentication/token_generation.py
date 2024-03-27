# import jwt
# from datetime import datetime, timedelta
# from django.conf import settings

# def generate_jwt_token(user_id):
#     print("userid in generate",user_id)
#     payload = {
#         'user_id': user_id,
#         'key':'Expenses Tracking Application',
#         'exp': datetime.utcnow() + timedelta(days=1)
#     }
#     token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
#     return token
