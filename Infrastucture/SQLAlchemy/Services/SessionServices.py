from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from Application.Services.ConfigurationService import ConfigurationService
from Domain.Entities.Base import Base

class SessionService() : 

        _dbContext:Session = None
        _sessionMaker:sessionmaker = None
        _engine:Engine = None
        _configurationService:ConfigurationService = None

        def __init__(self, configurationService:ConfigurationService) :
            self._configurationService = configurationService
            self._engine = \
                create_engine(self._configurationService.SqliteConnectionString)\
                .execution_options(autocommit=False)
            self._sessionMaker = sessionmaker(bind=self._engine)

        @property
        def Engine(self) -> Engine: 
            return self._engine
            
        @property
        def DBContext(self) -> Session :
            if not self._dbContext :
                self._dbContext = self._sessionMaker()
            return self._dbContext

        def _CheckDataBaseExists(self) :
            if not database_exists(self._engine.url):
                create_database(self._engine.url)

        def _GenerateAllTables(self) : 
            Base.metadata.create_all(self._engine, Base.metadata.tables.values(),checkfirst=True)