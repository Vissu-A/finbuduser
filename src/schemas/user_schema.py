'''
user schema module for serialization.
'''

# python imports
import re

# fastapi imports


# third-party imports
from pydantic import BaseModel
from pydantic import EmailStr, SecretStr, Field
from pydantic import field_validator, model_validator

# internal imports

class CreateUserSchema(BaseModel):
    '''Creating user schema serializer'''

    # Fields
    name: str = Field(repr=True, max_length=50)
    email: EmailStr = Field(repr=True)
    passcode: SecretStr
    confirm_passcode: SecretStr

    # Field validators
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        '''validate username'''

        # name can't be mepty
        if not value:
            raise ValueError("Username should not be empty.")


    @field_validator("passcode")
    @classmethod
    def validate_passcode(cls, value: SecretStr) -> SecretStr:
        '''validate password rules'''
        special_chars = ['!', '@', '#', '$', '&', '*', '?', '-', '_']
        escaped_chars = [re.escape(char) for char in special_chars]
        special_chr_pattern =  f"[{''.join(escaped_chars)}]"
        print(f"special charecters pattern: {special_chr_pattern}")
        val = value.get_secret_value()

        # Passcode should not be empty
        if not val:
            raise ValueError("Passcode should not be empty.")
        # Atleast one Uppercase letter
        if not re.search(r"[A-Z]", val):
            raise ValueError("Passcode must contain atleast one uppercase letter")
        # Atleast one Lowercase letter
        if not re.search(r"[a-z]", val):
            raise ValueError("Passcode must contain atleast one lowercase letter")
        # At least one digit
        if not re.search(r"\d", val):
            raise ValueError("Passcode must contain atleast one digit")
        # Atleast one Special character
        if not re.search(pattern=special_chr_pattern, string=val):
            raise ValueError(f"Passcode must contain one special character {special_chars}")

        return pwd

    # Model validators
    # There are 2 modes in model validator.
    # 1. after
    # 2. before

        # mode="after" -> means this validation function will run after the model is fully built/instantiated.
        # raw input data is assigned to the respective fields in the model, and all field validators have been executed.
        # All field validators are executed, which means all fields are validated and assigned values.
        # This allows us to perform validations, that depend on multiple fields or all the fields of the model.
    @model_validator(mode="after")
    def passcode_match(self):
        '''check both passcodes are same or not'''

        p1 = self.passcode.get_secret_value()
        p2 = self.confirm_passcode.get_secret_value()
        if p1 != p2:
            raise ValueError("Passcode mismatch identified...!")
        else:
            return self

        # mode="before" -> means this validation function will run before the model is built/instantiated.
        # This means that this validation function will run on raw input data before any field validators are executed, and before any values are assigned to the fields.
        # This allows us to perform validations/transformations on the raw input data before the model is created, which can be useful for tasks like data cleaning.
    # @model_validator(mode="before")
    # def passcode_strip(self, input_data: dict) -> dict:
    #     '''strip passcode fields before any other validation'''
    #     if "passcode" in input_data:
    #         input_data["passcode"] = input_data["passcode"].strip()
    #     if "confirm_passcode" in input_data:
    #         input_data["confirm_passcode"] = input_data["confirm_passcode"].strip()
    #     return input_data
