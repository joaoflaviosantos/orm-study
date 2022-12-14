from typing import Optional
from sqlmodel import Field, SQLModel, Column, VARCHAR


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # https://github.com/tiangolo/sqlmodel/issues/65
    #name: str
    #name: str = Field(sa_column=Column("name", VARCHAR, unique=True))
    name: str = Field(sa_column_kwargs={"unique": True}, index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
