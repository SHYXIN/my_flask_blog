from itsdangerous import URLSafeTimedSerializer

serializer = URLSafeTimedSerializer('123213')

sd = serializer.dumps({"confirm": 123})

print(sd)

timeout = 10

print("Please click on the confirmation link just sent "
                f"to your email address within {timeout} hours "
                "to complete you registration")

from enum import Flag, auto

class Permissions(Flag):
    """This internally defined class creates the
    permissions bitmasks. It's internal here
    just to contain it within the scope of the
    Role class

    Args:
        Flag (enum.Flag): The bitmask value of a permissions
    """
    REGISTERED = auto()
    EDITOR = auto()
    ADMINISTRATOR = auto()
print(Permissions.REGISTERED)
print(Permissions.REGISTERED.value)

print(Permissions.EDITOR)
print(Permissions.EDITOR.value)

print((Permissions.REGISTERED | Permissions.EDITOR).value)

print(Permissions.ADMINISTRATOR)
print(Permissions.ADMINISTRATOR.value)


print((Permissions.REGISTERED | Permissions.EDITOR | Permissions.ADMINISTRATOR).value)



