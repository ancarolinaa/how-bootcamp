from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
  'postgresql+psycopg2://root:root@localhost/test_db')

sql = '''
select * from vw_song;
'''

df_songs = pd.read_sql_query(sql, engine)

df_artist = pd.read_sql_query('select * from tb_artist', engine)


# Revisar essa parte:
sql = '''
insert into tb_artist (
select t1."date"
	,t1."rank"
	,t1.artist
	,t1.song
from public."Billboard" as t1
where t1.artist like 'Adelle'
order by t1.artist, t1.song, t1."date"
);
'''