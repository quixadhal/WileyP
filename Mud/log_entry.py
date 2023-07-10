# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

from sqlalchemy import Column, BigInteger, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from Mud.db_system import DataBase


class LogEntry(DataBase):
    __tablename__ = 'log_entry'

    date_created = Column(DateTime(timezone=True), primary_key=True, server_default=func.now())
    level = Column(String, nullable=False)
    module = Column(String)
    line = Column(Integer)
    message = Column(String, nullable=False)
    pid = Column(Integer)
    tid = Column(BigInteger)
    stack = Column(String)
