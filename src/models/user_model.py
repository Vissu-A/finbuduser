'''
user database model module.
'''

# standard python imports
from uuid import uuid4
from datetime import datetime, timezone

# standard fastapi imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, UUID, Date, Boolean, DateTime

# third-party imports

# internal imports

Base = declarative_base()

class MyUser(Base):
    '''
    Custom user model class.
    '''
    # Defining table name for the model in the database.
    __tablename__ = "users" # Table is created with given name in database.

    # 1. Definfing state of the model by creating attributes/fields.

    # Fields: AII(Account Identification Information): Required
    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    passcode = Column(String(25), nullable=False, unique=False)

    # Fields: PII(Personal Identification Information): Optional
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(10), nullable=True)
    dp = Column(String(275), nullable=True)

    # Fields: ACCII(Access Identification Information): Default
    is_active = Column(Boolean, nullable=False, default=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    # Fields: ACTII(Activity Identification Information): Default
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc)
        )
    logged_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc)
        )

    # 2. Defining Behaviour of the model by creadting methods.
    def __str__(self) -> str:
        return f"MyUser<id={self.uid}, username={self.name}, email={self.email}>"
