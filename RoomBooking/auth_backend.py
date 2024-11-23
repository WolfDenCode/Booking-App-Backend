# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model


# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, email=None, **kwargs):
#         """
#         Authenticate using email and password.
#         """
#         UserModel = get_user_model()
#         # Use the email field explicitly
#         if email is None:
#             # email = username  # Handle compatibility with authenticate calls
#             return None
        
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user
#         return None
