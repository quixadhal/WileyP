# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from alembic.migration import MigrationContext
from alembic.config import Config
from alembic.script import ScriptDirectory
from alembic import command
import Mud.log_system
from Mud.log_system import Loggers

log_boot = Loggers.addLogger('BOOT')

DB_NAME = 'wileyp'
ALEMBIC_CONFIG = 'alembic.ini'

SQLEngine = create_engine('postgresql://@:5432/' + DB_NAME)
DataBase = declarative_base()
SessionFactory = sessionmaker(bind=SQLEngine)
Session = scoped_session(SessionFactory)


def init_db():
    connection = SQLEngine.connect()
    context = MigrationContext.configure(connection)
    current_revision = context.get_current_revision()
    #current_revision = None
    log_boot.info('Database revision: %s', current_revision)
    if current_revision is None:
        DataBase.metadata.create_all(SQLEngine)

    config = Config(ALEMBIC_CONFIG)
    script = ScriptDirectory.from_config(config)
    head_revision = script.get_current_head()
    #head_revision = None
    if current_revision is None or current_revision != head_revision:
        log_boot.info('Upgrading database to version %s.', head_revision)
        command.upgrade(config, 'head')
        #from Mud.option import Option
        #session = Session()
        #options = session.query(Option).first()
        #if options is None:
        #    options = Option()
        #options.version = head_revision
        #session.add(options)
        #session.commit()
