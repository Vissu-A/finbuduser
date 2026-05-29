'''
user schema module for serialization.
'''

# standard python imports
# standard fastapi imports
from pydantic import BaseModel, Field, EmailStr, SecretStr
from pydantic import field_validator

# third-party imports

# internal imports

class CreateUserModel(BaseModel):
    '''Creating user schema serializer'''

    name: str = Field(repr=True, max_length=50)
    email: EmailStr = Field(repr=True)
    passcode: SecretStr = Field(repr=False, min_length=8)
    confirm_passcode: SecretStr = Field(repr=False)

    # Validate passcode rules: 
        # Minimum length of 8 characters
        # combination of alpha-numeric
        # special charecters
        # combination of upper and lower case letters
    @field_validator("passcode")
    @classmethod
    def validated_passcode(cls, value: SecretStr) -> SecretStr:
        '''function to validate passcode rules.'''
