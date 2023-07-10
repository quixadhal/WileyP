# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from Mud.db_system import DataBase


class Option(DataBase):
    __tablename__ = 'option'

    date_created = Column(DateTime(timezone=True), primary_key=True, server_default=func.now())
    date_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    version = Column(String)
    port = Column(Integer, default=4400)
    wizlock = Column(Boolean, default=False)
