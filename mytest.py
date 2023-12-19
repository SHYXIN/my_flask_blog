from itsdangerous import URLSafeTimedSerializer

serializer = URLSafeTimedSerializer('123213')

sd = serializer.dumps({"confirm": 123})

print(sd)

timeout = 10

print("Please click on the confirmation link just sent "
                f"to your email address within {timeout} hours "
                "to complete you registration")
