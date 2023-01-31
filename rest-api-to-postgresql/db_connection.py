from sqlalchemy.engine.url import URL


def get_url_postgres(username, password, host, port, dbname):
   return(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}')